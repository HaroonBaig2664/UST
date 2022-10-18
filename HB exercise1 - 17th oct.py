#!/usr/bin/env python
# coding: utf-8

# In[1]:


from enum import auto

from operator import truediv

from turtle import color

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

import warnings

warnings.filterwarnings('ignore')
from itertools import count




dict ={}

file  = open('constitution.txt')

counts = 0

files = file.read()




for words in files:

    if words in dict:

        dict[words] +=1

    else:

        dict[words] = 1    




#bar plot



#used by categorical, nominal

sns.set_style('whitegrid')

keys = dict.keys()

values = dict.values()

plt.bar(keys, values)
# auto_price['make'].value_counts().plot.bar(figsize = (15,7), color = 'orangered')

plt.show()


# In[ ]:





# In[ ]:




