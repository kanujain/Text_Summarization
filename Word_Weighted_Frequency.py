#!/usr/bin/env python
# coding: utf-8

import Word_Frequency

def calc_weighted_freq():
    word_frequencies = Word_Frequency.calc_freq_word()
    maximum_freq_word = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_freq_word)
    return word_frequencies






