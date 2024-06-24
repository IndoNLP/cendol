'''
Script on Generating Wikipedia Data that are dumped into https://dumps.wikimedia.org/
More info can be read on https://huggingface.co/datasets/wikipedia
-------------------
Check here to see available indexed data: https://dumps.wikimedia.org/backup-index.html
Also check here to see language meta from its code: https://meta.wikimedia.org/wiki/List_of_Wikipedias
'''

import os
import logging
import argparse

import pandas as pd
from datasets import load_dataset


def set_logger():
    # Set up the logger
    logging.basicConfig(
        level=logging.INFO,  # Set the desired logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format='%(asctime)s [%(levelname)s]: %(message)s',  # Customize the log message format
        datefmt='%Y-%m-%d %H:%M:%S'  # Customize the date/time format
    )

    # Create a file handler to write logs into a file
    file_handler = logging.FileHandler('app.log')

    # Set the log level for the file handler
    file_handler.setLevel(logging.INFO) 

    # Create a formatter for the file handler (customize the log format for the file)
    file_formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(file_formatter)

    logger = logging.getLogger("Wiki Dataset Generation")
    logger.addHandler(file_handler)

    return logger


#only executed if called directly
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--lang-id", help="Lang ID from Wikipedia Data to extract")
    parser.add_argument("--date-ver", help="Date of Wikipedia Data (YYYYMMDD) generation to extract")
    parser.add_argument("--save-dir-path", help="""Relative dir path of saved Wikipedia CSV data
                        to the `extract_raw_wiki_data.py` script dir""",
            default=os.path.dirname(os.path.abspath(__file__)))

    args = parser.parse_args()


    dset_name = "wikipedia"

    logger = set_logger()
    logger.info("Parsing arguments...")

    lang_id = args.lang_id
    date_ver = args.date_ver
    save_dir = args.save_dir_path

    logger.info("Loading the dataset from Wikipedia...")
    df = load_dataset(dset_name, language=lang_id, date=date_ver, beam_runner='DirectRunner', split="train").to_pandas()
    logger.info("Loading done!")
    logger.info(f"#Data collected: {df.shape[0]}")
    logger.info("Saving dataset raw form...")
    df.to_csv(f"{save_dir}/wiki_{lang_id}_{date_ver}_raw_dataset.csv", index=False)
