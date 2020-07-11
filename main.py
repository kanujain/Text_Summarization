#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import heapq
import Sentence_Score

def main():
    sentence_scores = Sentence_Score.calc_sentence_score()
    Summary_MachineLearning = heapq.nlargest(10, sentence_scores, key=sentence_scores.get)
    print(Summary_MachineLearning)

if __name__ == "__main__":
    main()
    

