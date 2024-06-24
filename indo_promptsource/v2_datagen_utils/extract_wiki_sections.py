'''
Script on Generating Title-Subsections-Text Wikipedia Data to make short-context responses
'''

#core functionality modules
import os
import logging
import warnings
import argparse

from tqdm import tqdm

#text preprocess modules
import re

#dataset related modules
import numpy as np
import pandas as pd


### MODULES DEFINITION ###
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


class RuleBasedWikiContent(object):
    def __init__(self):
        self._is_df_wiki_present = False

    @staticmethod
    def __validate_df_wiki_input_schema(df_to_check: pd.DataFrame):
        col_schema_assert = ["title", "text"]
        if len(set(col_schema_assert).difference(df_to_check.columns.to_list())) > 0:
            raise AssertionError("Schema of DF doesn't match! Only expects a DF with colnames 'title' and 'text'!")

        for col in col_schema_assert:
            df_to_check[col] = df_to_check[col].astype("str")

        return df_to_check

    @staticmethod
    def __validate_df_wiki_output_schema(df_to_check: pd.DataFrame):
        col_schema_assert = ["type", "text", "len"]
        if len(set(df_to_check.columns.to_list()).difference(col_schema_assert)) > 0 or len(set(col_schema_assert).difference(df_to_check.columns.to_list())) > 0:
            raise AssertionError("Schema of DF doesn't match! Only expects a DF with colnames 'title' and 'text'!")

        for col in col_schema_assert:
            df_to_check[col] = df_to_check[col].astype("str")

        return df_to_check

    def instantiate_df_wiki(self, df_wiki_input: pd.DataFrame):
        if not isinstance(df_wiki_input, pd.DataFrame):
            raise ValueError("The dataframe hasn't been instantiated via `instantiate_df_wiki` nor passed as argument!")
        elif self._is_df_wiki_present:
            warnings.warn("The class has been instantiated with DF! Recall this fn will override existing DF!")

        self.df = self.__validate_df_wiki_input_schema(df_wiki_input)
        self._is_df_wiki_present = True


    @staticmethod
    def wiki_paragraph_rulebased_recognition(title:str, text:str):

        # instantiate output variable first
        # wiki info data first value is its article title
        wiki_info_data = [{
            "text": title,
            "type": "Title"
        }]
        wiki_related_data = []


        parts = [p.strip() for p in text.split("\n") if p.strip() != ""]

        is_header_or_external_reference = True
        is_external_data = False

        external_reference_re = "|".join([f"((^|\s){data}(\s|$))" for data in external_reference])

        for idx, part in enumerate(parts, start=1):

            n_words = len(part.split())

            # header
            if n_words<=threshold_header:
                # detect for external data first by regex or previous values is external_data
                # assumption: any linedata that is not exceeds threshold_content, will
                # be assumed as external data until a "content" is found
                if (is_external_data) or (bool(re.search(external_reference_re,part, flags=re.I))):
                    is_external_data = True
                    #dumped to 2nd list of external/related data
                    wiki_related_data.append({
                        "paragraph_pos": idx,
                        "text": part
                    })

                # detect for previous values is header (consecutive short-len line-delim text)
                # header should not appear on multiline, hence will be marked as "Undecided-Continued Header"
                elif is_header_or_external_reference:
                    wiki_info_data.append({
                        "text": part,
                        "type": "Undecided-Continued Header"
                    })

                #if previous data isn't a header, will assign it to header-type
                else:
                    wiki_info_data.append({
                        "text": part,
                        "type": "Header"
                    })

                # mark the current line data as header (or external link)
                # (will be used to check next data)
                is_header_or_external_reference = True

                continue

            # if the prev data is header or external data and has sufficient len, will be marked as content
            elif (is_header_or_external_reference)&(n_words>=threshold_content):

                # reset the mark of header and external_data (hence making it as content-type data)
                is_header_or_external_reference = False
                is_external_data = False

                wiki_info_data.append({
                    "text": part,
                    "type": "Content"
                })
                continue

            # this section belongs to text with one of following criterias:
            # 1. which its previous value not a header or external_data (is_header_or_external_reference is False) -- possibility of multiline content
            # 2. Its length isn't sufficient to be assumed directly as content data
            #    but is too-long for rule-based to say this as header (escaped the first if statement)

            # if external_data isn't active (prev value is a content) and passed max threshold for a header
            # it will be marked as "Undecided-Continued Text" -- possible multiline content
            elif not(is_external_data):
                wiki_info_data.append({
                    "text": part,
                    "type": "Undecided-Continued Text"
                })

            # this will keep gray-area with external_data as active to be marked as external_data
            else:
                #dumped to 2nd list of external/related data
                wiki_related_data.append({
                    "paragraph_pos": idx,
                    "text": part
                })

        if len(wiki_info_data) >= 0:
            wiki_df = pd.DataFrame(wiki_info_data)
        else:
            raise AssertionError("No Data can be extracted!")
        wiki_df["len"] = wiki_df["text"].apply(lambda x: len(x.split()))
        

        if len(wiki_related_data) > 0:
            wiki_related_df = pd.DataFrame(wiki_related_data)
            wiki_related_df["len"] = wiki_related_df["text"].apply(lambda x: len(x.split()))
        else:
            wiki_related_df = pd.DataFrame()

        return wiki_df, wiki_related_df


    @staticmethod
    def __subsection_fn_result_wrapper(*args, mode: str="wiki_only_data"):
        if mode not in ["wiki_only_data", "appendix_only_data", "concat"]:
            raise ValueError(f"`Mode` value isn't expected! Only receive 'wiki_only_data', 'appendix_only_data', or 'concat', got {mode}!")

        (_wiki_df, _wiki_related_df, *_) = args

        if mode == "wiki_only_data":
            return _wiki_df

        elif mode == "appendix_only_data":
            return _wiki_related_df

        elif mode == "concat":
            _wiki_df["identifier"] = "wiki data"
            _wiki_related_df["identifier"] = "appendix data"

            return pd.concat([_wiki_df, _wiki_related_df], axis=0, ignore_index=True)

    @classmethod
    def post_process_wiki_extracted_data(cls, article_title: str, df_wiki_subtitle_extr: pd.DataFrame):
        output_df = []
        text = ""
        header_title = ""
        df_wiki_subtitle_extr = cls.__validate_df_wiki_output_schema(df_wiki_subtitle_extr)

        for idx, data in df_wiki_subtitle_extr.iterrows():

            # assign value 'title' with data of "Header" and "Title"
            if data["type"] in ("Header", "Title"):
                _is_header = True

                # append this to output_df as long as its not a first row value
                # or unexpected title/header in last row value (this case should be skipped)
                if idx not in (df_wiki_subtitle_extr.index[0], df_wiki_subtitle_extr.index[df_wiki_subtitle_extr.shape[0]-1]):
                    output_df.append({
                        "article_title": article_title,
                        "header_title": header_title,
                        "text": text
                    })

                #assign title and reset text
                header_title = data["text"]
                text = ""

            # skip data that has "Undecided-Continued Header"
            elif data["type"] == "Undecided-Continued Header":
                continue

            # check values for "Content" and "Undecided-Continued Text"
            elif data["type"] in ("Content", "Undecided-Continued Text"):
                # append this data for now as content-type in var text
                # supposedly should be treated different since its not enough to be 
                # a content type (one possibility is a list-down)
                if _is_header and data["type"] == "Undecided-Continued Text":
                    text = data["text"]
                    _is_header = False

                # set this data as content in var text                
                elif _is_header and data["type"] == "Content":
                    text = data["text"]
                    _is_header = False

                #prev data is a content-type
                else:
                    text = text + "\n\n" + data["text"]
                
                if idx == df_wiki_subtitle_extr.index[df_wiki_subtitle_extr.shape[0]-1]:
                    output_df.append({
                        "article_title": article_title,
                        "header_title": header_title,
                        "text": text
                    })

        return pd.DataFrame(output_df)

    #to be added: `post_process_wiki_extracted_external_data` method (for post-process references)

    @classmethod
    def wiki_paragraph_rulebased_recognition_partial(cls, title:str, text:str, mode: str="wiki_only_data"):
        if mode not in ["wiki_only_data", "appendix_only_data"]:
            raise ValueError(f"`Mode` value isn't expected! Only receive 'wiki_only_data' or 'appendix_only_data', got {mode}!")

        return cls.__subsection_fn_result_wrapper(*cls.wiki_paragraph_rulebased_recognition(title=title, text=text), mode=mode)


    def __call__(self, df_wiki_input:pd.DataFrame=None, is_postprocess: bool=True):
        if (not self._is_df_wiki_present) and (not isinstance(df_wiki_input, pd.DataFrame)):
            #value isn't provided
            raise ValueError("The dataframe hasn't been instantiated via `instantiate_df_wiki` nor passed as argument!")

        if not isinstance(is_postprocess, bool):
            raise ValueError(f"Wrong type of `is_postprocess` arg! Expected `bool`, received {type(is_postprocess)}!")

        elif isinstance(df_wiki_input, pd.DataFrame):
            #warnings if  isn't provided
            if self._is_df_wiki_present:
                warnings.warn("Method `extract_all_subsections` received external `df` variable while internal DF has been defined! Will use args provided externally instead of its internal value!")
            _df_to_be_extracted = self.__validate_df_wiki_input_schema(df)
        
        elif not isinstance(df_wiki_input, pd.DataFrame):
            _df_to_be_extracted = self.df

        df_subsections = []
        for _, wiki_article_data in tqdm(_df_to_be_extracted.iterrows(), desc="Extracting Wiki Subsections", total=_df_to_be_extracted.shape[0]):

            _df_wiki = self.wiki_paragraph_rulebased_recognition_partial(title = wiki_article_data["title"], text = wiki_article_data["text"])

            if not is_postprocess:
                _df_wiki["title"] = wiki_article_data["title"]
            else:
                _df_wiki = self.post_process_wiki_extracted_data(wiki_article_data["title"], _df_wiki)

            df_subsections.append(_df_wiki)

        return pd.concat(df_subsections, ignore_index=True)


