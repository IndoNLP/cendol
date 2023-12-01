from nusacrowd import NusantaraConfigHelper
from nusacrowd.utils.constants import Tasks
import pandas as pd
import datasets
from enum import Enum

NLU_TASK_LIST = [
    # 'indotacos',
    # 'indo_law',
    'id_hsd_nofaaulia',
    'wrete',
    'id_short_answer_grading',
    'id_google_play_review',
    'id_stance',
    'indolem_ntp',
    'id_google_play_review_posneg',
    'jadi_ide',
    'code_mixed_jv_id_jv',
    'nusax_senti_ace',
    'nusax_senti_ban',
    'nusax_senti_bjn',
    'nusax_senti_bug',
    'nusax_senti_mad',
    'nusax_senti_nij',    
]

NLU_TASK_LIST_EXTERNAL = [
    'MAPS',
    'haryoaw/COPAL',
    'MABL/id',
    'MABL/jv',
    'MABL/su',
    'IndoStoryCloze',
    'IndoMMLU',
    # 'MAPS/figurative',
    # 'MAPS/non_figurative',
]

NLG_TASK_LIST = [
    # 'korpus_nusantara_ind_xdy',
    # 'korpus_nusantara_ind_bug',
    # 'korpus_nusantara_ind_mad',
    # 'korpus_nusantara_ind_bjn',
    # 'korpus_nusantara_ind_tiociu',
    # 'korpus_nusantara_xdy_ind',
    # 'korpus_nusantara_bug_ind',
    # 'korpus_nusantara_mad_ind',
    # 'korpus_nusantara_bjn_ind',
    # 'korpus_nusantara_tiociu_ind',
    # 'korpus_nusantara_ind_jav',
    # 'korpus_nusantara_ind_sun',
    # 'korpus_nusantara_jav_ind',
    # 'korpus_nusantara_sun_ind',
    'xl_sum',
    'xpersona_id',
    'stif_indonesia',
    'tydiqa_id',
]

FLORES200_TASK_LIST = [
    'flores200-sun_Latn-ind_Latn',
    'flores200-jav_Latn-ind_Latn',
    'flores200-bug_Latn-ind_Latn',
    'flores200-ace_Latn-ind_Latn',
    'flores200-bjn_Latn-ind_Latn',
    'flores200-ban_Latn-ind_Latn',
    'flores200-min_Latn-ind_Latn',
    'flores200-ind_Latn-sun_Latn',
    'flores200-ind_Latn-jav_Latn',
    'flores200-ind_Latn-bug_Latn',
    'flores200-ind_Latn-ace_Latn',
    'flores200-ind_Latn-bjn_Latn',
    'flores200-ind_Latn-ban_Latn',
    'flores200-ind_Latn-min_Latn',
]

def load_nlu_datasets():
    nc_conhelp = NusantaraConfigHelper()
    cfg_name_to_dset_map = {
        con.config.name: (con.load_dataset(), list(con.tasks)[0])
        for con in nc_conhelp.filtered(lambda x: x.config.name.replace(x.config.schema, '')[:-1] in NLU_TASK_LIST and 'nusantara_' in x.config.schema)
    } # {config_name: (datasets.Dataset, task_name)
    
    return cfg_name_to_dset_map

def load_external_nlu_datasets(lang='ind'):
    cfg_name_to_dset_map = {} # {config_name: (datasets.Dataset, task_name)

    # hack, add new Task
    class NewTasks(Enum):
        COPA = "COPA"
        MABL = "MABL"
        MAPS = "MAPS"
        IndoStoryCloze = "IndoStoryCloze"
        IndoMMLU = "IndoMMLU"

    for task in NLU_TASK_LIST_EXTERNAL:
        if 'COPAL' in task:
            dset = datasets.load_dataset(task)
            cfg_name_to_dset_map[task] = (dset, NewTasks.COPA)
        elif 'MABL' in task:
            mabl_path = './mabl_data'
            subset = task.split('/')[-1]
            
            df = pd.read_csv(f'{mabl_path}/{subset}.csv')
            dset = datasets.Dataset.from_pandas(
                df.rename({'startphrase': 'premise', 'ending1': 'choice1', 'ending2': 'choice2', 'labels': 'label'}, axis='columns')
            )
            cfg_name_to_dset_map[task] = (datasets.DatasetDict({'test': dset}), NewTasks.MABL)
        elif 'MAPS' in task:
            maps_path = './maps_data'
            df = pd.read_excel(f'{maps_path}/test_proverbs.xlsx')
            
            # Split by subset
            if '/' in task:
                subset = task.split('/')[-1]
                if subset =='figurative':
                    df = df.loc[df['is_figurative'] == 1,:]
                else: # non_figurative
                    df = df.loc[df['is_figurative'] == 0,:]

            dset = datasets.Dataset.from_pandas(
                df.rename({
                    'proverb': 'premise', 'conversation': 'context', 
                    'answer1': 'choice1', 'answer2': 'choice2', 'answer_key': 'label'
                }, axis='columns')
            )
            cfg_name_to_dset_map[task] = (datasets.DatasetDict({'test': dset}), NewTasks.MAPS)
        elif 'IndoStoryCloze' in task:
            df = datasets.load_dataset('indolem/indo_story_cloze')['test'].to_pandas()
            
            # Preprocess
            df['premise'] = df.apply(lambda x: '. '.join([
                x['sentence-1'], x['sentence-2'], x['sentence-3'], x['sentence-4']
            ]), axis='columns')
            df = df.rename({'correct_ending': 'choice1', 'incorrect_ending': 'choice2'}, axis='columns')
            df = df[['premise', 'choice1', 'choice2']]
            df['label'] = 0
            
            dset = datasets.Dataset.from_pandas(df)
            cfg_name_to_dset_map[task] = (datasets.DatasetDict({'test': dset}), NewTasks.IndoStoryCloze)
        elif 'IndoMMLU' in task:
            df = pd.read_csv('indommlu_data/IndoMMLU.csv')
            dset = datasets.Dataset.from_pandas(df.rename({'kunci': 'label'}, axis='columns'))
            cfg_name_to_dset_map[task] = (datasets.DatasetDict({'test': dset}), NewTasks.IndoMMLU)
    return cfg_name_to_dset_map

def load_nlg_datasets():
    nc_conhelp = NusantaraConfigHelper()
    cfg_name_to_dset_map = {
        con.config.name: (con.load_dataset(), list(con.tasks)[0])
        for con in nc_conhelp.filtered(lambda x: x.config.name.replace(x.config.schema, '')[:-1] in NLG_TASK_LIST and 'nusantara_' in x.config.schema)
    } # {config_name: (datasets.Dataset, task_name)
    return cfg_name_to_dset_map

def load_flores_datasets():
    dset_map = {}
    for task in FLORES200_TASK_LIST:
        subset = task.replace('flores200-', '')
        src_lang, tgt_lang = subset.split('-')
        dset = datasets.load_dataset('facebook/flores', subset)
        dset = dset.rename_columns({f'sentence_{src_lang}': 'text_1', f'sentence_{tgt_lang}': 'text_2'}).select_columns(['id', 'text_1', 'text_2'])
        dset_map[task] = (dset, Tasks.MACHINE_TRANSLATION)
    return dset_map
