#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Import necessary libraries
import numpy as np


# In[15]:


#Import the FAA (Federal Aviation Authority) dataset
import pandas as pd
exercise = pd.read_csv('assignment.csv')
display(exercise)


# In[16]:


#View the dataset shape
exercise.shape


# In[17]:


exercise.head()


# In[18]:


#View all the columns present in the dataset
exercise.columns


# In[22]:


#Create a new dataframe with only the required columns
df_analyze_dataframe = exercise[['ACFT_MAKE_NAME','LOC_STATE_NAME','ACFT_MODEL_NAME','RMK_TEXT',
                                       'FLT_PHASE','EVENT_TYPE_DESC','FATAL_FLAG']]


# In[23]:


#View the type of the object
type(df_analyze_dataframe)


# In[24]:


#Check if the dataframe contains all the required attributes
df_analyze_dataframe.head()


# In[25]:


#Replace all Fatal Flag missing values with the required output
df_analyze_dataframe['FATAL_FLAG'].fillna(value = 'No',inplace = True)


# In[26]:


#Verify if the missing values are replaced
df_analyze_dataframe.head()


# In[27]:


#Check the number of observations
df_analyze_dataframe.shape


# In[28]:


#Drop the unwanted values/observations from the dataset
df_final_dataset = df_analyze_dataframe.dropna(subset = ['ACFT_MAKE_NAME'])


# In[29]:


#Check the number of observations now to compare it with the original dataset and see how many values have been dropped
df_final_dataset.shape


# In[30]:


#Group the dataset by aircraft name
aircraftType = df_final_dataset.groupby('ACFT_MAKE_NAME')


# In[31]:


#View the number of times each aircraft type appears in the dataset (Hint: use the size() method)
aircraftType.size()


# In[32]:


#Group the dataset by fatal flag
fatalAccident = df_final_dataset.groupby('FATAL_FLAG')


# In[33]:


#View the total number of fatal and non-fatal accidents
fatalAccident.size()


# In[37]:


#K Create a new dataframe to view only the fatal accidents (Fatal Flag values = Yes)
accidents_with_fatality = fatalAccident.get_group('Yes')


# In[36]:


#L
accidents_with_fatality


# In[ ]:




