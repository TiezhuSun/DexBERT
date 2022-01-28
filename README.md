# AndroBERT
Android Representation based on BERT

# Usage
Data pre-processing for pre-taining a BertAE model: ```python pretrain_preprocessing.py -d apk_dir -l hash_list -cp cpu_number```

Start pre-training a BertAE model: ```sh pretrainBertAE.sh```

Infer a pre-trained BertAE model: ```python InferBertAE.py --model_cfg config_file_path --data_file pre-processed_data_file --model_file pre-trained_model_file --vocab vocabulary_path```


