lang='af,ar,az,bn,cs,de,en,es,et,fa,fi,fr,gl,gu,he,hi,hr,id,it,ja,ka,kk,km,ko,lt,lv,mk,ml,mn,mr,my,ne,nl,pl,ps,pt,ro,ru,si,sl,sv,sw,ta,te,th,tl,tr,uk,ur,vi,xh,zh'
model_size='small'
OMP_NUM_THREADS=32
WORLD_SIZE=1
CUDA_VISIBLE_DEVICES=0,1,2,3
TRANSFORMERS_CACHE=/home/jovyan/.cache/huggingface
HF_HOME=/home/jovyan/.cache/huggingface

torchrun --nproc_per_node=4 --master_port=1234 finetune_seq2seq.py \
--model_name_or_path google/mt5-${model_size} \
--lang ${lang} \
--output_dir output/cendol-mt5-${model_size}-X-lora \
--overwrite_output_dir \
--learning_rate 3e-4 \
--fp16 \
--sharded_ddp zero_dp_3 \
--per_device_train_batch_size 128 \
--per_device_eval_batch_size 128 \
--gradient_accumulation_steps 1 \
--num_train_epochs 1 \
--source_max_length 512 \
--model_max_length 512 \
--val_set_size 5000 \
--save_steps 5000 \
--eval_steps 5000 \
--logging_steps 100 \
--preprocessing_num_workers 32 \
--dataloader_num_workers 8 \
--use_lora False \
--lora_r 64 \
--lora_alpha 16 \
--lora_dropout 0.05 \
--lora_target_modules 'q,v' \
--ddp_find_unused_parameters False \
--save_total_limit 5 \
--group_by_length \
--report_to wandb \
--wandb_project cendol \
--run_name cendol-mt5-${model_size}-X
