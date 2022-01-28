export DATA_FILE=/home/tiezhu/work_space/AndroBert/dataset/dataset1/train/data/data_file.txt
export VOCAB_FILE=/home/tiezhu/work_space/AndroBert/dataset/dataset1/train/data/vocab.txt
export SAVE_DIR=../save_dir/BertAE
export LOG_DIR=../log_dir/BertAE

python pretrainBertAE.py \
    --train_cfg config/BertAE/pretrain.json \
    --model_cfg config/BertAE/bert_base.json \
    --data_file $DATA_FILE \
    --vocab $VOCAB_FILE \
    --save_dir $SAVE_DIR \
    --log_dir $LOG_DIR \
    --max_len 512 \
    --max_pred 20 \
    --mask_prob 0.15
