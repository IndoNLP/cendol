CUDA_VISIBLE_DEVICES=0 python main_nlu_prompt_batch.py ind bigscience/mt0-small 32 &
CUDA_VISIBLE_DEVICES=1 python main_nlu_prompt_batch.py ind bigscience/mt0-base 16 &
CUDA_VISIBLE_DEVICES=2 python main_nlu_prompt_batch.py ind bigscience/mt0-large 8 &
# CUDA_VISIBLE_DEVICES=0 python main_nlu_prompt_batch.py ind bigscience/mt0-xl 4
# CUDA_VISIBLE_DEVICES=0 python main_nlu_prompt_batch.py ind bigscience/mt0-xxl 2

CUDA_VISIBLE_DEVICES=3 python main_nlu_prompt_batch.py ind bigscience/bloomz-560m 16 &

wait
wait
wait

CUDA_VISIBLE_DEVICES=0 python main_nlu_prompt_batch.py ind bigscience/bloomz-1b1 8 &
CUDA_VISIBLE_DEVICES=1 python main_nlu_prompt_batch.py ind bigscience/bloomz-1b7 6 &
CUDA_VISIBLE_DEVICES=2 python main_nlu_prompt_batch.py ind bigscience/bloomz-3b 4 &
# CUDA_VISIBLE_DEVICES=0 python main_nlu_prompt_batch.py ind bigscience/bloomz-7b 2
