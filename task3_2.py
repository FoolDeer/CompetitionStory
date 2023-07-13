#!/usr/bin/env python
# coding: utf-8

# In[29]:


# 导入我们所需的库 as：即给库取别名，方便书写
import matplotlib
import numpy as np
import pandas as pd
from  matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.figure(figsize=(12,8))
detail1=pd.read_excel(r'E:\program\0.xls')
product_D=detail1['CreditScore']
product_B=detail1['Age']
detail=pd.read_excel(r'E:\program\1.xlsx')
product_C=detail['CreditScore']
product_A=detail['Age']
plt.scatter(product_B,product_D,marker="o")
plt.scatter(product_A,product_C,marker="o")
plt.ylabel('CreditScore')
plt.xlabel('Age')
plt.legend(["0","1"])
plt.title('3.2')


# In[ ]:




