TASK_TO_PROMPT = {
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
        
    ],
    # Tasks.NEXT_SENTENCE_PREDICTION
    'NSP': [

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

def get_prompt():
    prompt_templates = {}
    for config, prompts in TASK_TO_PROMPT.items():
        prompt_templates[config] = prompts
    return prompt_templates
