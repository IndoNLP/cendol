import os
import logging
import argparse

import pandas as pd
import multiprocessing as mp

import concurrent.futures as cf

from tqdm import tqdm
from functools import partial
from nusacrowd import NusantaraConfigHelper

from collections.abc import Iterable
from concurrent.futures import ThreadPoolExecutor
from promptsource.templates import DatasetTemplates

parser = argparse.ArgumentParser()

#create custom type-checking of incoming ArgParse
def argparse_bool_check(value: str):
    #cast str with value like float into actual float
    try:
        value = float(value)
    #can't be parsed as float, keep as it is
    except ValueError:
        pass

    #cast float-like value (incl int) into str
    if isinstance(value, float) and int(value) == value:
        value = str(int(value))
    #raise ArgumentTypeError if the value isn't in string already
    else:
        if not isinstance(value, str):
            raise argparse.ArgumentTypeError(f"Not the correct value (args: {value})! Expected is cast-able to '1' or '0' or already in string. Please rectify!")
    #check for these combinations of values
    if value.lower() in ("yes", "true", "t", "y", "1"):
        return True
    elif value.lower() in ("no", "false", "f", "n", "0"):
        return False
    else:
        raise argparse.ArgumentTypeError(f"Value Error! Not the correct value (args: {value})! Please rectify!")


def validate_nonzero_int(value: str):
    #cast str with value like float into actual float (later will be casted and validated into positive int)
    try:
        float(value)
    #can't be parsed as float, raise Error
    except ValueError:
        raise argparse.ArgumentTypeError(f"Not the correct value (args: {value})! Expected value should be cast-able to int. Please rectify!")
    else:
        value = float(value)

    #should be castable to int and exact (not rounded by 'int') and positive
    if isinstance(value, float) and int(value) == value and value > 0:
        return int(value)
    else:
        raise argparse.ArgumentTypeError(f"Value Error! Not the correct expected value (args: {value})! Please rectify!")


def set_logger():
    # Set up the logger
    logging.basicConfig(
        level=logging.DEBUG,  # Set the desired logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format='%(asctime)s [%(levelname)s]: %(message)s',  # Customize the log message format
        datefmt='%Y-%m-%d %H:%M:%S'  # Customize the date/time format
    )

    # Create a file handler to write logs into a file
    file_handler = logging.FileHandler('app.log')

    # Set the log level for the file handler
    file_handler.setLevel(logging.DEBUG) 

    # Create a formatter for the file handler (customize the log format for the file)
    file_formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(file_formatter)

    logger = logging.getLogger("IndoP3 Dataset Generation")
    logger.addHandler(file_handler)

    return logger


def __run_t2t_parallel(fn_to_execute, iterable_input, n_workers: int):
    if not isinstance(iterable_input, Iterable):
        raise TypeError("Received second args in 'run_parallel' isn't an iterable object!")
    with ThreadPoolExecutor(max_workers=n_workers) as p:
        futures = {p.submit(fn_to_execute, *args_input, iter_idx) for iter_idx, args_input in enumerate(iterable_input, start=1)}
        cf_futures = cf.as_completed(futures)
        try:
            next(cf_futures).result()
        except StopIteration:
            logger.info("All futures finished")
            pass


def dataset_generator(dataset_name: str, subset_name: str, total_partition: int):

    # Set Config of NusaCrowd to stream the data
    conhelps = NusantaraConfigHelper()

    # Load dataset (only obtain the first value returned from config filter)
    nusa_metadata = conhelps.filtered(lambda x: dataset_name in x.dataset_name and subset_name in x.config.name)[0]
    dataset = nusa_metadata.load_dataset()

    dataset_name = nusa_metadata.dataset_name
    subset_name = nusa_metadata.config.name
    logger.info("============================================")
    logger.info(f"## DATASET INFO ##")
    logger.info(f"Real dataset_name: {dataset_name}")
    logger.info(f"Real subset_name: {subset_name}")
    logger.info(f"Dataset Shape: {dataset.shape}")
    logger.info(f"Example dataset: {dataset['train'][0]}")
    logger.info("============================================")

    for dataset_key in dataset.keys():
        for ind in range(total_partition):
            yield dataset[dataset_key].shard(num_shards=total_partition, index=ind), dataset_name, subset_name, dataset_key


