import os, sys
import csv
from os.path import exists

import pandas as pd
from tqdm import tqdm
from prompt_utils import get_prompt, get_lang_name
from data_utils import load_nlg_datasets

import torch

from peft import PeftModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForCausalLM, BloomTokenizerFast, set_seed
from nusacrowd.utils.constants import Tasks

from sacremoses import MosesTokenizer
import datasets
from anyascii import anyascii
import openai
from retry import retry

openai.api_key = ""

DEBUG=True

""" Generation metrics """
bleu = datasets.load_metric('bleu')
rouge = datasets.load_metric('rouge')
sacrebleu = datasets.load_metric('sacrebleu')
chrf = datasets.load_metric('chrf')
squad_v2_metric = datasets.load_metric('squad_v2')
mt = MosesTokenizer(lang='id')

def generation_metrics_fn(list_hyp, list_label):
    # hyp and label are both list of string
    list_hyp_bleu = list(map(lambda x: mt.tokenize(x), list_hyp))
    list_label_bleu = list(map(lambda x: [mt.tokenize(x)], list_label))    
    list_label_sacrebleu = list(map(lambda x: [x], list_label))
    
    metrics = {}
    metrics["BLEU"] = bleu._compute(list_hyp_bleu, list_label_bleu)['bleu'] * 100
    metrics["SacreBLEU"] = sacrebleu._compute(list_hyp, list_label_sacrebleu)['score']
    metrics["chrF++"] = chrf._compute(list_hyp, list_label_sacrebleu)['score']
    
    rouge_score = rouge._compute(list_hyp, list_label)
    metrics["ROUGE1"] = rouge_score['rouge1'].mid.fmeasure * 100
    metrics["ROUGE2"] = rouge_score['rouge2'].mid.fmeasure * 100
    metrics["ROUGEL"] = rouge_score['rougeL'].mid.fmeasure * 100
    metrics["ROUGELsum"] = rouge_score['rougeLsum'].mid.fmeasure * 100
    
    return metrics


def to_prompt(input, prompt, prompt_lang, task_name, task_type, with_label=False, use_template=False):
    if '[INPUT]' in prompt:
        prompt = prompt.replace('[INPUT]', input['text_1'])

    if task_type == Tasks.MACHINE_TRANSLATION.value:
        # Extract src and tgt based on nusantara config name
        task_names = task_name.split('_')
        src_lang = task_names[-4]
        tgt_lang = task_names[-3]

        # Replace src and tgt lang name
        prompt = prompt.replace('[SOURCE]', get_lang_name(prompt_lang, src_lang))
        prompt = prompt.replace('[TARGET]', get_lang_name(prompt_lang, tgt_lang))
    
    if task_type == Tasks.QUESTION_ANSWERING.value:
        prompt = prompt.replace('[CONTEXT]', input['context'])
        prompt = prompt.replace('[QUESTION]', input['question'])
    
    if with_label:
        if task_type == Tasks.QUESTION_ANSWERING.value:
            prompt += " " + input['answer'][0]
        else:
            prompt += " " + input['text_2']

    if use_template:
        prompt_template = "### USER:\n{human_prompt}\n\n### RESPONSE:\n"
        prompt = prompt_template.format(human_prompt=prompt)
    
    return prompt


