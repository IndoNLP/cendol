from nusacrowd import NusantaraConfigHelper
from nusacrowd.utils.constants import Tasks
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
    'haryoaw/COPAL',
]

NLG_TASK_LIST = [
    'korpus_nusantara_ind_xdy',
    'korpus_nusantara_ind_bug',
    'korpus_nusantara_ind_mad',
    'korpus_nusantara_ind_bjn',
    'korpus_nusantara_ind_tiociu',
    'korpus_nusantara_xdy_ind',
    'korpus_nusantara_bug_ind',
    'korpus_nusantara_mad_ind',
    'korpus_nusantara_bjn_ind',
    'korpus_nusantara_tiociu_ind',
    'korpus_nusantara_ind_jav',
    'korpus_nusantara_ind_sun',
    'korpus_nusantara_jav_ind',
    'korpus_nusantara_sun_ind',
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

    # hack, add new Task
    class NewTasks(Enum):
        COPA = "COPA"

   
    for task in NLU_TASK_LIST_EXTERNAL:
        dset = datasets.load_dataset(task)
        cfg_name_to_dset_map[task] = (dset, NewTasks.COPA)
    print(cfg_name_to_dset_map)
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