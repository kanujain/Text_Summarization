#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import StopWord

def calc_freq_word():
    stopwords = StopWord.stop_word()
    word_frequencies = {}
    for word in word_tokens:
        if word not in stopwords:
            if word not in word_frequencies:
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

