# DexBERT
Effective, Task-Agnostic and Fine-grained Representation Learning of Android Bytecode

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

## Instruction
  -  For most users, if you just want to use a pre-trained DexBERT to generate class features for your own Android analysis tasks, please skip the pretraining stage and download our pre-trained DexBERT model using the link provided below.
  
  - For readers who want to replicate our experiments, please follow the steps below to pre-train a DexBERT model and apply it in malicious code localization and app defect detection.

  - Please find some smali examples for malicious code localization and app defect detection in the folder './examples'.

## DexBERT Pre-training
  - Data preparation: 
    - First, find apk hash list at: ```Data/data/pretraining_apks.txt```
    - Second, download and process APKs: ```python data4pretraining.py -d apk_dir -l apk_hash_list -cp cpu_number```

  - Start pre-training: 
    - ```sh pretrainDexBERT.sh```

  - Infer a pre-trained model: 
    - ```python InferBERT.py --model_cfg config_file_path --data_file pre-processed_data_file --model_file pre-trained_model_file --vocab vocabulary_path```
  
  - Download our pre-trained DexBERT model with this link: https://drive.google.com/file/d/1z6aZQXT1dS6wX1JgPnWJVS_e6Td2sBPg/view?usp=sharing

## Malicious Code Localization
  - Data preparation: 
    - First, download APKs and ground-truth with link: https://sites.google.com/view/mkldroid/dataset-and-results
    - Second, extract Smali instructions: ```python data4malice.py```

  - Training & Evaluation:
    - ```python MaliciousCodeLocalization.py```

## App Defect Detection
  - Data preparation:
    - First, download the APKs with link: https://github.com/breezedong/DNN-based-software-defect-prediction; labels for defective smali files are provided in ```Data/data/defect_labels```
    - Second, extract Smali instructions and generate sample list: ```python data4defect.py```

  - Training & Evaluation:
    - ```python AppDefectDetection.py```

## Compute Model Flops
  - ```python count_flops.py```