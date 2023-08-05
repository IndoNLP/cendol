# # Zero-Shot mT0 Ind
CUDA_VISIBLE_DEVICES=0 python main_nlu_prompt_batch.py ind bigscience/mt0-small 32 &
CUDA_VISIBLE_DEVICES=1 python main_nlu_prompt_batch.py ind bigscience/mt0-base 16 &
CUDA_VISIBLE_DEVICES=2 python main_nlu_prompt_batch.py ind bigscience/mt0-large 8 &
CUDA_VISIBLE_DEVICES=3 python main_nlu_prompt_batch.py ind bigscience/mt0-xl 4 &
CUDA_VISIBLE_DEVICES=4 python main_nlu_prompt_batch.py ind bigscience/mt0-xxl 2

# # Zero-Shot BLOOMZ Ind
CUDA_VISIBLE_DEVICES=0 python main_nlu_prompt_batch.py ind bigscience/bloomz-560m 16 &
CUDA_VISIBLE_DEVICES=1 python main_nlu_prompt_batch.py ind bigscience/bloomz-1b1 12 &
CUDA_VISIBLE_DEVICES=2 python main_nlu_prompt_batch.py ind bigscience/bloomz-1b7 8 &
CUDA_VISIBLE_DEVICES=3 python main_nlu_prompt_batch.py ind bigscience/bloomz-3b 4 &
CUDA_VISIBLE_DEVICES=4 python main_nlu_prompt_batch.py ind bigscience/bloomz-7b1 2

# Zero-Shot mT0 Eng
CUDA_VISIBLE_DEVICES=4 python main_nlu_prompt_batch.py eng bigscience/mt0-small 32 &
CUDA_VISIBLE_DEVICES=3 python main_nlu_prompt_batch.py eng bigscience/mt0-base 16 &
CUDA_VISIBLE_DEVICES=0 python main_nlu_prompt_batch.py eng bigscience/mt0-large 8 &
CUDA_VISIBLE_DEVICES=3 python main_nlu_prompt_batch.py eng bigscience/mt0-xl 4 &
CUDA_VISIBLE_DEVICES=4 python main_nlu_prompt_batch.py eng bigscience/mt0-xxl 2

# Zero-Shot BLOOMZ Eng
CUDA_VISIBLE_DEVICES=4 python main_nlu_prompt_batch.py eng bigscience/bloomz-560m 16 &
CUDA_VISIBLE_DEVICES=2 python main_nlu_prompt_batch.py eng bigscience/bloomz-1b1 12 &
CUDA_VISIBLE_DEVICES=5 python main_nlu_prompt_batch.py eng bigscience/bloomz-1b7 8 &
CUDA_VISIBLE_DEVICES=1 python main_nlu_prompt_batch.py eng bigscience/bloomz-3b 4 &
CUDA_VISIBLE_DEVICES=4 python main_nlu_prompt_batch.py eng bigscience/bloomz-7b1 2

# Zero-Shot Bactrian-X with Bloom 7B Ind
CUDA_VISIBLE_DEVICES=0 python main_nlu_prompt_batch.py ind bigscience/bloom-7b1---MBZUAI/bactrian-x-bloom-7b1-lora 20
CUDA_VISIBLE_DEVICES=1 python main_nlu_prompt_batch.py ind bigscience/bloom-7b1---haonan-li/bactrian-id-bloom-7b1-lora 20

# Zero-Shot Bactrian-X with Bloom 7B Eng
CUDA_VISIBLE_DEVICES=0 python main_nlu_prompt_batch.py eng bigscience/bloom-7b1---MBZUAI/bactrian-x-bloom-7b1-lora 20
CUDA_VISIBLE_DEVICES=1 python main_nlu_prompt_batch.py eng bigscience/bloom-7b1---haonan-li/bactrian-id-bloom-7b1-lora 20
