# Zero-Shot mT0
CUDA_VISIBLE_DEVICES=0 python main_nlg_prompt_batch.py ind bigscience/mt0-small 0 128
CUDA_VISIBLE_DEVICES=0 python main_nlg_prompt_batch.py ind bigscience/mt0-base 0 64
CUDA_VISIBLE_DEVICES=0 python main_nlg_prompt_batch.py ind bigscience/mt0-large 0 32
CUDA_VISIBLE_DEVICES=0 python main_nlg_prompt_batch.py ind bigscience/mt0-xl 0 8
CUDA_VISIBLE_DEVICES=0 python main_nlg_prompt_batch.py ind bigscience/mt0-xxl 0 4

# Zero-Shot BLOOMZ
CUDA_VISIBLE_DEVICES=0 python main_nlg_prompt_batch.py ind bigscience/bloomz-560m 0 8
CUDA_VISIBLE_DEVICES=0 python main_nlg_prompt_batch.py ind bigscience/bloomz-1b1 0 6
CUDA_VISIBLE_DEVICES=0 python main_nlg_prompt_batch.py ind bigscience/bloomz-1b7 0 4
CUDA_VISIBLE_DEVICES=0 python main_nlg_prompt_batch.py ind bigscience/bloomz-3b 0 2
CUDA_VISIBLE_DEVICES=0 python main_nlg_prompt_batch.py ind bigscience/bloomz-7b 0 1
