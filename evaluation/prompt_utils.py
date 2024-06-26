TASK_TO_PROMPT = {
    'eng': {
        'TRUTHFULQA': [
            '[QUESTION]\n[LABELS_CHOICE]',
            'Question: [QUESTION]\nAnswer: [LABELS_CHOICE]',
            'What is the best answer for the given question: [QUESTION]\nAnswer: [LABELS_CHOICE]',
            '[QUESTION]\nAnswer: [LABELS_CHOICE]',
        ],
        # COPA-style (no nusacrowd Tasks yet)
        'COPA': [
            {'cause': '[PREMISE] This happened because...\nHelp me pick the more plausible option: - choice1: [OPTION_1], choice2: [OPTION_2]\n\n[LABELS_CHOICE]',
             'effect': '[PREMISE] As a consequence...\nHelp me pick the more plausible option: - choice1: [OPTION_1], choice2: [OPTION_2]\n\n[LABELS_CHOICE]'},
            {'cause': '[PREMISE]\n\nselect the most plausible cause:\n - [OPTION_1]\n - [OPTION_2]\n\n[LABELS_CHOICE]',
             'effect': '[PREMISE]\n\nselect the most plausible effect:\n - [OPTION_1]\n - [OPTION_2]\n\n[LABELS_CHOICE]'},
            {'cause': '[PREMISE_STRIP] because [LABELS_CHOICE]',
             'effect': '[PREMISE_STRIP] therefore [LABELS_CHOICE]'},
            {'cause': '[PREMISE_STRIP]. What was the cause? [LABELS_CHOICE]',
             'effect': '[PREMISE_STRIP]. What happened as a result? [LABELS_CHOICE]'},
        ],
        # MABL-style (no nusacrowd Tasks yet)
        'MABL': [
            'The sentence "[PREMISE]" implies [LABELS_CHOICE]',
            '"[PREMISE]" suggests that [LABELS_CHOICE]',
            '[PREMISE]\n\nThe statement above implies: [LABELS_CHOICE]',
            '[PREMISE]\n\nThe above statement entails [LABELS_CHOICE]'
        ],
        # MAPS-style (no nusacrowd Tasks yet)
        'MAPS': [
            'Question: What does the person mean by the proverb?\nProverb: [PREMISE]\nContext: [CONTEXT]\nChoices: A: [OPTION_1] B: [OPTION_2]\nAnswer: [LABELS_CHOICE]',
            'Question: What does the proverb means in this context?\nProverb: [PREMISE]\nContext: [CONTEXT]\nChoices: A: [OPTION_1] B: [OPTION_2]\nAnswer: [LABELS_CHOICE]',
            'Question: Which sense is more suitable given the following proverb and its context?\nProverb: [PREMISE]\nContext: [CONTEXT]\nChoices: A: [OPTION_1] B: [OPTION_2]\nAnswer: [LABELS_CHOICE]',
            'Question: Which interpretation is more likely to define the proverb?\nProverb: [PREMISE]\nContext: [CONTEXT]\nChoices: A: [OPTION_1] B: [OPTION_2]\nAnswer: [LABELS_CHOICE]',
        ],
        # IndoStoryCloze-style (no nusacrowd Tasks yet)
        'IndoStoryCloze': [
            '[PREMISE]. [LABELS_CHOICE]',
            'Continue the following paragraph:\n[PREMISE]. [LABELS_CHOICE]',
            '[PREMISE]\nMake a sentence to continue the paragraph above: [LABELS_CHOICE]',
            '[PREMISE]\nWhat sentence is suitable to follow the paragraph above? Answer: [LABELS_CHOICE]',
        ],
        # IndoMMLU-style (no nusacrowd Tasks yet)
        'IndoMMLU': [
            'This is a [SUBJECT] question for [LEVEL]. Choose one of the answers that is considered correct!\n\n[INPUT]\n[OPTION]\n\nAnswer: [LABELS_CHOICE]',
            'The following is a [SUBJECT] question for [LEVEL] level. Choose the right answer!\nQuestion:[INPUT]\nChoice: [OPTION]\nAnswer: [LABELS_CHOICE]',
            'Choose one of the most appropriate answers to answer the [SUBJECT] question for [LEVEL]!\nQuestion: [INPUT]\nChoice: [OPTION]\n\nAnswer: [LABELS_CHOICE]' 
            ],
        # Tasks.SENTIMENT_ANALYSIS
        'SA': [
            'Classify the sentiment of the text below.\n[INPUT] => Sentiment ([OPTIONS]): [LABELS_CHOICE]',
            'Predict the sentiment of the following text.\nText: [INPUT]\nAnswer with [OPTIONS]: [LABELS_CHOICE]',
            '[INPUT]\nWhat would be the sentiment of the text above? [OPTIONS]? [LABELS_CHOICE]',
            'What is the sentiment of this text?\nText: [INPUT]\nSentiment ([OPTIONS]): [LABELS_CHOICE]',
            'Text: [INPUT]\nPlease classify the sentiment of above text. Answer with [OPTIONS].\nSentiment: [LABELS_CHOICE]',
        ],
        # Tasks.SHORT_ANSWER_GRADING
        'SAG': [
            'Eestimate the grade of the test answer below.\n[INPUT] => Grade ([OPTIONS]): [LABELS_CHOICE]',
            'Predict the grade of the following test answer.\nText: [INPUT]\nAnswer with [OPTIONS]: [LABELS_CHOICE]',
            '[INPUT]\nWhat would be the grade of the test answer above? [OPTIONS]? [LABELS_CHOICE]',
            'What is the grade of this test answer?\nText: [INPUT]\nGrade ([OPTIONS]): [LABELS_CHOICE]',
            'Text: [INPUT]\nPlease estimate the grade of above test answer. Answer with [OPTIONS].\nGrade: [LABELS_CHOICE]',
        ],
        # Tasks.EMOTION_CLASSIFICATION
        'EC': [
            'Classify the emotion of the text below.\n[INPUT] => Emotion ([OPTIONS]): [LABELS_CHOICE]',
            'Predict the emotion of the following text.\nText: [INPUT]\nAnswer with [OPTIONS]: [LABELS_CHOICE]',
            '[INPUT]\nWhat would be the emotion of the text above? [OPTIONS]? [LABELS_CHOICE]',
            'What is the emotion of this text?\nText: [INPUT]\nEmotion ([OPTIONS]): [LABELS_CHOICE]',
            'Text: [INPUT]\nPlease classify the emotion of above text. Answer with [OPTIONS].\nEmotion: [LABELS_CHOICE]',
        ],
        # Tasks.LEGAL_CLASSIFICATION
        'LC':  [
            'Classify the verdict of the legal statement below.\n[INPUT] => Verdict ([OPTIONS]): [LABELS_CHOICE]',
            'Predict the verdict of the following legal statement.\nText: [INPUT]\nAnswer with [OPTIONS]: [LABELS_CHOICE]',
            '[INPUT]\nWhat would be the verdict of the legal statement above? [OPTIONS]? [LABELS_CHOICE]',
            'What is the verdict of this legal statement?\nText: [INPUT]\nVerdict ([OPTIONS]): [LABELS_CHOICE]',
            'Text: [INPUT]\nPlease classify the verdict of above legal statement. Answer with [OPTIONS].\nVerdict: [LABELS_CHOICE]',
        ],
        # Tasks.TEXTUAL_ENTAILMENT
        'TE': [
            'Hypothesis: [INPUT_A]\nPremise: [INPUT_B]\nQuestion: What is the relation between the hypothesis and the premise? [OPTIONS]? [LABELS_CHOICE]',
            'Given the following premise and hypothesis:\nHypothesis: [INPUT_A]\nPremise: [INPUT_B]\nDetermine the logical relationship (([OPTIONS])): [LABELS_CHOICE]',
            'Choose the most appropriate relationship ([OPTIONS]) between the premise and hypothesis:\nRelationship between "[INPUT_B]" and "[INPUT_A]": [LABELS_CHOICE]',
            'Identify the relationship between the premise and hypothesis:\nHypothesis: [INPUT_A]\nPremise: [INPUT_B]\nLabel ([OPTIONS]): [LABELS_CHOICE]',
            'Classify the relationship between the premise and hypothesis:\nPremise: [INPUT_B]\nHypothesis: [INPUT_A]\nRelationship ([OPTIONS]): [LABELS_CHOICE]',
        ],
        # Tasks.NEXT_SENTENCE_PREDICTION
        'NSP': [
            'Is tweet "[INPUT_B]" a continuation of tweet "[INPUT_A]"? [OPTIONS]? [LABELS_CHOICE]',
            'Does tweet "[INPUT_B]" a logical continuation of tweet "[INPUT_A]"? Answer with [OPTIONS]? [LABELS_CHOICE]',
            'Do tweet "[INPUT_A]" and tweet "[INPUT_B]" form a coherent sequence? Answer with [OPTIONS]? [LABELS_CHOICE]',
            'Is tweet "[INPUT_B]" a relevant continuation of tweet "[INPUT_A]"? Answer with [OPTIONS]? [LABELS_CHOICE]',
            'Can tweet "[INPUT_B]" be considered a direct continuation to tweet "[INPUT_A]"? Answer with [OPTIONS]? [LABELS_CHOICE]'
        ],

        # Tasks.MACHINE_TRANSLATION
        'MT': [
            'Translate the following text from [SOURCE] to [TARGET].\nText: [INPUT]\nTranslation:',
            '[INPUT]\nTranslate the text above from [SOURCE] to [TARGET].',
            'Text in [SOURCE]: [INPUT]\nHow would you translate that in [TARGET]?',
            'Translate the following [SOURCE] text to [TARGET].\nText: [INPUT]\nTranslation:',
            'Text in [SOURCE]: [INPUT]\nText in [TARGET]:',
        ],
        # Tasks.PARAPHRASING
        'PARA': [
            'Write a paraphrase the following text.\nText: [INPUT]\nParaphrase:',
            '[INPUT]\nWrite a paraphrase of the text above.',
            'Text: [INPUT]\nHow would you rewrite this text?',
            'Paraphrase this text: [INPUT]\nParaphrase:',
            '[INPUT]\nRewrite the text above.',
        ],
        # Tasks.QUESTION_ANSWERING
        'QA': [
            'Refer to the passage below and answer the following question:\nPassage: [CONTEXT]\nQuestion: [QUESTION]\nAnswer:',
            '[CONTEXT]\nBased on the above text, [QUESTION]',
            '[CONTEXT]\nQuestion: [QUESTION]\nReferring to the passage above, the correct answer to the given question is:',
            'Paragraph: [CONTEXT]\nQuestion: [QUESTION]\nBased on the paragraph, what is the answer to the question?',
            'Passage: [CONTEXT]\nQuestion: [QUESTION]\nAnswer:'
        ],
        # Tasks.SUMMARIZATION
        'SUM': [
            'Write a summary from of the following text.\nText: [INPUT]\nSummary:',
            '[INPUT]\nWrite a summary of the text above.',
            'Text: [INPUT]\nHow would you summarize this text?',
            'Summarize this text: [INPUT]\nSummary:',
            '[INPUT]\nGiven the above document, write one sentence to summarize:',
        ],
        # Tasks.DIALOGUE_SYSTEM
        'DS': [
            'Write a response to continue the following dialogue.\n[INPUT]\nResponse:',
            '[INPUT]\n\nWrite an appropriate response to continue the conversation above.',
            '[INPUT]\n\nHow would you response to the above dialogue?',
            'Provide the response for this dialogue:\n[INPUT]\nResponse:',
            '[INPUT]\nGiven the above conversation, write the response to continue the conversation:',
        ],
    },
    'ind': {
        'TRUTHFULQA': [
            '[QUESTION]\n[LABELS_CHOICE]',
            'Pertanyaan: [QUESTION]\nJawaban: [LABELS_CHOICE]',
            'Apa jawaban terbaik dari pertanyaan berikut: [QUESTION]\nJawaban: [LABELS_CHOICE]',
            '[QUESTION]\nJawaban: [LABELS_CHOICE]',
        ],
        # COPA-style (no nusacrowd Tasks yet)
        'COPA': [
            {'cause': '[PREMISE] Ini terjadi karena...\nBantu saya memilih opsi yang paling mungkin: - opsi1: [OPTION_1], opsi2: [OPTION_2]\n\n[LABELS_CHOICE]',
             'effect': '[PREMISE] Konsekuensinya...\nBantu saya memilih opsi yang paling mungkin: -opsi1: [OPTION_1], opsi2: [OPTION_2]\n\n[LABELS_CHOICE]'},
            {'cause': '[PREMISE]\n\npilih penyebab yang paling mungkin:\n - [OPTION_1]\n - [OPTION_2]\n\n[LABELS_CHOICE]',
             'effect': '[PREMISE]\n\npilih efek yang paling mungkin:\n - [OPTION_1]\n - [OPTION_2]\n\n[LABELS_CHOICE]'},
            {'cause': '[PREMISE_STRIP] karena [LABELS_CHOICE]',
             'effect': '[PREMISE_STRIP] maka [LABELS_CHOICE]'},
            {'cause': '[PREMISE_STRIP]. Apa penyebabnya? [LABELS_CHOICE]',
             'effect': '[PREMISE_STRIP]. Apa akibatnya? [LABELS_CHOICE]'},
        ],
        # MABL-style (no nusacrowd Tasks yet)
        'MABL': [
            'Dari kalimat "[PREMISE]" bisa disimpulkan bahwa [LABELS_CHOICE]',
            '"[PREMISE]" menunjukan [LABELS_CHOICE]',
            '[PREMISE]\n\nKalimat diatas menyatakan bahwa: [LABELS_CHOICE]',
            '[PREMISE]\n\nKalimat tersebut menyimpulkan [LABELS_CHOICE]'
        ],
        # MAPS-style (no nusacrowd Tasks yet)
        'MAPS': [
            'Pertanyaan: Apa yang orang itu maksud dengan peribahasa berikut?\nPeribahasa [PREMISE]\nKonteks: [CONTEXT]\nPilihan: A: [OPTION_1] B: [OPTION_2]\nJawaban: [LABELS_CHOICE]',
            'Pertanyaan: Apa arti peribahasa dalam konteks berikut?\nPeribahasa [PREMISE]\nKonteks: [CONTEXT]\nPilihan: A: [OPTION_1] B: [OPTION_2]\nJawaban: [LABELS_CHOICE]',
            'Pertanyaan: Makna apa yang lebih tepat untuk mengartikan peribahasa dari konteks berikut?\nPeribahasa [PREMISE]\nKonteks: [CONTEXT]\nPilihan: A: [OPTION_1] B: [OPTION_2]\nJawaban: [LABELS_CHOICE]',
            'Pertanyaan: Interpretasi mana yang lebih memungkinkan untuk mendefinisikan peribahasa berikut?\nPeribahasa [PREMISE]\nKonteks: [CONTEXT]\nPilihan: A: [OPTION_1] B: [OPTION_2]\nJawaban: [LABELS_CHOICE]',
        ],    
        # IndoStoryCloze-style (no nusacrowd Tasks yet)
        'IndoStoryCloze': [
            '[PREMISE]. [LABELS_CHOICE]',
            'Lanjutkan paragraf berikut:\n[PREMISE]. [LABELS_CHOICE]',
            '[PREMISE]\nBuat kalimat untuk melanjutkan paragraf diatas: [LABELS_CHOICE]',
            '[PREMISE]\nKalimat apa yang sesuai untuk menyambung paragraf diatas? Jawaban: [LABELS_CHOICE]',
        ],
        # IndoMMLU-style (no nusacrowd Tasks yet)
        'IndoMMLU': [
            'Ini adalah soal [SUBJECT] untuk [LEVEL]. Pilihlah salah satu jawaban yang dianggap benar!\n\n[INPUT]\n[OPTION]\n\nJawaban: [LABELS_CHOICE]',
            'Berikut ini adalah soal [SUBJECT] untuk tingkat [LEVEL]. Pilih jawaban yang tepat!\nSoal:[INPUT]\nPilihan: [OPTION]\nJawaban: [LABELS_CHOICE]',
            'Pilihlah salah satu jawaban yang paling tepat untuk menjawab soal [SUBJECT] untuk [LEVEL] berikut!\nSoal: [INPUT]\nPilihan: [OPTION]\n\nJawaban: [LABELS_CHOICE]'
        ],
        # Tasks.SENTIMENT_ANALYSIS
        'SA': [
            'Klasifikasikan sentimen dari kalimat berikut.\n[INPUT] => Sentimen ([OPTIONS]): [LABELS_CHOICE]',
            'Prediksikan sentimen dari kalimat berikut.\nTeks: [INPUT]\nJawab dengan [OPTIONS]: [LABELS_CHOICE]',
            '[INPUT]\nApakah sentimen dari kalimat diatas? [OPTIONS]? [LABELS_CHOICE]',
            'Apakah sentimen dari teks berikut?\nTeks: [INPUT]\nSentimen ([OPTIONS]): [LABELS_CHOICE]',
            'Teks: [INPUT]\nTolong klasifikasikan sentimen dari teks diatas. Jawab dengan [OPTIONS].\nSentimen: [LABELS_CHOICE]',
        ],
        # Tasks.SHORT_ANSWER_GRADING
        'SAG': [
            'Klasifikasikan nilai dari jawaban ujian berikut.\n[INPUT] => Nilai ([OPTIONS]): [LABELS_CHOICE]',
            'Prediksikan nilai dari jawaban ujian berikut.\nTeks: [INPUT]\nJawab dengan [OPTIONS]: [LABELS_CHOICE]',
            '[INPUT]\nApakah nilai dari jawaban ujian diatas? [OPTIONS]? [LABELS_CHOICE]',
            'Apakah nilai dari jawaban ujian berikut?\nTeks: [INPUT]\nNilai ([OPTIONS]): [LABELS_CHOICE]',
            'Teks: [INPUT]\nTolong klasifikasikan nilai dari jawaban ujian diatas. Jawab dengan [OPTIONS].\nNilai: [LABELS_CHOICE]',
        ],
        # Tasks.EMOTION_CLASSIFICATION
        'EC': [
            'Klasifikasikan emosi dari kalimat berikut.\n[INPUT] => Emosi ([OPTIONS]): [LABELS_CHOICE]',
            'Prediksikan emosi dari kalimat berikut.\nTeks: [INPUT]\nJawab dengan [OPTIONS]: [LABELS_CHOICE]',
            '[INPUT]\nApakah emosi dari kalimat diatas? [OPTIONS]? [LABELS_CHOICE]',
            'Apakah emosi dari teks berikut?\nTeks: [INPUT]\nEmosi ([OPTIONS]): [LABELS_CHOICE]',
            'Teks: [INPUT]\nTolong klasifikasikan emosi dari teks diatas. Jawab dengan [OPTIONS].\nEmosi: [LABELS_CHOICE]',
        ],
        # Tasks.LEGAL_CLASSIFICATION
        'LC':  [
            'Klasifikasikan keputusan dari pernyataan hukum berikut.\n[INPUT] => Keputusan ([OPTIONS]): [LABELS_CHOICE]',
            'Prediksikan keputusan dari pernyataan hukum berikut.\nText: [INPUT]\nJawab dengan [OPTIONS]: [LABELS_CHOICE]',
            '[INPUT]\nApakah keputusan dari pernyataan hukum diatas? [OPTIONS]? [LABELS_CHOICE]',
            'Apakah keputusan dari teks berikut?\nTeks: [INPUT]\nKeputusan ([OPTIONS]): [LABELS_CHOICE]',
            'Teks: [INPUT]\nTolong klasifikasikan keputusan dari teks diatas. Jawab dengan [OPTIONS].\nKeputusan: [LABELS_CHOICE]',
        ],
        # Tasks.TEXTUAL_ENTAILMENT
        'TE': [
            'Hipotesis: [INPUT_A]\nPremis: [INPUT_B]\nPertanaan: Apakah hubungan antara hipotesis dan premis diatas? [OPTIONS]? [LABELS_CHOICE]',
            'Diberikan hipotesis dan premis sebagai berikut:\nHipotesis: [INPUT_A]\nPremis: [INPUT_B]\nTentukan hubungan logis ([OPTIONS]) dari kedua kalimat tersebut: [LABELS_CHOICE]',
            'Pilih hubungan ([OPTIONS]) yang paling cocok antara premis dan hipotesis berikut:\nHubungan antara "[INPUT_B]" dan "[INPUT_A]": [LABELS_CHOICE]',
            'Identifikasi hubungan antara premis dan hipotesis berikut:\nHipotesis: [INPUT_A]\nPremis: [INPUT_B]\nLabel ([OPTIONS]): [LABELS_CHOICE]',
            'Klasifikasikan hubungan antara premis dan hypothesis berikut:\nPremis: [INPUT_B]\nHipotesis: [INPUT_A]\nHubungan ([OPTIONS]): [LABELS_CHOICE]',
        ],
        # Tasks.NEXT_SENTENCE_PREDICTION
        'NSP': [
            'Apakah tweet "[INPUT_B]" kelanjutan dari tweet "[INPUT_A]"? [OPTIONS]? [LABELS_CHOICE]',
            'Apakah tweet "[INPUT_B]" merupakan kelanjutan logis dari tweet "[INPUT_A]"? Jawab dengan [OPTIONS]? [LABELS_CHOICE]',
            'Apakah tweet "[INPUT_A]" dan tweet "[INPUT_B]" membentuk sebuah urutan yang koheren? Jawab dengan [OPTIONS]? [LABELS_CHOICE]',
            'Apakah tweet "[INPUT_B]" merupakan sambungan yang relevan dengan tweet "[INPUT_A]"? Jawab dengan [OPTIONS]? [LABELS_CHOICE]',
            'Bisakah tweet "[INPUT_B]" dianggap sebagai sambungan langsung dari tweet "[INPUT_A]"? Jawab dengan [OPTIONS]? [LABELS_CHOICE]'
        ],

        # Tasks.MACHINE_TRANSLATION
        'MT': [
            'Terjemahkan teks berikut dari bahasa [SOURCE] ke bahasa [TARGET].\nTeks: [INPUT]\nTerjemahan:',
            '[INPUT]\nTerjemahkan teks di atas dari bahasa [SOURCE] ke bahasa [TARGET].',
            'Teks dalam bahasa [SOURCE]: [INPUT]\nApa terjemahannya dalam bahasa [TARGET]?',
            'Terjemahkan teks bahasa [SOURCE] berikut ke bahasa [TARGET].\nTeks: [INPUT]\nTerjemahan:',
            'Teks dalam bahasa [SOURCE]: [INPUT]\nTeks dalam bahasa [TARGET]:',
        ],
        # Tasks.PARAPHRASING
        'PARA': [
            'Tuliskan parafrasa dari teks berikut.\nTeks: [INPUT]\nParafrasa:',
            '[INPUT]\nTuliskan parafrasa dari teks di atas.',
            'Teks: [INPUT]\nApa parafrasa dari teks tersebut?',
            'Parafrasakan teks berikut: [INPUT]\nParafrasa:',
            '[INPUT]\nParafrasa dari teks di atas adalah:',
        ],
        # Tasks.QUESTION_ANSWERING
        'QA': [
            'Lihat paragraf di bawah ini dan jawab pertanyaannya.\nParagraf: [CONTEXT]\nPertanyaan: [QUESTION]\nJawaban:',
            '[CONTEXT]\nBerdasarkan teks di atas, [QUESTION]',
            '[CONTEXT]\nQuestion: [QUESTION]\nMengacu pada teks di atas, jawaban yang benar untuk pertanyaan yang diberikan adalah:',
            'Paragraf: [CONTEXT]\nPertanyaan: [QUESTION]\nBerdasarkan paragraf di atas, apa jawaban dari pertanyaan yang diberikan?',
            'Teks: [CONTEXT]\nPertanyaan: [QUESTION]\nJawaban:'
        ],
        # Tasks.SUMMARIZATION
        'SUM': [
            'Tuliskan ringkasan dari teks berikut.\nTeks: [INPUT]\nRingkasan:',
            '[INPUT]\nTulis ringkasan dari teks di atas.',
            'Teks: [INPUT]\nApa ringkasan dari teks tersebut?',
            'Ringkaslah teks berikut: [INPUT]\nRingkasan:',
            '[INPUT]\nBerdasarkan dokumen di atas, tulis satu kalimat ringkasan:',
        ],
        # Tasks.DIALOGUE_SYSTEM
        'DS': [
            'Tulis respon untuk melanjutkan dialog berikut.\n[INPUT]\nRespon:',
            '[INPUT]\n\nTulis respon yang sesuai untuk melanjukan percakapan diatas.',
            '[INPUT]\n\nBagaimana kamu merespon dialog diatas?',
            'Berikan respon untuk dialog berikut:\n[INPUT]\nRespon:',
            '[INPUT]\nDiberikan sebuah percakapan, tuliskan respon yang sesuai untuk melanjutkan percakapan tersebut:',
        ],
    }
}

