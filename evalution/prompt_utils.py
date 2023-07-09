TASK_TO_PROMPT = {
    'eng': {
        # Tasks.SENTIMENT_ANALYSIS
        'SA': [
            'Classify the sentiment of the text below.\n[INPUT] => Emotion: [LABELS_CHOICE]',
            'Predict the sentiment of the following text.\nText: [INPUT] => Emotion: [LABELS_CHOICE]',
            '[INPUT]\nWhat would be the sentiment of the text above? [LABELS_CHOICE]',
            'What is the sentiment of this text?\nText: [INPUT]\nAnswer: [LABELS_CHOICE]',
            'Text: [INPUT]\nPlease classify the sentiment of above text. Emotion: [LABELS_CHOICE]',
        ],
        # Tasks.SHORT_ANSWER_GRADING
        'SAG': [
            'Classify the grade of the test answer below.\n[INPUT] => Emotion: [LABELS_CHOICE]',
            'Predict the grade of the following test answer.\nINPUT] => Emotion: [LABELS_CHOICE]',
            '[INPUT]\nWhat would be the grade of the test answer above? [LABELS_CHOICE]',
            'What is the grade of this test answer?\[INPUT]\nAnswer: [LABELS_CHOICE]',
            'Text: [INPUT]\nPlease classify the grade of above test answer. Emotion: [LABELS_CHOICE]',
        ],
        # Tasks.EMOTION_CLASSIFICATION
        'EC': [
            'Classify the emotion of the text below.\n[INPUT] => Emotion: [LABELS_CHOICE]',
            'Predict the emotion of the following text.\nText: [INPUT] => Emotion: [LABELS_CHOICE]',
            '[INPUT]\nWhat would be the emotion of the text above? [LABELS_CHOICE]',
            'What is the emotion of this text?\nText: [INPUT]\nAnswer: [LABELS_CHOICE]',
            'Text: [INPUT]\nPlease classify the emotion of above text. Emotion: [LABELS_CHOICE]',
        ],
        # Tasks.LEGAL_CLASSIFICATION
        'LC':  [
            'Classify the verdict of the legal statement below.\n[INPUT] => Topic: [LABELS_CHOICE]',
            'Predict the verdict of the following legal statement.\nText: [INPUT] => Topic: [LABELS_CHOICE]',
            '[INPUT]\nWhat would be the verdict of the legal statement above? [LABELS_CHOICE]',
            'What is the verdict of this legal statement?\nText: [INPUT]\nAnswer: [LABELS_CHOICE]',
            'Text: [INPUT]\nPlease classify the verdict of above legal statement. Topic: [LABELS_CHOICE]',
        ],
        # Tasks.TEXTUAL_ENTAILMENT
        'TE': [
            '[INPUT_A]\nBased on the previous passage, is it true that "[INPUT_B]"? Yes, no, or maybe? [OPTIONS]? [LABELS_CHOICE]',
            '[INPUT_A]\n\nQuestion: Does this imply that "[INPUT_B]"? Yes, no, or maybe? [LABELS_CHOICE]',
            'Given that [INPUT_A]. Does it follow that [INPUT_B]? Yes, no, or maybe? [LABELS_CHOICE]',
        ],
        # Tasks.NEXT_SENTENCE_PREDICTION
        'NSP': [
            'Given two tweets\nA: [INPUT_A]\nB: [INPUT_B]\n\nIs tweet B is a continuation of tweet A? [OPTIONS]? [LABELS_CHOICE]',
            'Is tweet "[INPUT_B]" a continuation of tweet "[INPUT_A]"? [LABELS_CHOICE]',
            'First Tweet: [INPUT_A].\nWould "[INPUT_B]" a continuation of the first tweet? [LABELS_CHOICE]',
        ],

        # Tasks.MACHINE_TRANSLATION
        'MT': [
            'Translate the following text from [SOURCE] to [TARGET].\nText: [INPUT]\nTranslation:',
            '[INPUT]\nTranslate the text above from [SOURCE] to [TARGET].',
            'Text in [SOURCE]: [INPUT]\nHow would you translate that in [TARGET]?',
            'Translate the following [SOURCE] text from to [TARGET].\nText: [INPUT]\nTranslation:',
            'Text in [SOURCE]: [INPUT]\nText in [TARGET]:',
        ],
        # Tasks.PARAPHRASING
        'PARA': [
            'Translate the following text from [SOURCE] to [TARGET].\nText: [INPUT]\nTranslation:',
            '[INPUT]\nTranslate the text above from [SOURCE] to [TARGET].',
            'Text in [SOURCE]: [INPUT]\nHow would you translate that in [TARGET]?',
            'Translate the following [SOURCE] text from to [TARGET].\nText: [INPUT]\nTranslation:',
            'Text in [SOURCE]: [INPUT]\nText in [TARGET]:',
        ],
        # Tasks.QUESTION_ANSWERING
        'QA': [
            'Translate the following text from [SOURCE] to [TARGET].\nText: [INPUT]\nTranslation:',
            '[INPUT]\nTranslate the text above from [SOURCE] to [TARGET].',
            'Text in [SOURCE]: [INPUT]\nHow would you translate that in [TARGET]?',
            'Translate the following [SOURCE] text from to [TARGET].\nText: [INPUT]\nTranslation:',
            'Text in [SOURCE]: [INPUT]\nText in [TARGET]:',
        ],
        # Tasks.SUMMARIZATION
        'SUM': [
            'Translate the following text from [SOURCE] to [TARGET].\nText: [INPUT]\nTranslation:',
            '[INPUT]\nTranslate the text above from [SOURCE] to [TARGET].',
            'Text in [SOURCE]: [INPUT]\nHow would you translate that in [TARGET]?',
            'Translate the following [SOURCE] text from to [TARGET].\nText: [INPUT]\nTranslation:',
            'Text in [SOURCE]: [INPUT]\nText in [TARGET]:',
        ]
    },
    'ind': {
        # Tasks.SENTIMENT_ANALYSIS
        'SA': [
            'Classify the sentiment of the text below.\n[INPUT] => Emotion: [LABELS_CHOICE]',
            'Predict the sentiment of the following text.\nText: [INPUT] => Emotion: [LABELS_CHOICE]',
            '[INPUT]\nWhat would be the sentiment of the text above? [LABELS_CHOICE]',
            'What is the sentiment of this text?\nText: [INPUT]\nAnswer: [LABELS_CHOICE]',
            'Text: [INPUT]\nPlease classify the sentiment of above text. Emotion: [LABELS_CHOICE]',
        ],
        # Tasks.SHORT_ANSWER_GRADING
        'SAG': [
            'Classify the grade of the test answer below.\n[INPUT] => Emotion: [LABELS_CHOICE]',
            'Predict the grade of the following test answer.\nINPUT] => Emotion: [LABELS_CHOICE]',
            '[INPUT]\nWhat would be the grade of the test answer above? [LABELS_CHOICE]',
            'What is the grade of this test answer?\[INPUT]\nAnswer: [LABELS_CHOICE]',
            'Text: [INPUT]\nPlease classify the grade of above test answer. Emotion: [LABELS_CHOICE]',
        ],
        # Tasks.EMOTION_CLASSIFICATION
        'EC': [
            'Classify the emotion of the text below.\n[INPUT] => Emotion: [LABELS_CHOICE]',
            'Predict the emotion of the following text.\nText: [INPUT] => Emotion: [LABELS_CHOICE]',
            '[INPUT]\nWhat would be the emotion of the text above? [LABELS_CHOICE]',
            'What is the emotion of this text?\nText: [INPUT]\nAnswer: [LABELS_CHOICE]',
            'Text: [INPUT]\nPlease classify the emotion of above text. Emotion: [LABELS_CHOICE]',
        ],
        # Tasks.LEGAL_CLASSIFICATION
        'LC':  [
            'Classify the verdict of the legal statement below.\n[INPUT] => Topic: [LABELS_CHOICE]',
            'Predict the verdict of the following legal statement.\nText: [INPUT] => Topic: [LABELS_CHOICE]',
            '[INPUT]\nWhat would be the verdict of the legal statement above? [LABELS_CHOICE]',
            'What is the verdict of this legal statement?\nText: [INPUT]\nAnswer: [LABELS_CHOICE]',
            'Text: [INPUT]\nPlease classify the verdict of above legal statement. Topic: [LABELS_CHOICE]',
        ],
        # Tasks.TEXTUAL_ENTAILMENT
        'TE': [
            '[INPUT_A]\nBased on the previous passage, is it true that "[INPUT_B]"? Yes, no, or maybe? [OPTIONS]? [LABELS_CHOICE]',
            '[INPUT_A]\n\nQuestion: Does this imply that "[INPUT_B]"? Yes, no, or maybe? [LABELS_CHOICE]',
            'Given that [INPUT_A]. Does it follow that [INPUT_B]? Yes, no, or maybe? [LABELS_CHOICE]',
        ],
        # Tasks.NEXT_SENTENCE_PREDICTION
        'NSP': [
            'Given two tweets\nA: [INPUT_A]\nB: [INPUT_B]\n\nIs tweet B is a continuation of tweet A? [OPTIONS]? [LABELS_CHOICE]',
            'Is tweet "[INPUT_B]" a continuation of tweet "[INPUT_A]"? [LABELS_CHOICE]',
            'First Tweet: [INPUT_A].\nWould "[INPUT_B]" a continuation of the first tweet? [LABELS_CHOICE]',
        ],

        # Tasks.MACHINE_TRANSLATION
        'MT': [
            'Translate the following text from [SOURCE] to [TARGET].\nText: [INPUT]\nTranslation:',
            '[INPUT]\nTranslate the text above from [SOURCE] to [TARGET].',
            'Text in [SOURCE]: [INPUT]\nHow would you translate that in [TARGET]?',
            'Translate the following [SOURCE] text from to [TARGET].\nText: [INPUT]\nTranslation:',
            'Text in [SOURCE]: [INPUT]\nText in [TARGET]:',
        ],
        # Tasks.PARAPHRASING
        'PARA': [
            'Translate the following text from [SOURCE] to [TARGET].\nText: [INPUT]\nTranslation:',
            '[INPUT]\nTranslate the text above from [SOURCE] to [TARGET].',
            'Text in [SOURCE]: [INPUT]\nHow would you translate that in [TARGET]?',
            'Translate the following [SOURCE] text from to [TARGET].\nText: [INPUT]\nTranslation:',
            'Text in [SOURCE]: [INPUT]\nText in [TARGET]:',
        ],
        # Tasks.QUESTION_ANSWERING
        'QA': [
            'Translate the following text from [SOURCE] to [TARGET].\nText: [INPUT]\nTranslation:',
            '[INPUT]\nTranslate the text above from [SOURCE] to [TARGET].',
            'Text in [SOURCE]: [INPUT]\nHow would you translate that in [TARGET]?',
            'Translate the following [SOURCE] text from to [TARGET].\nText: [INPUT]\nTranslation:',
            'Text in [SOURCE]: [INPUT]\nText in [TARGET]:',
        ],
        # Tasks.SUMMARIZATION
        'SUM': [
            'Translate the following text from [SOURCE] to [TARGET].\nText: [INPUT]\nTranslation:',
            '[INPUT]\nTranslate the text above from [SOURCE] to [TARGET].',
            'Text in [SOURCE]: [INPUT]\nHow would you translate that in [TARGET]?',
            'Translate the following [SOURCE] text from to [TARGET].\nText: [INPUT]\nTranslation:',
            'Text in [SOURCE]: [INPUT]\nText in [TARGET]:',
        ]
    }
}

