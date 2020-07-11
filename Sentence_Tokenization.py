#!/usr/bin/env python
# coding: utf-8

#Tokenisation of Sentences

import nltk
import Data_Cleaning

def sentence_tokenization():
    all_Para_Content_clean = Data_Cleaning.data_Cleaning()
    sentence_tokens = nltk.sent_tokenize(all_Para_Content_clean)
    return sentence_tokens





