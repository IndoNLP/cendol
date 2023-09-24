import re
import os
os.environ['TRANSFORMERS_NO_ADVISORY_WARNINGS'] = 'true'
os.environ['HF_HOME'] = '/home/jovyan/.cache/huggingface'
os.environ['HUGGINGFACE_HUB_CACHE'] = '/home/jovyan/.cache/huggingface/hub'
os.environ['TRANSFORMERS_CACHE'] = '/home/jovyan/.cache/huggingface/hub'
os.environ['HF_DATASETS_CACHE'] = '/home/jovyan/.cache/huggingface/datasets'

import sys
import glob
import math
import logging
import argparse
import numpy as np
from typing import Dict, List, Optional, Sequence
from dataclasses import dataclass, field

import torch
import datasets
import transformers
from transformers import AutoModelForCausalLM, AutoTokenizer, LlamaTokenizer, Trainer, HfArgumentParser, TrainingArguments
from datasets import load_dataset, concatenate_datasets, DatasetDict

from peft import (
    LoraConfig,
    get_peft_model,
    get_peft_model_state_dict,
    set_peft_model_state_dict,
    prepare_model_for_int8_training,
)

logger = logging.getLogger(__name__)

IGNORE_INDEX = -100
DEFAULT_PAD_TOKEN = "[PAD]"
DEFAULT_EOS_TOKEN = "</s>"
DEFAULT_BOS_TOKEN = "<s>"
DEFAULT_UNK_TOKEN = "<unk>"


@dataclass
class ModelArguments:
    # Base model parameters
    model_name_or_path: Optional[str] = field(default=None)
    load_in_8bit: bool = field(
                default=False, metadata={"help": "Whether to convert the loaded model into mixed-8bit quantized model."}
    )
    # LoRA parameters
    use_lora: bool = field(default=False, metadata={"help": "Whether to use Lora or not."})
    lora_r: int = field(default=8, metadata={"help": "Lora rank."})
    lora_alpha: int = field(default=16, metadata={"help": "Lora alpha."})
    lora_dropout: float = field(default=0.05, metadata={"help": "Lora dropout."})
    lora_target_modules: str = field(default="q_proj,v_proj", metadata={"help": "Names of the modules to apply Lora to."})


@dataclass
class DataArguments:
    data_path: Optional[str] = field(default='MBZUAI/Bactrian-X', metadata={"help": "Path to the training file."})
    model_max_length: Optional[int] = field(
        default=1024, metadata={"help": "Maximum sequence length. Sequences will be right padded (and possibly truncated)."}
    )
    preprocessing_num_workers: Optional[int] = field(
        default=None, metadata={"help": "The number of processes to use for the preprocessing."}
    )
    sample_size: Optional[int] = field(default=-1, metadata={"help": "The maximum sample size from the whole dataset."})
    val_set_size: Optional[int] = field(default=2000, metadata={"help": "The validation set size. For loss checking."})

@dataclass
class BactrianTrainingArguments(TrainingArguments):
    optim: str = field(default="adamw_torch", metadata={"help": "Optimizer to use."})
    fp16: bool = field(
        default=True, metadata={"help": "Whether to use fp16 16-bit (mixed) precision training instead of 32-bit training."}
    )
    lang: str = field(default="zh", metadata={"help": "The language or language list separated by `,`, dataset will be downlaoded from HF Hub."})
    evaluation_strategy: str = field(default="steps", metadata={"help": ""})
    save_strategy: str = field(default="steps", metadata={"help": ""})
    wandb_project: str = field(default="bactrian", metadata={"help": "Weight & Bias (W&B) project name."})

# Copied from https://github.com/bofenghuang/stanford_alpaca/blob/eb5b171d9b103a12a8e14e0edca9cbc45fe1d512/train.py#L75-L95
def smart_tokenizer_and_embedding_resize(
    special_tokens_dict: Dict,
    tokenizer: transformers.PreTrainedTokenizer,
    model: transformers.PreTrainedModel,
):
    """Resize tokenizer and embedding.
    Note: This is the unoptimized version that may make your embedding size not be divisible by 64.
    """
    num_new_tokens = tokenizer.add_special_tokens(special_tokens_dict)
    model.resize_token_embeddings(len(tokenizer))

    if num_new_tokens > 0:
        input_embeddings = model.get_input_embeddings().weight.data
        output_embeddings = model.get_output_embeddings().weight.data

        input_embeddings_avg = input_embeddings[:-num_new_tokens].mean(dim=0, keepdim=True)
        output_embeddings_avg = output_embeddings[:-num_new_tokens].mean(dim=0, keepdim=True)

        input_embeddings[-num_new_tokens:] = input_embeddings_avg
        output_embeddings[-num_new_tokens:] = output_embeddings_avg

