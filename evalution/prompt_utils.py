TASK_TO_PROMPT = {
    'eng': {
        # Tasks.SENTIMENT_ANALYSIS
        'SA': [
            'Classify the sentiment of the text below.\n[INPUT] => Sentiment: [LABELS_CHOICE]',
            'Predict the sentiment of the following text.\nText: [INPUT] => [LABELS_CHOICE]',
            '[INPUT]\nWhat would be the sentiment of the text above? [LABELS_CHOICE]',
            'What is the sentiment of this text?\nText: [INPUT]\nSentiment: [LABELS_CHOICE]',
            'Text: [INPUT]\nPlease classify the sentiment of above text. Sentiment: [LABELS_CHOICE]',
        ],
        # Tasks.SHORT_ANSWER_GRADING
        'SAG': [
            'Estimate the grade of the test answer below.\n[INPUT] => Grade: [LABELS_CHOICE]',
            'Predict the grade of the following test answer.\n[INPUT] => [LABELS_CHOICE]',
            '[INPUT]\nWhat would be the grade of the test answer above? [LABELS_CHOICE]',
            'What is the grade of this test answer?\[INPUT]\nAnswer: [LABELS_CHOICE]',
            'Text: [INPUT]\nPlease estimate the grade of above test answer. Grade: [LABELS_CHOICE]',
        ],
        # Tasks.EMOTION_CLASSIFICATION
        'EC': [
            'Classify the emotion of the text below.\n[INPUT] => Emotion: [LABELS_CHOICE]',
            'Predict the emotion of the following text.\nText: [INPUT] => [LABELS_CHOICE]',
            '[INPUT]\nWhat would be the emotion of the text above? [LABELS_CHOICE]',
            'What is the emotion of this text?\nText: [INPUT]\nAnswer: [LABELS_CHOICE]',
            'Text: [INPUT]\nPlease classify the emotion of above text. Emotion: [LABELS_CHOICE]',
        ],
        # Tasks.LEGAL_CLASSIFICATION
        'LC':  [
            'Classify the verdict of the legal statement below.\n[INPUT] => Verdict: [LABELS_CHOICE]',
            'Predict the verdict of the following legal statement.\n[INPUT] => [LABELS_CHOICE]',
            '[INPUT]\nWhat would be the verdict of the legal statement above? [LABELS_CHOICE]',
            'What is the verdict of the following legal statement?\n[INPUT]\nVerdict: [LABELS_CHOICE]',
            '[INPUT]\nPlease classify the verdict of above legal statement. Verdict: [LABELS_CHOICE]',
        ],
        # Tasks.TEXTUAL_ENTAILMENT
        'TE': [
            'Hypothesis: [INPUT_A]\nPremise: [INPUT_B]\nQuestion: What is the relation between the hypothesis and the premise? [LABELS_CHOICE]',
            'Given the following premise and hypothesis:\nHypothesis: [INPUT_A]\nPremise: [INPUT_B]\nDetermine the logical relationship: [LABELS_CHOICE]',
            'Choose the most appropriate relationship between the premise and hypothesis:\nRelationship between "[INPUT_B]" and "[INPUT_A]": [LABELS_CHOICE]',
            'Identify the relationship between the premise and hypothesis:\nHypothesis: [INPUT_A]\nPremise: [INPUT_B]\nLabel: [LABELS_CHOICE]',
            'Classify the relationship between the premise and hypothesis:\nPremise: [INPUT_B]\nHypothesis: [INPUT_A]\nRelationship: [LABELS_CHOICE]',
        ],
        # Tasks.NEXT_SENTENCE_PREDICTION
        'NSP': [
            'Is tweet "[INPUT_B]" a continuation of tweet "[INPUT_A]"?',
            'Does tweet "[INPUT_B]" a logical continuation of tweet "[INPUT_A]"?',
            'Do tweet "[INPUT_A]" and tweet "[INPUT_B]" form a coherent sequence?',
            'Is tweet "[INPUT_B]" a relevant continuation of tweet "[INPUT_A]"?',
            'Can tweet "[INPUT_B]" be considered a direct continuation to tweet "[INPUT_A]"?'
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
            'Klasifikasikan sentimen dari kalimat berikut.\n[INPUT] => Sentimen: [LABELS_CHOICE]',
            'Prediksikan sentimen dari kalimat berikut.\nText: [INPUT] => [LABELS_CHOICE]',
            '[INPUT]\nApakah sentimen dari kalimat diatas? [LABELS_CHOICE]',
            'Apakah sentimen dari teks berikut?\nTeks: [INPUT]\nSentimen: [LABELS_CHOICE]',
            'Teks: [INPUT]\nTolong klasifikasikan sentimen dari teks diatas. Sentimen: [LABELS_CHOICE]',
        ],
        # Tasks.SHORT_ANSWER_GRADING
        'SAG': [
            'Klasifikasikan nilai dari jawaban ujian berikut.\n[INPUT] => Nilai: [LABELS_CHOICE]',
            'Prediksikan nilai dari jawaban ujian berikut.\n[INPUT] => [LABELS_CHOICE]',
            '[INPUT]\nApakah nilai dari jawaban ujian diatas? [LABELS_CHOICE]',
            'Apakah nilai dari jawaban ujian berikut?\nJawaban: [INPUT]\nNilai: [LABELS_CHOICE]',
            'Teks: [INPUT]\nTolong klasifikasikan sentimen dari teks diatas. Nilai: [LABELS_CHOICE]',
        ],
        # Tasks.EMOTION_CLASSIFICATION
        'EC': [
            'Klasifikasikan emosi dari kalimat berikut.\n[INPUT] => Emosi: [LABELS_CHOICE]',
            'Prediksikan emosi dari kalimat berikut.\nText: [INPUT] => [LABELS_CHOICE]',
            '[INPUT]\nApakah emosi dari kalimat diatas? [LABELS_CHOICE]',
            'Apakah emosi dari teks berikut?\nTeks: [INPUT]\nEmosi: [LABELS_CHOICE]',
            'Teks: [INPUT]\nTolong klasifikasikan emosi dari teks diatas. Emosi: [LABELS_CHOICE]',
        ],
        # Tasks.LEGAL_CLASSIFICATION
        'LC':  [
            'Klasifikasikan keputusan dari pernyataan hukum berikut.\n[INPUT] => Keputusan: [LABELS_CHOICE]',
            'Prediksikan keputusan dari pernyataan hukum berikut.\n[INPUT] => [LABELS_CHOICE]',
            '[INPUT]\nApakah keputusan dari pernyataan hukum diatas? [LABELS_CHOICE]',
            'Apakah keputusan dari pernyataan hukum berikut?\n[INPUT]\nKeputusan: [LABELS_CHOICE]',
            '[INPUT]\nTolong klasifikasikan keputusan dari pernyataan hukum diatas. Keputusan: [LABELS_CHOICE]',
        ],
        # Tasks.TEXTUAL_ENTAILMENT
        'TE': [
            'Hipotesis: [INPUT_A]\nPremis: [INPUT_B]\nPertanaan: Apakah hubungan antara hipotesis dan premis diatas? [LABELS_CHOICE]',
            'Diberikan hipotesis dan premis sebagai berikut:\nHipotesis: [INPUT_A]\nPremis: [INPUT_B]\nTentukan hubungan logis dari kedua kalimat tersebut: [LABELS_CHOICE]',
            'Pilih hubungan yang paling cocok antara premis dan hipotesis berikut:\nHubungan antara "[INPUT_B]" dan "[INPUT_A]": [LABELS_CHOICE]',
            'Identifikasi hubungan antara premis dan hipotesis berikut:\nHipotesis: [INPUT_A]\nPremis: [INPUT_B]\nLabel: [LABELS_CHOICE]',
            'Klasifikasikan hubungan antara premis dan hypothesis berikut:\nPremis: [INPUT_B]\nHipotesis: [INPUT_A]\nHubungan: [LABELS_CHOICE]',
        ],
        # Tasks.NEXT_SENTENCE_PREDICTION
        'NSP': [
            'Apakah tweet "[INPUT_B]" kelanjutan dari tweet "[INPUT_A]"?',
            'Apakah tweet "[INPUT_B]" merupakan kelanjutan logis dari tweet "[INPUT_A]"?',
            'Apakah tweet "[INPUT_A]" dan tweet "[INPUT_B]" membentuk sebuah urutan yang koheren?',
            'Apakah tweet "[INPUT_B]" merupakan sambungan yang relevan dengan tweet "[INPUT_A]"?',
            'Bisakah tweet "[INPUT_B]" dianggap sebagai sambunagn langsung dari tweet "[INPUT_A]"?'
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
		'eng': {'for': 'entailment', 'against': 'contradiction', 'no': 'irrelevant'},
		'ind': {'for': 'saling mendukung', 'against': 'saling berlawanan', 'no': 'tidak berhubungan'}
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

def get_label_mapping(dset_subset, prompt_lang):
    return LABEL_LANG_MAP[dset_subset][prompt_lang]

def get_prompt(prompt_lang):
    prompt_templates = {}
    for config, prompts in TASK_TO_PROMPT[prompt_lang].items():
        prompt_templates[config] = prompts
    return prompt_templates
