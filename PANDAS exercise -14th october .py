from enum import auto
from itertools import count
from operator import truediv
from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


datas = pd.read_csv(r'C:\Users\arbazalx\OneDrive - Intel Corporation\Desktop\javasc\flames website\FDNY.csv')


## 1 viewing content of data
print(datas)

## 2 view firt 5 records
print(datas.head(6))  

## 3 skipping first row and print 5 data sets
print(datas.iloc[1:6 ,  1:])
# print(datas,skiprows=1)

## 4 show statistics 
print(datas.count)
## 5 displaying row index
print(datas.index)

## 6 pandas accessing columns

print(datas.columns) ## ADDING COLUMN NAME IN string

print(datas['Borough'].value_counts())



#show datatypes of each columns
print(datas.dtypes)



# find the total number of facilities

print(datas['FacilityName'].value_counts())

## finding total number of fire department facilities in nyc
# fd_nyc = (datas.loc[:,"LOC_STATE_NAME"] == "New York" )
# countt = 0
# for i in fd_nyc:
#     if i == True:
#         count +=1
# print(countt)    

## finding total number of fire department facilities in all newyork
# fd_all = (datas.loc[:,"LOC_STATE_NAME"])
# print(fd_all.count())


# show size of fdny for each borough

print(datas.groupby(['Borough']).size())

# view fdny information for each borough

print(datas.groupby(['Borough']).describe())

 # replacing nan
# print(datas.dropna(inplace = True))



# describe gives stats unique top freq count
