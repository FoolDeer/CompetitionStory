#!/usr/bin/env python
# coding: utf-8

# In[48]:


import matplotlib
import numpy as np
import pandas as pd
from  matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.figure(figsize=(12,8))
detail=pd.read_excel(r'E:\program\0(0).xlsx')
a=detail['age']
b=detail['percent']
detail1=pd.read_excel(r'E:\program\1(1).xlsx')
c=detail1['age']
d=detail1['percent']
#通用设置
matplotlib.rc('axes', facecolor = 'white')
matplotlib.rc('figure', figsize = (6, 4))
matplotlib.rc('axes', grid = False)
#数据及线属性
plt.plot(a, b,'*:r')
plt.plot(c, d,'*:b')
plt.legend(["0","1"])
#标题设置
plt.title('Condition of loss')
plt.xlabel('age')
plt.ylabel('proportion')


# In[42]:


import matplotlib
import numpy as np
import pandas as pd
from  matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.figure(figsize=(12,8))
detail=pd.read_excel(r'E:\program\1(1).xlsx')
a=detail['age']
b=detail['percent']
#通用设置
matplotlib.rc('axes', facecolor = 'white')
matplotlib.rc('figure', figsize = (6, 4))
matplotlib.rc('axes', grid = False)
#数据及线属性
plt.plot(a, b,'*:r')
#标题设置
plt.title('3.1')
plt.xlabel('age')
plt.ylabel('Condition of loss')


# In[ ]:




