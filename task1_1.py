# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 08:22:46 2022

@author: lenovo
"""

import pandas as pd
# #1.1.1
# Data_short = pd.read_csv("short-customer-data.csv")


# #丢弃缺失值 dropna()删除缺失值所在行(axis=0)或列(axis=1) 默认为 axis=0
# Data_short = Data_short.dropna()


# #去重
# Data_short.drop_duplicates(subset=['user_id'],keep='first',inplace=True)


# Data_short.to_excel("result1_1.xlsx",index=None)


# #1.1.2
Data_long = pd.read_csv("long-customer-train.csv")

#删除数值为-1、0 和“-”的异常值
Data_long = Data_long[~Data_long['Age'].isin(['-1'])]
Data_long = Data_long[~Data_long['Age'].isin(['0'])]
Data_long = Data_long[~Data_long['Age'].isin(['-'])]
# 删除空格和“岁”等异常字符
Data_long['Age'].replace('\s+','',regex=True,inplace=True) 
Data_long['Age'].replace(regex=True,inplace=True,to_replace=r'岁',value=r'')

Data_long['Age'] = Data_long['Age'].astype(int)
# print(Data_long['Age'].dtype)
# Data_long.to_excel("result1_2.xlsx",index=None)