# AndroBERT
Android Representation based on BERT

For BERT part, we are strongly inspired by and borrowed some parts from  https://github.com/dhlee347/pytorchic-bert

# Usage

## AndroBERT PRe-training
Data preparation: ```python data4pretraining.py -d apk_dir -l apk_hash_list -cp cpu_number```

Start pre-training: ```sh pretrainBertAE.sh```

Infer a pre-trained model: ```python InferBertAE.py --model_cfg config_file_path --data_file pre-processed_data_file --model_file pre-trained_model_file --vocab vocabulary_path```

## Malicious Code Localization
Data preparation: 
  - First, download the APKs with link: 
  - Second, extract Smali instructions: ```python data4malice.py```

## App defect detection
  - First, download the APKs with link: 
  - Second, extract Smali instructions: ```python data4defect.py```



