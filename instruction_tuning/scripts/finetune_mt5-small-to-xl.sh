OMP_NUM_THREADS=32
WORLD_SIZE=4
# CUDA_VISIBLE_DEVICES=0,1,2,3
HF_HOME=/home/jovyan/.cache/huggingface
HUGGINGFACE_HUB_CACHE=/home/jovyan/.cache/huggingface/hub
TRANSFORMERS_CACHE=/home/jovyan/.cache/huggingface/hub
HF_DATASETS_CACHE=/home/jovyan/.cache/huggingface/datasets

# SMALL
model_size='small'
batch_size=32
grad_accum=1
torchrun --nproc_per_node=4 --master_port=1234 finetune_seq2seq.py \
    --model_name_or_path google/mt5-${model_size} \
    --output_dir output/cendol-mt5-${model_size} \
    --overwrite_output_dir \
    --learning_rate 3e-4 \
    --bf16 \
    --fsdp "full_shard auto_wrap" \
    --fsdp_config configs/fsdp_config.json \
    --per_device_train_batch_size ${batch_size} \
    --per_device_eval_batch_size ${batch_size} \
    --gradient_accumulation_steps ${grad_accum} \
    --num_train_epochs 3 \
    --source_max_length 512 \
    --model_max_length 768 \
    --sample_size 6005000 \
    --val_set_size 5000 \
    --save_steps 5000 \
    --eval_steps 5000 \
    --logging_steps 100 \
    --preprocessing_num_workers 64 \
    --dataloader_num_workers 32 \
    --use_lora False \
    --lora_r 64 \
    --lora_alpha 16 \
    --lora_dropout 0.05 \
    --lora_target_modules 'q,v' \
    --ddp_find_unused_parameters False \
    --save_total_limit 3 \
    --group_by_length \
    --report_to wandb \
    --wandb_project cendol \
    --run_name cendol-mt5-${model_size}

#     --torch_compile \

# BASE
model_size='base'
batch_size=16
grad_accum=2
torchrun --nproc_per_node=4 --master_port=1234 finetune_seq2seq.py \
    --model_name_or_path google/mt5-${model_size} \
    --output_dir output/cendol-mt5-${model_size} \
    --overwrite_output_dir \
    --learning_rate 3e-4 \
    --bf16 \
    --fsdp "full_shard auto_wrap" \
    --fsdp_config configs/fsdp_config.json \
    --per_device_train_batch_size ${batch_size} \
    --per_device_eval_batch_size ${batch_size} \
    --gradient_accumulation_steps ${grad_accum} \
    --num_train_epochs 3 \
    --source_max_length 512 \
    --model_max_length 768 \
    --sample_size 6005000 \
    --val_set_size 5000 \
    --save_steps 5000 \
    --eval_steps 5000 \
    --logging_steps 100 \
    --preprocessing_num_workers 64 \
    --dataloader_num_workers 32 \
    --use_lora False \
    --lora_r 64 \
    --lora_alpha 16 \
    --lora_dropout 0.05 \
    --lora_target_modules 'q,v' \
    --ddp_find_unused_parameters False \
    --save_total_limit 3 \
    --group_by_length \
    --report_to wandb \
    --wandb_project cendol \
    --run_name cendol-mt5-${model_size}

# LARGE
model_size='large'
batch_size=8
grad_accum=4
torchrun --nproc_per_node=4 --master_port=1234 finetune_seq2seq.py \
    --model_name_or_path google/mt5-${model_size} \
    --output_dir output/cendol-mt5-${model_size} \
    --overwrite_output_dir \
    --learning_rate 3e-4 \
    --bf16 \
    --fsdp "full_shard auto_wrap" \
    --fsdp_config configs/fsdp_config.json \
    --per_device_train_batch_size ${batch_size} \
    --per_device_eval_batch_size ${batch_size} \
    --gradient_accumulation_steps ${grad_accum} \
    --num_train_epochs 3 \
    --source_max_length 512 \
    --model_max_length 768 \
    --sample_size 6005000 \
    --val_set_size 5000 \
    --save_steps 5000 \
    --eval_steps 5000 \
    --logging_steps 100 \
    --preprocessing_num_workers 64 \
    --dataloader_num_workers 32 \
    --use_lora False \
    --lora_r 64 \
    --lora_alpha 16 \
    --lora_dropout 0.05 \
    --lora_target_modules 'q,v' \
    --ddp_find_unused_parameters False \
    --save_total_limit 3 \
    --group_by_length \
    --report_to wandb \
    --wandb_project cendol \
    --run_name cendol-mt5-${model_size}

# XL
model_size='xl'
batch_size=2
grad_accum=16
torchrun --nproc_per_node=4 --master_port=1234 finetune_seq2seq.py \
    --model_name_or_path google/mt5-${model_size} \
    --output_dir output/cendol-mt5-${model_size} \
    --overwrite_output_dir \
    --learning_rate 3e-4 \
    --bf16 \
    --fsdp "full_shard auto_wrap" \
    --fsdp_config configs/fsdp_config.json \
    --per_device_train_batch_size ${batch_size} \
    --per_device_eval_batch_size ${batch_size} \
    --gradient_accumulation_steps ${grad_accum} \
    --num_train_epochs 3 \
    --source_max_length 512 \
    --model_max_length 768 \
    --sample_size 6005000 \
    --val_set_size 5000 \
    --save_steps 5000 \
    --eval_steps 5000 \
    --logging_steps 100 \
    --preprocessing_num_workers 64 \
    --dataloader_num_workers 32 \
    --use_lora False \
    --lora_r 64 \
    --lora_alpha 16 \
    --lora_dropout 0.05 \
    --lora_target_modules 'q,v' \
    --ddp_find_unused_parameters False \
    --save_total_limit 3 \
    --group_by_length \
    --report_to wandb \
    --wandb_project cendol \
    --run_name cendol-mt5-${model_size}
