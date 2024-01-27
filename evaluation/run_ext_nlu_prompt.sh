# Zero-Shot mT0 Ind
CUDA_VISIBLE_DEVICES=0 python main_ext_nlu_prompt_batch.py ind bigscience/mt0-small 256 &
CUDA_VISIBLE_DEVICES=0 python main_ext_nlu_prompt_batch.py ind bigscience/mt0-base 128 &
CUDA_VISIBLE_DEVICES=0 python main_ext_nlu_prompt_batch.py ind bigscience/mt0-large 64 &
CUDA_VISIBLE_DEVICES=0 python main_ext_nlu_prompt_batch.py ind bigscience/mt0-xl 32 &
CUDA_VISIBLE_DEVICES=0 python main_ext_nlu_prompt_batch.py ind bigscience/mt0-xxl 16 &

# Zero-Shot BLOOMZ Ind
CUDA_VISIBLE_DEVICES=1 python main_ext_nlu_prompt_batch.py ind bigscience/bloomz-560m 256 &
CUDA_VISIBLE_DEVICES=1 python main_ext_nlu_prompt_batch.py ind bigscience/bloomz-1b1 128 &
CUDA_VISIBLE_DEVICES=1 python main_ext_nlu_prompt_batch.py ind bigscience/bloomz-1b7 64 &
CUDA_VISIBLE_DEVICES=1 python main_ext_nlu_prompt_batch.py ind bigscience/bloomz-3b 32 &
CUDA_VISIBLE_DEVICES=1 python main_ext_nlu_prompt_batch.py ind bigscience/bloomz-7b1 16 &

# Zero-Shot mT0 Eng
CUDA_VISIBLE_DEVICES=2 python main_ext_nlu_prompt_batch.py eng bigscience/mt0-small 256 &
CUDA_VISIBLE_DEVICES=2 python main_ext_nlu_prompt_batch.py eng bigscience/mt0-base 128 &
CUDA_VISIBLE_DEVICES=2 python main_ext_nlu_prompt_batch.py eng bigscience/mt0-large 64 &
CUDA_VISIBLE_DEVICES=2 python main_ext_nlu_prompt_batch.py eng bigscience/mt0-xl 32 &
CUDA_VISIBLE_DEVICES=2 python main_ext_nlu_prompt_batch.py eng bigscience/mt0-xxl 16 &

# Zero-Shot BLOOMZ Eng
CUDA_VISIBLE_DEVICES=3 python main_ext_nlu_prompt_batch.py eng bigscience/bloomz-560m 256 &
CUDA_VISIBLE_DEVICES=3 python main_ext_nlu_prompt_batch.py eng bigscience/bloomz-1b1 128 &
CUDA_VISIBLE_DEVICES=3 python main_ext_nlu_prompt_batch.py eng bigscience/bloomz-1b7 64 &
CUDA_VISIBLE_DEVICES=3 python main_ext_nlu_prompt_batch.py eng bigscience/bloomz-3b 32 &
CUDA_VISIBLE_DEVICES=3 python main_ext_nlu_prompt_batch.py eng bigscience/bloomz-7b1 16 &

# Zero-Shot Bactrian-X with Bloom 7B Ind
CUDA_VISIBLE_DEVICES=0 python main_ext_nlu_prompt_batch.py ind bigscience/bloom-7b1---MBZUAI/bactrian-x-bloom-7b1-lora 16 &
CUDA_VISIBLE_DEVICES=0 python main_ext_nlu_prompt_batch.py ind bigscience/bloom-7b1---haonan-li/bactrian-id-bloom-7b1-lora 16 &

# Zero-Shot Bactrian-X with Bloom 7B Eng
CUDA_VISIBLE_DEVICES=0 python main_ext_nlu_prompt_batch.py eng bigscience/bloom-7b1---MBZUAI/bactrian-x-bloom-7b1-lora 16 &
CUDA_VISIBLE_DEVICES=0 python main_ext_nlu_prompt_batch.py eng bigscience/bloom-7b1---haonan-li/bactrian-id-bloom-7b1-lora 16 &

# Zero-Shot aisingapore/sealion7b Ind & Eng
CUDA_VISIBLE_DEVICES=0 python main_ext_nlu_prompt_batch.py ind aisingapore/sealion7b-instruct-nc 16 &
CUDA_VISIBLE_DEVICES=0 python main_ext_nlu_prompt_batch.py eng aisingapore/sealion7b-instruct-nc 16 &

