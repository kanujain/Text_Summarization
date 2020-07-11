#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nltk
import Data_Cleaning

def word_tokenization():
    all_Para_Content_clean = Data_Cleaning.data_Cleaning()
    word_tokens = nltk.sent_tokenize(all_Para_Content_clean)
    return word_tokens

