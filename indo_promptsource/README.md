# IndoPromptSource
**IndoPromptSource is a toolkit for creating, sharing and using natural language prompts for NusaCrowd Datasets.**
We only download the first 10 samples from the training set of each dataset to speed up the prompt designing process.

## Setup
If you do not intend to modify prompts, you can simply run:
1. Install required packages
```bash
pip install -e .
```
2. Install nusacrowd
```
pip install git+https://github.com/IndoNLP/nusa-crowd.git@release_exp
```
3. Ensure you are in the `indo_promptsource directory`
4. Run streamlit
```
streamlit run promptsource/app.py
```

## How to create/edit/view prompt design
PromptSource provides a Web-based GUI that enables developers to write prompts in a templating language and immediately view their outputs on different examples.

There are 3 modes in the app:
- **Sourcing**: create and write new prompts
- **Prompted dataset viewer**: check the prompts you wrote (or the existing ones) on the entire dataset
- **Helicopter view**: aggregate high-level metrics on the current state of P3

For creating prompts, you can refer to the following screnshot
- **Original Task**: refers to whether the prompt is aligned with the proposed task (e.g. QA prompts for SQuAD-like dataset is original. However if we change the concept to question generation based on a given context and answer, then it is not original task)
- **Choices in Templates**: is the template contain answer options? Example usage with template:
![image](https://user-images.githubusercontent.com/68817249/229166140-0cfc0d0c-a85d-4828-9df1-e24bea962ea0.png)
- **Metrics**: common types used to classify a task
- **Prompt Language**: language of the proposed prompt
- **Template**: Prompt Template in Jinja format
![image](https://user-images.githubusercontent.com/68817249/229163860-054c5fa5-5975-494c-8b69-c11bb495b52a.png)

For viewing all existing prompts:
![image](https://user-images.githubusercontent.com/68817249/229165079-1c11ca80-644d-438d-b621-c5414418175d.png)

## Citation
If you find P3 or PromptSource useful, please cite the following reference:
```bibtex
@misc{bach2022promptsource,
      title={PromptSource: An Integrated Development Environment and Repository for Natural Language Prompts},
      author={Stephen H. Bach and Victor Sanh and Zheng-Xin Yong and Albert Webson and Colin Raffel and Nihal V. Nayak and Abheesht Sharma and Taewoon Kim and M Saiful Bari and Thibault Fevry and Zaid Alyafeai and Manan Dey and Andrea Santilli and Zhiqing Sun and Srulik Ben-David and Canwen Xu and Gunjan Chhablani and Han Wang and Jason Alan Fries and Maged S. Al-shaibani and Shanya Sharma and Urmish Thakker and Khalid Almubarak and Xiangru Tang and Xiangru Tang and Mike Tian-Jian Jiang and Alexander M. Rush},
      year={2022},
      eprint={2202.01279},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
```
