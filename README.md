# DexBERT
Android Representation based on BERT

# Environment

  - Java 11.0.11
  - Python 3.7.11
  - numpy 1.19.5
  - torch 1.7.1
  - torchvision 0.8.2
  - ptflops 0.6.8
  - tensorflow 2.6.0
  - tensorboard 2.7.0
  - scikit-learn 1.0.2

# Usage

## AndroBERT PRe-training
  - Data preparation: ```python data4pretraining.py -d apk_dir -l apk_hash_list -cp cpu_number```

  - Start pre-training: ```sh pretrainDexBERT.sh```

  - Infer a pre-trained model: ```python InferBERT.py --model_cfg config_file_path --data_file pre-processed_data_file --model_file pre-trained_model_file --vocab vocabulary_path```

## Malicious Code Localization
Data preparation: 
  - First, download the APKs with link: 
  - Second, extract Smali instructions: ```python data4malice.py```

Training & Evaluation:
  - ```python MaliciousCodeLocalizarion.py```

## App defect detection
  - First, download the APKs with link: 
  - Second, extract Smali instructions: ```python data4defect.py```

Training & Evaluation:
  - ```python AppDefectDetection.py```

## compute model flops
  - ```python count_flops.py```