# They sometimes timeout
@retry(Exception, tries=5, delay=1)
def predict_generation_gpt(prompt, model_name):
    if "turbo" in model_name:
        response = openai.ChatCompletion.create(
          model=model_name,
          messages=[
                {"role": "user", "content": prompt},
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    else:
        response = openai.Completion.create(
            model=model_name,
            prompt=prompt,
            max_tokens=200,
          )
        return response['choices'][0]['text'].strip()


def predict_generation(prompts, model_name, tokenizer, model):
    if "gpt" in model_name or "text" in model_name:
        # AFAIK, ChatCompletion doesn't support batch input, so use single generation for now
        return [predict_generation_gpt(prompt, model_name) for prompt in prompts]

    inputs = tokenizer(prompts, return_tensors="pt", padding=True, truncation=True, max_length=1024).to('cuda')
    input_size = inputs["input_ids"].shape[1]

    if "sealion" in model_name:
        inputs.pop("token_type_ids", None)
    
    if model.config.is_encoder_decoder:
        outputs = model.generate(**inputs, do_sample=True, min_length=1, max_length=100)
        preds = tokenizer.batch_decode(outputs, skip_special_tokens=True) 
        return preds
    else:
        outputs = model.generate(**inputs, do_sample=True, 
            min_length=input_size+1, max_length=input_size+100)
        if "llama" in model_name:
            preds = [p.strip() for p in tokenizer.batch_decode(outputs[:,inputs["input_ids"].shape[1]:], skip_special_tokens=True)]
        else:
            preds = tokenizer.batch_decode(outputs[:,inputs["input_ids"].shape[1]:], skip_special_tokens=True)
        return preds

if __name__ == '__main__':
    if len(sys.argv) != 5:
        raise ValueError('main_nlg_prompt.py <prompt_lang> <model_path_or_name> <n_shot> <n_batch>')

    # TODO: reduce hardcoded vars
    out_dir = './outputs_nlg'
    metric_dir = './metrics_nlg'
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(metric_dir, exist_ok=True)

    prompt_lang = sys.argv[1]
    MODEL = sys.argv[2]
    N_SHOT = int(sys.argv[3])
    N_BATCH = int(sys.argv[4])
    SAVE_EVERY = 10
    ADAPTER = ''
    if 'bactrian' in MODEL:
        MODEL, ADAPTER = MODEL.split('---')

    # Load prompt
    prompt_templates = get_prompt(prompt_lang)

    # Load Dataset
    print('Load NLG Datasets...')
    nlg_datasets = load_nlg_datasets()

    print(f'Loaded {len(nlg_datasets)} NLG datasets')
    for i, dset_subset in enumerate(nlg_datasets.keys()):
        print(f'{i} {dset_subset}')

    # Set seed
    set_seed(42)

    # Load Model & Tokenizer
    # Tokenizer initialization
    trust_remote_code = "sealion" in MODEL
    use_prompt_template = "sealion" in MODEL and "instruct" in MODEL
    if "gpt" not in MODEL and "text" not in MODEL:
        tokenizer = AutoTokenizer.from_pretrained(MODEL, truncation_side='left', trust_remote_code=trust_remote_code)
        tokenizer.padding_side = "left"
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.bos_token if tokenizer.bos_token is not None else tokenizer.eos_token
    else:
        tokenizer = None

    # Model initialization
    fp16_args = {'device_map': "auto", 'torch_dtype': torch.float16, 'load_in_8bit': True}  # needed for larger model
    if ADAPTER != '':
        base_model = AutoModelForCausalLM.from_pretrained(MODEL, device_map="auto", load_in_8bit=True, resume_download=True)
        model = PeftModel.from_pretrained(base_model, ADAPTER, torch_dtype=torch.float16)
        MODEL = ADAPTER  # for file naming
    elif "gpt" in MODEL or "text" in MODEL:
        model = None
    elif "mt0" in MODEL or "mt5" in MODEL:
        extra_args = fp16_args if "xxl" in MODEL else {}
        model = AutoModelForSeq2SeqLM.from_pretrained(MODEL, resume_download=True, **extra_args)
        if "xxl" not in MODEL:
            model = model.to('cuda')
    else:
        extra_args = fp16_args if "7b" in MODEL.lower() or "13b" in MODEL.lower() else {}
        model = AutoModelForCausalLM.from_pretrained(MODEL, resume_download=True, trust_remote_code=trust_remote_code, **extra_args)
        if "SeaLLM" in MODEL or "llama" in MODEL:
            # quick fix for tensor error
            # https://github.com/facebookresearch/llama/issues/380
            model = model.bfloat16()
    
    if model is not None:
        model.eval()

    metrics = {'dataset': []}
    for i, dset_subset in enumerate(nlg_datasets.keys()):
        nlg_dset, task_type = nlg_datasets[dset_subset]
        print(f"{i} {dset_subset} {task_type}")
        
        if task_type.value not in prompt_templates or nlg_dset is None:
            continue

        if 'test' in nlg_dset.keys():
            data = nlg_dset['test']
        elif 'validation' in nlg_dset.keys():
            data = nlg_dset['validation']
        else:
            data = nlg_dset['train']
        few_shot_data = nlg_dset['train']

        for prompt_id, prompt_template in enumerate(prompt_templates[task_type.value]):
            inputs = []
            preds = []
            preds_latin = []
            golds = []  
            print(f"PROMPT ID: {prompt_id}")
            print(f"SAMPLE PROMPT: {to_prompt(data[0], prompt_template, prompt_lang, dset_subset, task_type.value, use_template=use_prompt_template)}")

            few_shot_text_list = []
            if N_SHOT > 0:
                for sample in tqdm(few_shot_data):
                    # Skip shot examples
                    if task_type != Tasks.QUESTION_ANSWERING and len(sample['text_1']) < 20:
                        continue
                    few_shot_text_list.append(
                        to_prompt(sample, prompt_template, dset_subset, task_type.value, with_label=True, use_template=use_prompt_template)
                    )
                    if len(few_shot_text_list) == N_SHOT:
                        break
            print(f'FEW SHOT SAMPLES: {few_shot_text_list}')
            
            # Zero-shot inference
            if exists(f'{out_dir}/{dset_subset}_{prompt_lang}_{prompt_id}_{N_SHOT}_{MODEL.split("/")[-1]}.csv'):        
                print("Output exist, use existing log instead")
                with open(f'{out_dir}/{dset_subset}_{prompt_lang}_{prompt_id}_{N_SHOT}_{MODEL.split("/")[-1]}.csv') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        inputs.append(row["Input"])
                        preds.append(row["Pred"])
                        preds_latin.append(row["Pred_Latin"])
                        golds.append(row["Gold"])
                print(f"Skipping until {len(preds)}")

            # If incomplete, continue
            if len(preds) < len(data):
                count = 0
                with torch.inference_mode():
                    prompts, batch_golds = [], []
                    for e, sample in enumerate(tqdm(data)):
                        if e < len(preds):
                            continue
                        
                        # Buffer
                        prompt_text = to_prompt(sample, prompt_template, prompt_lang, dset_subset, task_type.value, use_template=use_prompt_template)
                        prompt_text = '\n\n'.join(few_shot_text_list + [prompt_text])
                        prompts.append(prompt_text)
                        batch_golds.append(sample['answer'][0] if task_type == Tasks.QUESTION_ANSWERING else sample['text_2'])

                        # Batch inference
                        if len(prompts) == N_BATCH:
                            batch_preds = predict_generation(prompts, MODEL, tokenizer, model)
                            for (prompt_text, pred, gold) in zip(prompts, batch_preds, batch_golds):
                                inputs.append(prompt_text)
                                preds.append(pred)
                                preds_latin.append(anyascii(pred))
                                golds.append(gold)
                            prompts, batch_golds = [], []
                            count += 1

                        if count == SAVE_EVERY:
                            # partial saving
                            inference_df = pd.DataFrame(list(zip(inputs, preds, preds_latin, golds)), columns=['Input', 'Pred', 'Pred_Latin', 'Gold'])
                            inference_df.to_csv(f'{out_dir}/{dset_subset}_{prompt_lang}_{prompt_id}_{N_SHOT}_{MODEL.split("/")[-1]}.csv', index=False)
                            count = 0

                    # Predict the rest inputs
                    if len(prompts) > 0:
                        batch_preds = predict_generation(prompts, MODEL, tokenizer, model)
                        for (prompt_text, pred, gold) in zip(prompts, batch_preds, batch_golds):
                            inputs.append(prompt_text)
                            preds.append(pred)
                            preds_latin.append(anyascii(pred))
                            golds.append(gold)
                        prompts, batch_golds = [], []
            
            # Final save
            inference_df = pd.DataFrame(list(zip(inputs, preds, preds_latin, golds)), columns=['Input', 'Pred', 'Pred_Latin', 'Gold'])
            inference_df.to_csv(f'{out_dir}/{dset_subset}_{prompt_lang}_{prompt_id}_{N_SHOT}_{MODEL.split("/")[-1]}.csv', index=False)

            # To accomodate old bug where list are not properly re-initiated
            inputs = inputs[-len(data):]
            preds = preds[-len(data):]
            preds_latin = preds_latin[-len(data):]
            golds = golds[-len(data):]

            eval_metric = generation_metrics_fn(preds, golds)
            eval_metric_latin = generation_metrics_fn(preds_latin, golds)
            for key, value in eval_metric_latin.items():
                eval_metric[f'{key}_latin'] = value

            print(f'== {dset_subset} == ')
            for k, v in eval_metric.items():
                print(k, v)            
            print("===\n\n")
            eval_metric['prompt_id'] = prompt_id

            metrics['dataset'].append(dset_subset)
            for k in eval_metric:
                if k not in metrics:
                    metrics[k] = []
                metrics[k].append(eval_metric[k])


    pd.DataFrame.from_dict(metrics).reset_index().to_csv(f'{metric_dir}/nlg_results_{prompt_lang}_{N_SHOT}_{MODEL.split("/")[-1]}.csv', index=False)
