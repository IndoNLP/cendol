lang='af,ar,az,bn,cs,de,en,es,et,fa,fi,fr,gl,gu,he,hi,hr,id,it,ja,ka,kk,km,ko,lt,lv,mk,ml,mn,mr,my,ne,nl,pl,ps,pt,ro,ru,si,sl,sv,sw,ta,te,th,tl,tr,uk,ur,vi,xh,zh'
model_size='560m'
WORLD_SIZE=2
CUDA_VISIBLE_DEVICES=0,1

torchrun --nproc_per_node=2 --master_port=1234 finetune.py \
--model_name_or_path bigscience/bloom-${model_size} \
--lang ${lang} \
--output_dir output/cendol-bloom-${model_size} \
--overwrite_output_dir \
--learning_rate 2e-5 \
--fp16 \
--per_device_train_batch_size 8 \
--per_device_eval_batch_size 8 \
--gradient_accumulation_steps 4 \
--num_train_epochs 4 \
--model_max_length 768 \
--val_set_size 5000 \
--save_steps 5000 \
--eval_steps 5000 \
--logging_steps 100 \
--preprocessing_num_workers 32 \
--dataloader_num_workers 4 \
--use_lora False \
--lora_r 64 \
--lora_alpha 16 \
--lora_dropout 0.05 \
--lora_target_modules 'query_key_value' \
--ddp_find_unused_parameters False \
--save_total_limit 5 \
--group_by_length \
--report_to wandb \
--wandb_project cendol \
--run_name cendol-bloom-${model_size}
