OMP_NUM_THREADS=32
WORLD_SIZE=8
HF_HOME=/home/users/nus/hlovenia/scratch/.cache/huggingface
HUGGINGFACE_HUB_CACHE=/home/users/nus/hlovenia/scratch/.cache/huggingface/hub
TRANSFORMERS_CACHE=/home/users/nus/hlovenia/scratch/.cache/huggingface/hub
HF_DATASETS_CACHE=/home/users/nus/hlovenia/scratch/.cache/huggingface/datasets

huggingface-cli login --token $HF_TOKEN

wandb login --verify $WANDB_API_KEY
wandb enabled

# 7B Full Fine-Tuning
model_size='7b'
batch_size=4
grad_accum=8
CUDA_VISIBLE_DEVICES=2,3,4,5,6,7 accelerate launch finetune_sealion.py \
    --model_name_or_path /home/holylovenia/projects/indo-t0/instruction_tuning/output/cendol-sealion-7b/checkpoint-30000 \
    --output_dir output_v2/cendol-sealion-${model_size}-chat \
    --overwrite_output_dir \
    --learning_rate 1e-5 \
    --data_path indonlp/nusa_t2t_v2 \
    --bf16 \
    --per_device_train_batch_size ${batch_size} \
    --per_device_eval_batch_size ${batch_size} \
    --gradient_accumulation_steps ${grad_accum} \
    --eval_accumulation_steps ${grad_accum} \
    --num_train_epochs 1 \
    --model_max_length 1024 \
    --val_set_size 5000 \
    --save_steps 5000 \
    --eval_steps 5000 \
    --logging_steps 100 \
    --preprocessing_num_workers 16 \
    --dataloader_num_workers 16 \
    --gradient_checkpointing \
    --use_lora False \
    --lora_r 128 \
    --lora_alpha 128 \
    --lora_dropout 0.05 \
    --lora_target_modules 'q_proj,v_proj' \
    --ddp_find_unused_parameters False \
    --torch_compile \
    --save_total_limit 2 \
    --group_by_length \
    --report_to wandb \
    --wandb_project cendol-v2 \
    --run_name cendol-sealion-${model_size}-chat
# | tee ./logs/scripts_v2_cendol-sealion-${model_size}