LABEL_LANG_MAP ={
    'truthfulqa': {
        'eng': {0: '0', 1: '1'},
        'ind': {0: '0', 1: '1'}
    },
    'haryoaw/COPAL': {
        'eng': {0: '0', 1: '1'},
        'ind': {0: '0', 1: '1'}
    },
    'MABL/id': {
        'eng': {0: '0', 1: '1'},
        'ind': {0: '0', 1: '1'}
    },
    'MABL/jv': {
        'eng': {0: '0', 1: '1'},
        'ind': {0: '0', 1: '1'}
    },
    'MABL/su': {
        'eng': {0: '0', 1: '1'},
        'ind': {0: '0', 1: '1'}
    },
    'MAPS': {
        'eng': {'a': 'A', 'b': 'B'},
        'ind': {'a': 'A', 'b': 'B'}
    },
    'MAPS/figurative': {
        'eng': {'a': 'A', 'b': 'B'},
        'ind': {'a': 'A', 'b': 'B'}
    },
    'MAPS/non_figurative': {
        'eng': {'a': 'A', 'b': 'B'},
        'ind': {'a': 'A', 'b': 'B'}
    },
    'IndoStoryCloze': {
        'eng': {0: '0', 1: '1'},
        'ind': {0: '0', 1: '1'}
    },
    'IndoMMLU': {
        'eng': {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'},
        'ind': {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
    },
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

LANG_MAP = {
    'eng': {
        'ind': 'Indonesian',
        'xdy': 'Dayak',
        'bug': 'Buginese',
        'mad': 'Madurese',
        'bjn': 'Banjarese',
        'tiociu': 'Tiociu',
        'jav': 'Javanese',
        'sun': 'Sundanese',
        'ace': 'Acehnese',
        'ban': 'Balinese',
        'min': 'Minangkabau'
    },
    'ind': {
        'ind': 'Indonesia',
        'xdy': 'Dayak',
        'bug': 'Bugis',
        'mad': 'Madura',
        'bjn': 'Banjar',
        'tiociu': 'Tiociu',
        'jav': 'Jawa',
        'sun': 'Sunda',
        'ace': 'Aceh',
        'ban': 'Bali',
        'min': 'Minangkabau'
    }
}

def get_label_mapping(dset_subset, prompt_lang):
    return LABEL_LANG_MAP[dset_subset][prompt_lang]

def get_lang_name(prompt_lang, lang_code):
    return LANG_MAP[prompt_lang][lang_code]

def get_prompt(prompt_lang):
    prompt_templates = {}
    for config, prompts in TASK_TO_PROMPT[prompt_lang].items():
        prompt_templates[config] = prompts
    return prompt_templates
