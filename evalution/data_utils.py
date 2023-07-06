from nusacrowd import NusantaraConfigHelper
from nusacrowd.utils.constants import Tasks

TASK_LIST = [
    'tydiqa_id',
    'id_hsd_nofaaulia',
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
    'wrete',
    'korpus_nusantara_ind_jav',
    'korpus_nusantara_ind_sun',
    'korpus_nusantara_jav_ind',
    'korpus_nusantara_sun_ind',
    'xl_sum',
    'xpersona_id',
    'id_short_answer_grading',
    'stif_indonesia',
    'id_google_play_review',
    'id_stance',
    'indolem_ntp',
    'indo_law',
    'indotacos',
    'jadi_ide',
    'code_mixed_jv_id_jv',
    'id_google_play_review_posneg',
    'nusax_senti_ace',
    'nusax_senti_ban',
    'nusax_senti_bjn',
    'nusax_senti_bug',
    'nusax_senti_mad',
    'nusax_senti_nij',
]

def load_datasets():
    nc_conhelp = NusantaraConfigHelper()
    cfg_name_to_dset_map = {
        con.config.name: (con.load_dataset(), list(con.tasks)[0])
        for con in nc_conhelp.filtered(lambda x: x.config.name.replace(x.config.schema, '')[:-1] in task_list and 'nusantara_' in x.config.schema)
    } # {config_name: (datasets.Dataset, task_name)
    return cfg_name_to_dset_map