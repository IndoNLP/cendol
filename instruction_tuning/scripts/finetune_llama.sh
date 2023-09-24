OMP_NUM_THREADS=32
WORLD_SIZE=1
# CUDA_VISIBLE_DEVICES=0,1,2,3
HF_HOME=/home/jovyan/.cache/huggingface
HUGGINGFACE_HUB_CACHE=/home/jovyan/.cache/huggingface/hub
TRANSFORMERS_CACHE=/home/jovyan/.cache/huggingface/hub
HF_DATASETS_CACHE=/home/jovyan/.cache/huggingface/datasets
CUDA_VISIBLE_DEVICES=0,1,2,3

model_size='7b'
batch_size=1
grad_accum=32
torchrun --nproc_per_node=1 --master_port=1234 finetune.py \
    --model_name_or_path meta-llama/Llama-2-${model_size}-hf \
    --output_dir output/cendol-llama2-${model_size}-hf \
    --overwrite_output_dir \
    --learning_rate 2e-5 \
    --fp16 \
    --fsdp "full_shard auto_wrap" \
    --fsdp_config configs/fsdp_config.json \
    --per_device_train_batch_size ${batch_size} \
    --per_device_eval_batch_size ${batch_size} \
    --gradient_accumulation_steps ${grad_accum} \
    --num_train_epochs 3 \
    --model_max_length 768 \
    --sample_size 15000 \
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
    --lora_target_modules 'q_proj,v_proj' \
    --ddp_find_unused_parameters False \
    --save_total_limit 3 \
    --group_by_length \
    --report_to wandb \
    --wandb_project cendol \
    --run_name cendol-llama2-${model_size}-lr2e-5
#     --torch_compile \
