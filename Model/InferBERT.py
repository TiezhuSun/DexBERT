# Copyright 2022 Tiezhu SUN, Kevin Allix.

"""Infer a pretrained model to check the prediction results of the two tasks (masked words prediction and next sentence prediction)."""

import models
import tokenization
import torch
import fire
import numpy as np

from pretrainBertAE import Preprocess4Pretrain, SentPairDataLoader, BertModel4Pretrain
from colorama import Fore, Style
from tokenization import DeTokenizer

import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]= "2"
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
 

def main(model_cfg='config/SentGen/bert_base.json',
         data_file='../tbc/books_large_all.txt',
         model_file=None,
         vocab='../uncased_L-12_H-768_A-12/vocab.txt',
         max_len=512,
         max_pred=20,
         mask_prob=0.15):

    model_cfg = models.Config.from_json(model_cfg)

    bs = 1

    tokenizer = tokenization.FullTokenizer(vocab_file=vocab, do_lower_case=True)
    tokenize = lambda x: tokenizer.tokenize(tokenizer.convert_to_unicode(x))

    pipeline = [Preprocess4Pretrain(max_pred,
                                    mask_prob,
                                    list(tokenizer.vocab.keys()),
                                    tokenizer.convert_tokens_to_ids,
                                    max_len)]
    data_iter = SentPairDataLoader(data_file,
                                   bs,
                                   tokenize,
                                   max_len,
                                   pipeline=pipeline)

    model = BertModel4Pretrain(model_cfg)
    model.load_state_dict(torch.load(model_file))
    model.to(device)
    model.eval()
    
    cnt = 0

    for batch in data_iter:
        batch = [t.to(device) for t in batch]
        with torch.no_grad(): # evaluation without gradient calculation
            input_ids, segment_ids, input_mask, masked_ids, masked_pos, masked_weights, is_next = batch

            logits_lm, logits_clsf = model(input_ids, segment_ids, input_mask, masked_pos)


            pred_token_ids = torch.argmax(logits_lm, dim=2)
            pred_token_ids = np.array(pred_token_ids.cpu()[0])
            masked_ids     = np.array(masked_ids.cpu()[0])
            correct_pos    = set(np.where(pred_token_ids == masked_ids)[0])
            pred_tokens    = DeTokenizer.convert_ids_to_tokens(pred_token_ids, DeTokenizer.read_dic_to_set(vocab))
            gt_tokens      = DeTokenizer.convert_ids_to_tokens(masked_ids, DeTokenizer.read_dic_to_set(vocab))

            print('Masked Words Prediction  : ', end='')
            for i, token in enumerate(pred_tokens):
                if i in correct_pos:
                    print(f'{Fore.GREEN}{token}{Style.RESET_ALL} ', end='')
                else:
                    print(f'{Fore.RED}{token}{Style.RESET_ALL} ', end='')

            print('')
            
            print('Masked Words ground truth: ', end='')
            for i, token in enumerate(gt_tokens):
                if i in correct_pos:
                    print(f'{Fore.GREEN}{token}{Style.RESET_ALL} ', end='')
                else:
                    print(token+' ', end='')

            print('')
            
            is_next_pred = bool(torch.argmax(logits_clsf, dim=1)[0])
            is_next_gt   = bool(is_next[0])

            if is_next_pred == is_next_gt:
                print(f'is_next prediction  : {Fore.GREEN}{is_next_pred}{Style.RESET_ALL}') 
                print(f'is_next ground truth: {Fore.GREEN}{is_next_gt}{Style.RESET_ALL}') 
            else:
                print(f'is_next prediction  : {Fore.RED}{is_next_pred}{Style.RESET_ALL}') 
                print(f'is_next ground truth: {is_next_gt}') 
            
            print('*-'*10)
                
            cnt += 1
            if cnt >= 10:
                break

if __name__ == '__main__':
    fire.Fire(main)
        