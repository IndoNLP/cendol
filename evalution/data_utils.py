from nusacrowd import NusantaraConfigHelper
from nusacrowd.utils.constants import Tasks

NLU_TASK_LIST = [
    # 'indotacos',
    'id_hsd_nofaaulia',
    'wrete',
    'id_short_answer_grading',
    'id_google_play_review',
    'id_stance',
    'indolem_ntp',
    'indo_law',
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

def load_nlu_datasets():
    nc_conhelp = NusantaraConfigHelper()
    cfg_name_to_dset_map = {
        con.config.name: (con.load_dataset(), list(con.tasks)[0])
        for con in nc_conhelp.filtered(lambda x: x.config.name.replace(x.config.schema, '')[:-1] in NLU_TASK_LIST and 'nusantara_' in x.config.schema)
    } # {config_name: (datasets.Dataset, task_name)
    return cfg_name_to_dset_map


def load_nlg_datasets():
    nc_conhelp = NusantaraConfigHelper()
    cfg_name_to_dset_map = {
        con.config.name: (con.load_dataset(), list(con.tasks)[0])
        for con in nc_conhelp.filtered(lambda x: x.config.name.replace(x.config.schema, '')[:-1] in NLG_TASK_LIST and 'nusantara_' in x.config.schema)
    } # {config_name: (datasets.Dataset, task_name)
    return cfg_name_to_dset_map