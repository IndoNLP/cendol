# %%
import os
import pandas as pd

script_folder = os.path.dirname(os.path.abspath(__file__))
path_list = ["generated_dataset", "generated_parallel_dataset_default", "generated_parallel_dataset_nondefault"]

### these three path are executed from different python script w/ different args
### simplest one: generated_dataset csv files (no parallelization)
### "generated_dataset" -> python generate_dataset.py --dataset-name korpus_nusantara --subset-name korpus_nusantara_ind_bbc_nusantara
### med one: generated_parallel_dataset_default csv files (parallelization with half of the total cores used)
### "generated_parallel_dataset_default" -> python generate_dataset_batch_parallel.py --dataset-name korpus_nusantara --subset-name korpus_nusantara_ind_bbc_nusantara --split-on-prompts True --num-shard 3 --checkpoint-save-path generated_parallel_dataset_default --parallelize-flag y
### adv one: generated_parallel_dataset_nondefault csv files (parallelization with custom cores w/ max n_cpu-1)
### "generated_parallel_dataset_default" -> python generate_dataset_batch_parallel.py --dataset-name korpus_nusantara --subset-name korpus_nusantara_ind_bbc_nusantara --split-on-prompts True --num-shard 7 --checkpoint-save-path generated_parallel_dataset_nondefault --parallelize-flag y --num-concurrent-process 7

# %%
dset_list = list()

for folder_path in path_list:
    all_csv_path = [path for path in os.listdir(os.path.join(script_folder, folder_path)) if path.endswith(".csv")]
    print(all_csv_path)
    if len(all_csv_path) > 1:
        dset_list.append(pd.concat([pd.read_csv(os.path.join(folder_path, file_path)) for file_path in all_csv_path], ignore_index=True))
    else:
        dset_list.append(pd.read_csv(os.path.join(folder_path, all_csv_path[0])))

# %%
if not (all(dset_list[0] == dset_list[1]) and all(dset_list[0] == dset_list[2]) and all(dset_list[1] == dset_list[2])):
    raise AssertionError("There's something wrong on dataset generation script!")