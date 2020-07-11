#!/usr/bin/env python
# coding: utf-8


import nltk
import Sentence_Tokenization
import Word_Frequency

def calc_sentence_score:
    sentence_scores = {}
    sentence_tokens = Sentence_Tokenization.sentence_tokenization()
    word_frequencies = Word_Frequency.calc_freq_word()
    for sentence in sentence_tokens:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in word_frequencies.keys():
                if len(sentence.split(' ')) < 30:
                    if sentence not in sentence_scores:
                        sentence_scores[sentence] = word_frequencies[word]
                    else:
                        sentence_scores[sentence] += word_frequencies[word]
    
    return sentence_scores