def generate_t2t_from_prompts(dataset_shard, dataset_name, subset_name, dataset_key, partition_num,
                              split_on_prompts: bool, checkpoint_save_path: str = "generated_dataset"):

        all_data = []
        prompt = DatasetTemplates(dataset_name, subset_name=subset_name)

        # Iterate to each prompt templates
        for prompt_num, prompt_id in tqdm(enumerate(prompt.templates, start=1),
                                          total=len(prompt), position=1,desc="Iteration on Prompt"):
            template_name = prompt.templates[prompt_id].name

            for example in dataset_shard:
                data_details = {
                    "dataset_name": dataset_name,
                    "subset_name": subset_name,
                    "prompt_id": prompt_id,
                    "template_name": template_name,
                    "dataset_key": dataset_key,
                }
                input = None
                output = None

                try:
                    render = prompt[template_name].apply(example)
                    if len(render) != 2:
                        if len(render) == 1:
                            input = render[0]

                        logger.info(f"Output not available for {data_details}.")
                        break
                    else:
                        input = render[0]
                        output = render[1]
                except Exception as e:
                    logger.error(f"Exception occurred on {data_details}. Please rectify: {e}")
                    break

                data_details["input"] = input
                data_details["output"] = output

                #collect all single datapoints into collections
                all_data.append(
                    data_details
                )

            #decide whether want to split T2T DF generation on prompts or to continue
            if split_on_prompts:
                #directly create dataset after T2T has been generated
                df_ = pd.DataFrame(all_data)
                fn = f"{checkpoint_save_path}/{dataset_name}-{subset_name}-partition-{partition_num}-prompt-{prompt_num}.csv"
                df_.to_csv(fn)
                all_data = []
            else:
                #accumulate over all prompts, pass this condition
                pass

        if not split_on_prompts:
            df_ = pd.DataFrame(all_data)
            logger.info("Completed!")
            df_.to_csv(f"{checkpoint_save_path}/{dataset_name}-{subset_name}-partition-{partition_num}.csv")
            all_data = []
        else:
            #accumulate over all dataset generator, pass this condition
            pass


#only executed if called directly
if __name__ == "__main__":

    parser.add_argument("--dataset-name", help="Dataset name")
    parser.add_argument("--subset-name", help="Subset name")
    parser.add_argument("--split-on-prompts", help="Flag whether to split on prompts (useful for large ones)",
          default=False, type=argparse_bool_check)
    parser.add_argument("--num-shard", help="Partition Number of Dataset (useful for large ones)",
          default=1, type=validate_nonzero_int)
    parser.add_argument("--parallelize-flag", help="Flag whether to use parallelization (using async)",
          default=False, type=argparse_bool_check)
    parser.add_argument("--num-concurrent-process", help="Number of Concurrent Parallel Process",
          default=max(mp.cpu_count()-2, 1), type=validate_nonzero_int)
    parser.add_argument("--checkpoint-save-path", help="""Relative path of saved T2T CSV 
                        to the 'generate_dataset.py' script dir""",
            default="checkpoint_save_path")

    args = parser.parse_args()

    # example expected args
    # dataset_name = "korpus_nusantara"
    # subset_name = "korpus_nusantara_msa_ind_nusantara"
    # num_shard = 10
    # split_on_prompts = True

    logger = set_logger()

    logger.info("Parsing arguments...")

    # Set variable from args parser
    dataset_name = args.dataset_name
    subset_name = args.subset_name
    num_shard = args.num_shard
    split_on_prompts = args.split_on_prompts
    parallelize = args.parallelize_flag
    concurrent_process = min(args.num_concurrent_process, max(mp.cpu_count()-2, 1))
    checkpoint_save_path = args.checkpoint_save_path

    logger.info(f"Input dataset_name: {dataset_name}")
    logger.info(f"Input subset_name: {subset_name}")

    script_dirname = os.path.dirname(os.path.abspath(__file__))
    target_folder = os.path.join(script_dirname, checkpoint_save_path)

    if not os.path.isdir(target_folder):
        logger.info(f"Creating new dir in {target_folder}")
        os.mkdir(target_folder)
    else:
        logger.info(f"Dir {target_folder} already exists")

    if parallelize:
        logger.info(f"Using parallelization with concurrent process of {concurrent_process} from proposed process of {args.num_concurrent_process}")

    if split_on_prompts:
        logger.info(f"Using generation splitting based on prompts")

    if num_shard > 1:
        logger.info(f"Using generation splitting based on sharding with partition number of {num_shard}")

    partial_t2t_generation_fn = partial(generate_t2t_from_prompts, split_on_prompts = split_on_prompts, checkpoint_save_path=checkpoint_save_path)

    if not parallelize:
        for partition_num, args in tqdm(enumerate(dataset_generator(dataset_name, subset_name, total_partition = num_shard), start=1),
                total=num_shard, position=0, desc="Generating T2T Dataset on Partitioned fashion"):
            logger.info(f"Generating dataset sequentially of partition no {partition_num}")
            partial_t2t_generation_fn(*args, partition_num)
    #activate run parallelization on async
    else:
        logger.info(f"Generating dataset asyncronously...")
        __run_t2t_parallel(partial_t2t_generation_fn, dataset_generator(
                        dataset_name, subset_name, total_partition = num_shard),
                        n_workers=concurrent_process)