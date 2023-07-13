#!/usr/bin/env python
# coding: utf-8

# In[3]:


# -*- coding: utf-8 -*-
import numpy as np  
import matplotlib.mlab as mlab  
import matplotlib.pyplot as plt  
labels=["blue-collar","student","Other job"]
X=[5670,609,24166]  
 
fig = plt.figure()
plt.pie(X,labels=labels,autopct='%1.2f%%') #画饼图（数据，数据对应的标签，百分数保留两位小数点）
plt.title("short blue-collar and student")
plt.show()  
plt.savefig("3.jpg")


# In[ ]:


import numpy as np  
import matplotlib.mlab as mlab  
import matplotlib.pyplot as plt  
labels=["blue-collar","student","Other job"]
X=[5670,609,24166]  
 
fig = plt.figure()
plt.pie(X,labels=labels,autopct='%1.2f%%') #画饼图（数据，数据对应的标签，百分数保留两位小数点）
plt.title("short blue-collar and student")
plt.show()  
plt.savefig("3.jpg")