LABEL_LANG_MAP ={
	'code_mixed_jv_id_jv_nusantara_text': {
		'eng': {'-1': 'negative', '0': 'neutral', '1': 'positive'},
		'ind': {'-1': 'negatif', '0': 'netral', '1': 'positif'}
	},
	'id_google_play_review_nusantara_text': {
		'eng': {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5'},
		'ind': {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5'}
	},
	'id_google_play_review_posneg_nusantara_text': {
		'eng': {'pos': 'positive', 'neg': 'negative'},
		'ind': {'pos': 'positif', 'neg': 'negative'}
	},
	'id_hsd_nofaaulia_nusantara_text': {
		'eng': {'0': 'no', '1': 'yes'},
		'ind': {'0': 'no', '1': 'yes'}
	},
	'id_short_answer_grading_nusantara_pairs_score': {
		'eng': {1: '1', 2: '2', 3: '3', 4: '4', 5: '5'},
		'ind': {1: '1', 2: '2', 3: '3', 4: '4', 5: '5'}
	},
	'id_stance_nusantara_pairs': {
		'eng': {'for': 'entail', 'against': 'contradict', 'no': 'irrelevant'},
		'ind': {'for': 'sesuai', 'against': 'berlawanan', 'no': 'tidak berkaitan'}
	},
	'indo_law_nusantara_text': {
		'eng': {'pidana-khusus': 'special crime', 'pidana-umum': 'ordinary crime'},
		'ind': {'pidana-khusus': 'pidana khusus', 'pidana-umum': 'pidana umum'}
	},
	'indolem_ntp_nusantara_pairs': {
		'eng': {0: 'no', 1: 'yes'},
		'ind': {0: 'no', 1: 'yes'}
	},
	'jadi_ide_nusantara_text': {
		'eng': {'Jawa Timur': 'East Javanese', 'Jawa Standar': 'Standard Javanese', 'Jawa Ngapak': 'Ngapak Javanese'},
		'ind': {'Jawa Timur': 'Jawa Timur', 'Jawa Standar': 'Jawa Standar', 'Jawa Ngapak': 'Jawa Ngapak'}
	},
	'nusax_senti_ace_nusantara_text': {
		'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
		'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'}
	},
	'nusax_senti_ban_nusantara_text': {
		'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
		'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'}
	},
	'nusax_senti_bjn_nusantara_text': {
		'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
		'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'}
	},
	'nusax_senti_bug_nusantara_text': {
		'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
		'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'}
	},
	'nusax_senti_mad_nusantara_text': {
		'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
		'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'}
	},
	'nusax_senti_nij_nusantara_text': {
		'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
		'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'}
	},
	'wrete_nusantara_pairs': {
		'eng': {'NotEntail': 'not entail', 'Entail_or_Paraphrase': 'entail'},
		'ind': {'NotEntail': 'tidak sesuai', 'Entail_or_Paraphrase': 'sesuai'}
	}
}

def get_nlu_label(dset_subset, prompt_lang):
    return LABEL_LANG_MAP[dset_subset][prompt_lang]

def get_prompt(prompt_lang):
    prompt_templates = {}
    for config, prompts in TASK_TO_PROMPT[prompt_lang].items():
        prompt_templates[config] = prompts
    return prompt_templates