# Zero-Shot Merak-V4 Eng & Ind
CUDA_VISIBLE_DEVICES=3 python main_ext_nlu_prompt_batch.py ind Ichsan2895/Merak-7B-v4 16 &
CUDA_VISIBLE_DEVICES=1 python main_ext_nlu_prompt_batch.py eng Ichsan2895/Merak-7B-v4 16 &

# Zero-Shot SeaLLM 7b & 13b Ind
CUDA_VISIBLE_DEVICES=1 python main_ext_nlu_prompt_batch.py ind SeaLLMs/SeaLLM-7B-Chat 16 &
CUDA_VISIBLE_DEVICES=5 python main_ext_nlu_prompt_batch.py ind SeaLLMs/SeaLLM-13B-Chat 16 & # CANNOT LAH NO WEIGHT AVAILABLE

# Zero-Shot SeaLLM 7b & 13b Eng
CUDA_VISIBLE_DEVICES=1 python main_ext_nlu_prompt_batch.py eng SeaLLMs/SeaLLM-7B-Chat 16 &
CUDA_VISIBLE_DEVICES=2 python main_ext_nlu_prompt_batch.py eng SeaLLMs/SeaLLM-13B-Chat 16 & # CANNOT LAH NO WEIGHT AVAILABLE

# Zero-Shot LLaMA2 7b & 13b Ind
CUDA_VISIBLE_DEVICES=3 python main_ext_nlu_prompt_batch.py ind meta-llama/Llama-2-7b-chat-hf 16 &
CUDA_VISIBLE_DEVICES=0 python main_ext_nlu_prompt_batch.py ind meta-llama/Llama-2-13b-chat-hf 16 &

# Zero-Shot LLaMA2 7b & 13b  eng
CUDA_VISIBLE_DEVICES=3 python main_ext_nlu_prompt_batch.py eng meta-llama/Llama-2-7b-chat-hf 16 &
CUDA_VISIBLE_DEVICES=1 python main_ext_nlu_prompt_batch.py eng meta-llama/Llama-2-13b-chat-hf 16 &

# # Zero-Shot Cendol V1 Ind
CUDA_VISIBLE_DEVICES=5 python main_ext_nlu_prompt_batch.py ind indonlp/cendol-mt5-small 16 &
CUDA_VISIBLE_DEVICES=5 python main_ext_nlu_prompt_batch.py ind indonlp/cendol-mt5-base 16 &
CUDA_VISIBLE_DEVICES=5 python main_ext_nlu_prompt_batch.py ind indonlp/cendol-mt5-large 16 &
CUDA_VISIBLE_DEVICES=5 python main_ext_nlu_prompt_batch.py ind indonlp/cendol-mt5-xl 16 &
CUDA_VISIBLE_DEVICES=5 python main_ext_nlu_prompt_batch.py ind indonlp/cendol-mt5-xxl-merged 16 &

# Zero-Shot Cendol V1 Eng
CUDA_VISIBLE_DEVICES=5 python main_ext_nlu_prompt_batch.py eng indonlp/cendol-mt5-small 16 &
CUDA_VISIBLE_DEVICES=5 python main_ext_nlu_prompt_batch.py eng indonlp/cendol-mt5-base 16 &
CUDA_VISIBLE_DEVICES=5 python main_ext_nlu_prompt_batch.py eng indonlp/cendol-mt5-large 16 &
CUDA_VISIBLE_DEVICES=5 python main_ext_nlu_prompt_batch.py eng indonlp/cendol-mt5-xl 16 &
CUDA_VISIBLE_DEVICES=5 python main_ext_nlu_prompt_batch.py eng indonlp/cendol-mt5-xxl-merged 16

CUDA_VISIBLE_DEVICES=4 python main_ext_nlu_prompt_batch.py ind indonlp/cendol-llama2-7b 16 &
CUDA_VISIBLE_DEVICES=4 python main_ext_nlu_prompt_batch.py eng indonlp/cendol-llama2-7b 16
CUDA_VISIBLE_DEVICES=4 python main_ext_nlu_prompt_batch.py ind indonlp/cendol-llama2-13b-merged 16
CUDA_VISIBLE_DEVICES=5 python main_ext_nlu_prompt_batch.py eng indonlp/cendol-llama2-13b-merged 16
