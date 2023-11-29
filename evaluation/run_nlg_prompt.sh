# Zero-Shot mT0 Ind
CUDA_VISIBLE_DEVICES=0 python main_nlg_prompt_batch.py ind bigscience/mt0-small 0 64 &
CUDA_VISIBLE_DEVICES=1 python main_nlg_prompt_batch.py ind bigscience/mt0-base 0 32 &
CUDA_VISIBLE_DEVICES=2 python main_nlg_prompt_batch.py ind bigscience/mt0-large 0 16 &
CUDA_VISIBLE_DEVICES=3 python main_nlg_prompt_batch.py ind bigscience/mt0-xl 0 16
CUDA_VISIBLE_DEVICES=4 python main_nlg_prompt_batch.py ind bigscience/mt0-xxl 0 4

# Zero-Shot BLOOMZ Ind
CUDA_VISIBLE_DEVICES=0 python main_nlg_prompt_batch.py ind bigscience/bloomz-560m 0 5 &
CUDA_VISIBLE_DEVICES=1 python main_nlg_prompt_batch.py ind bigscience/bloomz-1b1 0 10 &
CUDA_VISIBLE_DEVICES=2 python main_nlg_prompt_batch.py ind bigscience/bloomz-1b7 0 8 &
CUDA_VISIBLE_DEVICES=3 python main_nlg_prompt_batch.py ind bigscience/bloomz-3b 0 4 &
CUDA_VISIBLE_DEVICES=4 python main_nlg_prompt_batch.py ind bigscience/bloomz-7b 0 2

# Zero-Shot mT0 Eng
CUDA_VISIBLE_DEVICES=0 python main_nlg_prompt_batch.py eng bigscience/mt0-small 0 64 &
CUDA_VISIBLE_DEVICES=1 python main_nlg_prompt_batch.py eng bigscience/mt0-base 0 32 &
CUDA_VISIBLE_DEVICES=2 python main_nlg_prompt_batch.py eng bigscience/mt0-large 0 16 &
CUDA_VISIBLE_DEVICES=3 python main_nlg_prompt_batch.py eng bigscience/mt0-xl 0 16
CUDA_VISIBLE_DEVICES=4 python main_nlg_prompt_batch.py eng bigscience/mt0-xxl 0 4

# Zero-Shot BLOOMZ Eng
CUDA_VISIBLE_DEVICES=0 python main_nlg_prompt_batch.py eng bigscience/bloomz-560m 0 5 &
CUDA_VISIBLE_DEVICES=1 python main_nlg_prompt_batch.py eng bigscience/bloomz-1b1 0 10 &
CUDA_VISIBLE_DEVICES=2 python main_nlg_prompt_batch.py eng bigscience/bloomz-1b7 0 8 &
CUDA_VISIBLE_DEVICES=3 python main_nlg_prompt_batch.py eng bigscience/bloomz-3b 0 4 &
CUDA_VISIBLE_DEVICES=4 python main_nlg_prompt_batch.py eng bigscience/bloomz-7b 0 2

# Zero-Shot Bactrian-X with Bloom 7B Ind
CUDA_VISIBLE_DEVICES=0 python main_nlg_prompt_batch.py ind bigscience/bloom-7b1---MBZUAI/bactrian-x-bloom-7b1-lora 0 20
CUDA_VISIBLE_DEVICES=1 python main_nlg_prompt_batch.py ind bigscience/bloom-7b1---haonan-li/bactrian-id-bloom-7b1-lora 0 20

# Zero-Shot Bactrian-X with Bloom 7B Ind
CUDA_VISIBLE_DEVICES=0 python main_nlg_prompt_batch.py eng bigscience/bloom-7b1---MBZUAI/bactrian-x-bloom-7b1-lora 0 20
CUDA_VISIBLE_DEVICES=1 python main_nlg_prompt_batch.py eng bigscience/bloom-7b1---haonan-li/bactrian-id-bloom-7b1-lora 0 20

# Zero-Shot aisingapore/sealion7b Ind & Eng
CUDA_VISIBLE_DEVICES=0 python main_nlg_prompt_batch.py ind aisingapore/sealion7b 8
CUDA_VISIBLE_DEVICES=1 python main_nlg_prompt_batch.py eng aisingapore/sealion7b 8

# Zero-Shot Merak-V4 Ind
CUDA_VISIBLE_DEVICES=0 python main_nlg_prompt_batch.py ind Ichsan2895/Merak-7B-v4 8
CUDA_VISIBLE_DEVICES=1 python main_nlg_prompt_batch.py eng Ichsan2895/Merak-7B-v4 8