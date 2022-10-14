#!/usr/bin/env python
# coding: utf-8

# In[56]:


#a.	Read data from csv file fire department of New York City (FDNY)
#b.	View content of the data

import pandas as pd
df = pd.read_csv('FDNY.csv')
display(df)


# In[13]:


#	View first five records
Exercise.head()


# In[57]:


#d.	Skip the first row from dataset
df = pd.read_csv('FDNY.csv',skiprows=1)


# In[22]:


#e.	View first five records from fixed dataset
df.head()


# In[26]:


#g.	Display columns of the dataset
df.columns


# In[29]:


#h.	View index of dataset
df.index


# In[49]:


#k.	Show size of FDNY information for each borough.
df['Borough'].value_counts()


# In[46]:


df.info()


# In[50]:


#j.	Find the total number of fire department facilities in each borough.
df.groupby(['Borough']).describe()


# In[51]:


#i.	Find the total number of fire department facilities in New York city
df['FacilityName'].unique().size


# In[52]:


#datatypes
df.dtypes


# In[54]:


#M
df.dropna(inplace = True)


# In[55]:


df


# In[ ]:




