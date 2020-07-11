#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nltk
import Sentence_Tokenization

def calc_sentence_score:
    sentence_scores = {}
    sentence_tokens = Sentence_Tokenization.sentence_tokenization()
    for sentence in sentence_tokens:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in word_frequencies.keys():
                # if len(sentence.split(' ')) < 30:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_frequencies[word]
                else:
                    sentence_scores[sentence] += word_frequencies[word]
    
    return sentence_scores

