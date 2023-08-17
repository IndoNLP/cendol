from tqdm import tqdm
import pandas as pd
from promptsource.templates import DatasetTemplates
from nusacrowd import NusantaraConfigHelper
import logging
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dataset-name', help='Dataset name')
parser.add_argument('--subset-name', help='Subset name')
parser.add_argument('--output-dir', help='output-dir')
args = parser.parse_args()

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

conhelps = NusantaraConfigHelper()

all_data = []
checkpoint_save_path = args.output_dir

dataset_name = args.dataset_name
subset_name = args.subset_name
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


# Load prompt
prompt = DatasetTemplates(dataset_name, subset_name=subset_name)

# Iterate to each prompt templates
for prompt_id in tqdm(prompt.templates):
    all_data = None
    all_data = []
    template_name = prompt.templates[prompt_id].name

    for dataset_key in dset.keys():
        logger.info(f"Generating prompt_id:{prompt_id} dataset_key:{dataset_key}")
        example_list = dset[dataset_key]
        for i in tqdm(range(len(example_list))):
            example = example_list[i]
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
    df_.to_csv(f"{checkpoint_save_path}/{dataset_name}-{subset_name}-{prompt_id}.csv")