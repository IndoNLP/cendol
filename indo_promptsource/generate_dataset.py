import logging
import argparse
import pandas as pd

from tqdm import tqdm
from promptsource.templates import DatasetTemplates
from nusacrowd import NusantaraConfigHelper

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


def dataset_generator(dataset_name: str, subset_name: str, total_partition: int):

    # Set Config of NusaCrowd to stream the data
    conhelps = NusantaraConfigHelper()

    # Load dataset (only obtain the first value returned from config filter)
    nusa_metadata = conhelps.filtered(lambda x: dataset_name in x.dataset_name and subset_name in x.config.name)[0]
    dset = nusa_metadata.load_dataset()

    dataset_name = nusa_metadata.dataset_name
    subset_name = nusa_metadata.config.name
    logger.info("============================================")
    logger.info(f"## DATASET INFO ##")
    logger.info(f"Real dataset_name: {dataset_name}")
    logger.info(f"Real subset_name: {subset_name}")
    logger.info(f"dset.shape: {dset.shape}")
    logger.info(f"Example dataset: {dset['train'][0]}")
    logger.info("============================================")

    for dset_key in dset.keys():
        for ind in range(total_partition):
            yield dataset_name, subset_name, dset_key, dset[dset_key].shard(num_shards=total_partition, index=ind)


def generate_t2t_from_prompts(hf_dataset_generator, split_on_prompts: bool, total_partition: int, checkpoint_save_path: str = "generated_dataset"):

    logger.info(f"Dataset Partition: {total_partition}")
    for partition_num, (dataset_name, subset_name, dataset_key, dataset_shard) in tqdm(
        enumerate(hf_dataset_generator, start=1),
            total=total_partition, position=0, desc="Generating T2T Dataset on Partitioned fashion"):

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
                df_.to_csv(f"{checkpoint_save_path}/{dataset_name}-{subset_name}-partition-{partition_num}-prompt-{prompt_num}.csv")
                all_data = []
            else:
                #accumulate over all prompts, pass this condition
                pass

        if not split_on_prompts:
            df_ = pd.DataFrame(all_data)
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
    parser.add_argument("--checkpoint-save-path", help="Relative path of saved T2T CSV",
            default="checkpoint_save_path")

    args = parser.parse_args()

    # example expected args
    # dataset_name = "korpus_nusantara"
    # subset_name = "korpus_nusantara_msa_ind_nusantara"
    # num_shard = 10
    # split_on_prompts = True

    # Set variable from args parser
    dataset_name = args.dataset_name
    subset_name = args.subset_name
    num_shard = args.num_shard
    split_on_prompts = args.split_on_prompts
    checkpoint_save_path = args.checkpoint_save_path

    logger = set_logger()

    logger.info(f"Input dataset_name: {dataset_name}")
    logger.info(f"Input subset_name: {subset_name}")

    logger.info(f"Input num_shard: {num_shard}")
    logger.info(f"Input split_on_prompts: {split_on_prompts}")

    generate_t2t_from_prompts(dataset_generator(dataset_name, subset_name, total_partition = num_shard),
                                split_on_prompts = split_on_prompts, total_partition = num_shard)
