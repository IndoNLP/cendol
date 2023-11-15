from tqdm import tqdm
import pandas as pd
from promptsource.templates import DatasetTemplates
from nusacrowd import NusantaraConfigHelper
import logging
import argparse


def set_logger():
    # Set up the logger
    logging.basicConfig(
        level=logging.DEBUG,  # Set the desired logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format='%(asctime)s [%(levelname)s]: %(message)s',  # Customize the log message format
        datefmt='%Y-%m-%d %H:%M:%S'  # Customize the date/time format
    )

    # Create a file handler to write logs into a file
    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(logging.DEBUG)  # Set the log level for the file handler

    # Create a formatter for the file handler (customize the log format for the file)
    file_formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(file_formatter)

    logger = logging.getLogger("IndoP3 Dataset Generation")
    logger.addHandler(file_handler)

    return logger


logger = set_logger()

def dataset_generator(dataset_name: str, subset_name: str):
    """
    The function `dataset_generator` loads a dataset based on the provided dataset name and subset name,
    and returns the loaded dataset.

    input:
        dataset_name (str): The `dataset_name` parameter is a string that represents the name of the
            dataset you want to generate. It is used to filter the NusaCrowd dataset configurations and find the
            corresponding metadata for the dataset
        subset_name (str): The `subset_name` parameter is a string that represents the name of a specific
            subset within a dataset. It is used to identify and load a specific subset of data from the dataset
    output:
        a tuple of 3 consists of HF Dataset from NusaCrowd, actual dataset name,
        and actual subset name that matched w/ NusaCrowd Dataset List
    """
    #init conhelps of NusaCrowd
    conhelps = NusantaraConfigHelper()

    logger.info(f"Input dataset_name: {dataset_name}")
    logger.info(f"Input subset_name: {subset_name}")

    # Load dataset
    nusa_metadata = conhelps.filtered(lambda x: dataset_name in x.dataset_name and subset_name in x.config.name)[0]
    dataset_name = nusa_metadata.dataset_name
    subset_name = nusa_metadata.config.name
    dset = nusa_metadata.load_dataset()
    logger.info("============================================")
    logger.info(f"## DATASET INFO ##")
    logger.info(f"Real dataset_name: {dataset_name}")
    logger.info(f"Real subset_name: {subset_name}")
    logger.info(f"dset.shape: {dset.shape}")
    example = dset["train"][0]
    logger.info(f"Example dataset: {example}")
    logger.info("============================================")

    return dset, dataset_name, subset_name


def generate_t2t_from_prompts(dataset, dataset_name: str, subset_name: str,
                              checkpoint_save_path: str = "generated_dataset"):
    """
    The function `generate_t2t_from_prompts` takes a dataset, dataset name, subset name, and checkpoint
    save path as input, and generates a T2T (Text-to-Text) dataset from prompts.

    input:
        dataset (hf DatasetDict): The `dataset` parameter is a dictionary that contains the data for generating the
            T2T (Text-to-Text) dataset. Each key in the dictionary represents a dataset, and the corresponding
            value is a list of examples in that dataset
        dataset_name (str): The `dataset_name` parameter is a string that represents the name of the
            dataset. It is used to identify the dataset in the generated output file
        subset_name (str): The `subset_name` parameter is used to specify the name of the subset within the
            dataset. It helps in organizing and identifying different subsets within the dataset
        checkpoint_save_path (str, optional): The `checkpoint_save_path` parameter is the path where the generated
            dataset will be saved. It is a string that specifies the directory where the generated dataset file
            will be stored, defaults to "generated_dataset"
    """
    all_data = []

    # Load prompt
    prompt = DatasetTemplates(dataset_name, subset_name=subset_name)

    # Iterate to each prompt templates
    for prompt_id in tqdm(prompt.templates):
        template_name = prompt.templates[prompt_id].name

        for dataset_key in dataset.keys():
            for example in dataset[dataset_key]:
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

                all_data.append(
                    data_details
                )

    df_ = pd.DataFrame(all_data)
    df_.to_csv(f"{checkpoint_save_path}/{dataset_name}-{subset_name}.csv")


def run(dataset_name, subset_name):
    print('-- Generating')
    dset, dataset_name, subset_name = dataset_generator(dataset_name=dataset_name, subset_name=subset_name)

    generate_t2t_from_prompts(dset, dataset_name=dataset_name, subset_name=subset_name)
    print('-- Done!')



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset-name', help='Dataset name')
    parser.add_argument('--subset-name', help='Subset name')
    args = parser.parse_args()

    
    dataset_name = args.dataset_name
    subset_name = args.subset_name

    logger = set_logger()

    print('-- Generating')
    dset, dataset_name, subset_name = dataset_generator(dataset_name=dataset_name, subset_name=subset_name)

    generate_t2t_from_prompts(dset, dataset_name=dataset_name, subset_name=subset_name)
    print('-- Done!')