### MAIN CODE ###
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--raw-csv-path", help="Relative dir path of csv file containing raw Wikipedia data")
    parser.add_argument("--save-dir-path", help="""Relative dir path of saved Wikipedia CSV data
                        to the `extract_wiki_sections.py` script dir""",
            default=os.path.dirname(os.path.abspath(__file__)))
    parser.add_argument("--save-file-name", help="""Filename of saved Wikipedia CSV data
                        to the `extract_wiki_sections.py` script dir""")
    parser.add_argument("--threshold-header", help="Max number of words to consider it as header (subsection) text",
            default=4, type=int)
    parser.add_argument("--threshold-content", help="Min number of words to consider it as content text",
            default=20, type=int)

    args = parser.parse_args()

    ## CONFIG
    threshold_header = args.threshold_header
    threshold_content = args.threshold_content
    save_folder_path = args.save_dir_path
    filename = args.save_file_name

    #for catching external references
    external_reference = ["referensi", "catatan kaki", "pranala luar"]

    ## LOAD THE DATA
    df = pd.read_csv(args.raw_csv_path)

    ## RUN THE EXTRACTION
    df_res = RuleBasedWikiContent()(df_wiki_input=df, is_postprocess=True)
    df_res["text_first_paragraph"] = df_res["text"].apply(lambda x: x.split("\n\n")[0])

    df_res.to_csv(f"{save_folder_path}/{filename}.csv", index=False)


# args used for data generation
# --raw_csv_path {path}/wiki_id_20230901_dataset_soft_hard_cleansed.csv
# --threshold_header 4
# --threshold_content 20
# --save_dir_path .
