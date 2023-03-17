# Explore PromptSource

## Instruction to reproduce exploration
1. Clone PromptSource [repository](https://github.com/bigscience-workshop/promptsource)
2. Copy `promptsource` folder content to the cloned repository
3. Run `test_promptsource.ipynb`

## Exploration notes
- The exploration was tested on `ag_news` dataset which is available on huggingface

- Each of the row in the `ag_news` dataset is a json. Below is an example of one row: 
```json
{
    "text": "Carlyle Looks Toward Commercial Aerospace (Reuters) Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.", 
    "label": 2
}
```

- PromptSource transform a json string in python to a list of string in python

- What we can learn from the sample template [here](promptsource/templates/ag_news_2/templates.yaml):
    - in `jinja` field (`line 6-14`), calling a field name within `{{ }}` will call the value in the input json string key. 
        - For example in `ag_news`, `{{label}}` will put `2` in the output string.

    - We can define a list that can be called in `jinja` field as in `line 13` (`answer_choices` variable) with a script like in `line 4`. 
        - Each element is separated by `|||`.
    
    - Each element in the output list of string is separated with `|||` as well (`line 11`)

    - A sample of random variable (`_blank1` variable) is in `line 7`
        - Calling it within `{{ }}` will take a random element that has been defined (`line 9`)

- With what we have learned, it should be possible to create a pipeline for our dataset to be saved in P3-like format ([P3 dataset](https://huggingface.co/datasets/bigscience/P3)).

