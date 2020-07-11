#!/usr/bin/env python
# coding: utf-8

# In[4]:


import Data_Scrapped
import re

def data_Cleaning():
    all_Para_Content = Data_Scrapped.data_scrapping()
    #Deleating [12][332] etc from paragraphs
    all_Para_Content_clean  = re.sub(r'\[[0-9]*\]', ' ', all_Para_Content)
    #Deleating extra space
    all_Para_Content_clean  = re.sub(r'\s+', ' ', all_Para_Content_clean)
    return all_Para_Content


# In[5]:




