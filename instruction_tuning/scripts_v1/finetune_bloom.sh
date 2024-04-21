lang='af,ar,az,bn,cs,de,en,es,et,fa,fi,fr,gl,gu,he,hi,hr,id,it,ja,ka,kk,km,ko,lt,lv,mk,ml,mn,mr,my,ne,nl,pl,ps,pt,ro,ru,si,sl,sv,sw,ta,te,th,tl,tr,uk,ur,vi,xh,zh'
model_size='560m'
OMP_NUM_THREADS=32
WORLD_SIZE=4
CUDA_VISIBLE_DEVICES=0,1,2,3

torchrun --nnodes=1 --nproc_per_node=4 --master_port=1234 finetune.py \
    --model_name_or_path bigscience/bloom-${model_size} \
    --lang ${lang} \
    --output_dir output/cendol-bloom-${model_size} \
    --overwrite_output_dir \
    --learning_rate 3e-4 \
    --load_in_8bit \
    --per_device_train_batch_size 4 \
    --per_device_eval_batch_size 4 \
    --gradient_accumulation_steps 32 \
    --num_train_epochs 4 \
    --model_max_length 768 \
    --val_set_size 5000 \
    --save_steps 5000 \
    --eval_steps 5000 \
    --logging_steps 100 \
    --preprocessing_num_workers 32 \
    --dataloader_num_workers 4 \
    --use_lora False \
    --lora_r 128 \
    --lora_alpha 128 \
    --lora_dropout 0.05 \
    --lora_target_modules 'query_key_value' \
    --ddp_find_unused_parameters False \
    --save_total_limit 5 \
    --group_by_length \
    --report_to wandb \
    --wandb_project cendol \
    --run_name cendol-bloom-${model_size}
