import generate_dataset
import os

LANGUAGES = ["btk", "bew", "bug", "jav", "mad", "mak", "min", "mui", "rej", "sun"]

for i, dataset_name in enumerate(os.listdir("./promptsource/templates/")):
    if "nusaparagraph" not in dataset_name:
        continue
    for lang in LANGUAGES:
        print(i, dataset_name, lang)
        try:
            generate_dataset.run(dataset_name, f"{lang}_nusantara")
        except Exception as e:
            print('-- No `nusa` subset.')
            print(e)

print("END!!!")
# try:
#     generate_dataset.run("indonli", "nusa")
# except Exception as e:
#     print(e)