def train():
    # HF parser
    parser = HfArgumentParser((ModelArguments, DataArguments, BactrianTrainingArguments))
    model_args, data_args, training_args = parser.parse_args_into_dataclasses()

    # Setup logging
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%m/%d/%Y %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
    )

    if training_args.should_log:
        # The default of training_args.log_level is passive, so we set log level at info here to have that default.
        transformers.utils.logging.set_verbosity_info()

    log_level = training_args.get_process_log_level()
    logger.setLevel(log_level)
    datasets.utils.logging.set_verbosity(log_level)
    transformers.utils.logging.set_verbosity(log_level)
    transformers.utils.logging.enable_default_handler()
    transformers.utils.logging.enable_explicit_format()

    # Log on each process the small summary:
    logger.warning(
        f"Process rank: {training_args.local_rank}, device: {training_args.device}, n_gpu: {training_args.n_gpu}"
        + f"distributed training: {bool(training_args.local_rank != -1)}, 16-bits training: {training_args.fp16}"
    )
    # Set the verbosity to info of the Transformers logger (on main process only):
    logger.info(f"Model parameters {model_args}")
    logger.info(f"Training/evaluation parameters {training_args}")
    
    device_map = "auto"
    world_size = int(os.environ.get("WORLD_SIZE", 1))
    ddp = world_size != 1
    if ddp:
        device_map = {"": int(os.environ.get("LOCAL_RANK") or 0)}

    if 'wandb' in training_args.report_to:
         os.environ["WANDB_PROJECT"] = training_args.wandb_project

    model = AutoModelForCausalLM.from_pretrained(
        model_args.model_name_or_path,
        load_in_8bit=model_args.load_in_8bit,
        # device_map=device_map,
    )

    tokenizer = AutoTokenizer.from_pretrained(
        model_args.model_name_or_path,
        padding_side="right",
        use_fast=False,
    )
    
    # llama has no pad_token
    if tokenizer.pad_token is None:
        smart_tokenizer_and_embedding_resize(
            special_tokens_dict=dict(pad_token=DEFAULT_PAD_TOKEN),
            tokenizer=tokenizer,
            model=model,
        )

    if model_args.load_in_8bit:
        model = prepare_model_for_int8_training(model)
    else:
        model.enable_input_require_grads()

    if model_args.use_lora:
        config = LoraConfig(
            r = model_args.lora_r,
            lora_alpha = model_args.lora_alpha,
            target_modules = model_args.lora_target_modules.split(','),
            lora_dropout = model_args.lora_dropout,
            bias = "none",
            task_type = "CAUSAL_LM",
        )
        model = get_peft_model(model, config)
        model.print_trainable_parameters()

    # Load dataset from HF Hub
    # if training_args.lang != '':
    #     all_dataset = [load_dataset(data_args.data_path, lang) for lang in training_args.lang.split(',')]
    # merged_dataset = concatenate_datasets(list(map(lambda x: x['train'], all_dataset)))
    # raw_datasets = DatasetDict({'train':merged_dataset})
    raw_datasets = load_dataset("indonlp/nusa_t2t", use_auth_token=True)

    # Determine model_max_length for truncation
    model_max_length = data_args.model_max_length

    def generate_and_tokenize_prompt(data_point):
        full_prompt = f'{data_point["input"]} {data_point["output"]}'
        user_prompt = f'{data_point["input"]} '
        user_prompt_len = len(tokenizer(user_prompt, truncation=True, max_length=model_max_length)["input_ids"])
        tokenized_full_prompt = tokenizer(full_prompt + tokenizer.eos_token, truncation=True, max_length=model_max_length)
        tokenized_full_prompt["labels"] = [IGNORE_INDEX] * user_prompt_len + tokenized_full_prompt["input_ids"].copy()[user_prompt_len:]
        tokenized_full_prompt.pop('attention_mask')
        return tokenized_full_prompt

    # Sampling
    if data_args.sample_size > 0:
        raw_datasets["train"] = raw_datasets["train"].train_test_split(
            test_size=data_args.sample_size, shuffle=True, seed=42
        )['test']
        
    # Splitting
    if data_args.val_set_size > 0:
        train_val_data = raw_datasets["train"].train_test_split(
            test_size=data_args.val_set_size, shuffle=True, seed=42
        )
    else:
        raise ValueError("val_set_size must large than 0.")

    #with training_args.main_process_first(desc="dataset map tokenization"):
    train_data = train_val_data["train"].map(
        generate_and_tokenize_prompt,
        num_proc=data_args.preprocessing_num_workers,
        remove_columns=next(iter(raw_datasets.values())).column_names,
        desc="preprocess train data set",
    )
    val_data = train_val_data["test"].map(
        generate_and_tokenize_prompt,
        num_proc=data_args.preprocessing_num_workers,
        remove_columns=next(iter(raw_datasets.values())).column_names,
        desc="preprocess val data set",
    )

    trainer = Trainer(
        model = model,
        train_dataset = train_data,
        eval_dataset = val_data,
        args = training_args,
        data_collator = transformers.DataCollatorForSeq2Seq(
            tokenizer, pad_to_multiple_of=8, return_tensors="pt", padding=True
        ),
    )
    model.config.use_cache = False

    # old_state_dict = model.state_dict
    # model.state_dict = (
    #     lambda self, *_, **__: get_peft_model_state_dict(
    #         self, old_state_dict()
    #     )
    # ).__get__(model, type(model))

#     if torch.__version__ >= "2" and sys.platform != "win32":
#         model = torch.compile(model)

    trainer.train()

    model.save_pretrained(training_args.output_dir)


if __name__ == "__main__":
    train()
