OMP_NUM_THREADS=32
WORLD_SIZE=8
HF_HOME=/home/users/nus/hlovenia/scratch/.cache/huggingface
HUGGINGFACE_HUB_CACHE=/home/users/nus/hlovenia/scratch/.cache/huggingface/hub
TRANSFORMERS_CACHE=/home/users/nus/hlovenia/scratch/.cache/huggingface/hub
HF_DATASETS_CACHE=/home/users/nus/hlovenia/scratch/.cache/huggingface/datasets

huggingface-cli login --token $HF_TOKEN

wandb login --verify $WANDB_API_KEY

# 3B Full Fine-Tuning
model_size='3b'
batch_size=32
grad_accum=1
CUDA_VISIBLE_DEVICES="0,1" accelerate launch finetune_sealion.py \
    --model_name_or_path aisingapore/sealion${model_size} \
    --output_dir output/cendol-sealion-${model_size} \
    --overwrite_output_dir \
    --learning_rate 2e-5 \
    --bf16 \
    --per_device_train_batch_size ${batch_size} \
    --per_device_eval_batch_size ${batch_size} \
    --gradient_accumulation_steps ${grad_accum} \
    --num_train_epochs 3 \
    --model_max_length 768 \
    --sample_size 6005000 \
    --val_set_size 5000 \
    --save_steps 5000 \
    --eval_steps 5000 \
    --logging_steps 100 \
    --preprocessing_num_workers 64 \
    --dataloader_num_workers 64 \
    --gradient_checkpointing \
    --use_lora False \
    --lora_r 128 \
    --lora_alpha 128 \
    --lora_dropout 0.05 \
    --lora_target_modules 'q_proj,v_proj' \
    --ddp_find_unused_parameters False \
    --torch_compile \
    --save_total_limit 3 \
    --group_by_length \
    --report_to wandb \
    --wandb_project cendol \
    --run_name cendol-sealion-${model_size} | tee ./logs/scripts_v1_cendol-sealion-${model_size}