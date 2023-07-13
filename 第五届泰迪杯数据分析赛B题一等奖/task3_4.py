# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 10:32:49 2022

@author: lenovo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#3.4.1
# Data_1 = pd.read_excel("result1_2.xlsx")

# Data_1.insert(loc=11, column='Status', value='0')
# Data_1.insert(loc=12, column='AssetStage', value='0')

# Data_1['Status'] = np.where((Data_1['Tenure'] <= 3)&(Data_1['Tenure'] >= 0),'新客户',Data_1['Status'])
# Data_1['Status'] = np.where((Data_1['Tenure'] <= 6)&(Data_1['Tenure'] > 3),'稳定客户',Data_1['Status'])
# Data_1['Status'] = np.where((Data_1['Tenure'] > 6)&(Data_1['Tenure'] <= 100),'老客户',Data_1['Status'])

# Data_1['AssetStage'] = np.where((Data_1['Balance'] <= 50000)&(Data_1['Balance'] >= 0),'低资产',Data_1['AssetStage'])
# Data_1['AssetStage'] = np.where((Data_1['Balance'] <= 90000)&(Data_1['Balance'] > 50000),'中下资产',Data_1['AssetStage'])
# Data_1['AssetStage'] = np.where((Data_1['Balance'] > 90000)&(Data_1['Balance'] <= 120000),'中上资产',Data_1['AssetStage'])
# Data_1['AssetStage'] = np.where(Data_1['Balance'] > 120000,'高资产',Data_1['AssetStage'])

# Data_1.to_excel("result3.xlsx",index=None)

#3.4.2

Data_2 = pd.read_excel("result3.xlsx")
Sum_new_1 = 0
Sum_new_2 = 0
Sum_new_3 = 0
Sum_new_4 = 0
Sum_old_1 = 0
Sum_old_2 = 0
Sum_old_3 = 0
Sum_old_4 = 0
for i in range(len(Data_2.index)):
    if((Data_2['Exited'][i] == 0)&(Data_2['Status'][i] == "新客户")&(Data_2['AssetStage'][i] == "低资产")):
        Sum_new_1 = Sum_new_1 + 1
    if((Data_2['Exited'][i] == 0)&(Data_2['Status'][i] == "新客户")&(Data_2['AssetStage'][i] == "中下资产")):
        Sum_new_2 = Sum_new_2 + 1
    if((Data_2['Exited'][i] == 0)&(Data_2['Status'][i] == "新客户")&(Data_2['AssetStage'][i] == "中上资产")):
        Sum_new_3 = Sum_new_3 + 1
    if((Data_2['Exited'][i] == 0)&(Data_2['Status'][i] == "新客户")&(Data_2['AssetStage'][i] == "高资产")):
        Sum_new_4 = Sum_new_4 + 1
    if((Data_2['Exited'][i] == 0)&(Data_2['Status'][i] == "老客户")&(Data_2['AssetStage'][i] == "低资产")):
        Sum_old_1 = Sum_old_1 + 1
    if((Data_2['Exited'][i] == 0)&(Data_2['Status'][i] == "老客户")&(Data_2['AssetStage'][i] == "中下资产")):
        Sum_old_2 = Sum_old_2 + 1
    if((Data_2['Exited'][i] == 0)&(Data_2['Status'][i] == "老客户")&(Data_2['AssetStage'][i] == "中上资产")):
        Sum_old_3 = Sum_old_3 + 1
    if((Data_2['Exited'][i] == 0)&(Data_2['Status'][i] == "老客户")&(Data_2['AssetStage'][i] == "高资产")):
        Sum_old_4 = Sum_old_4 + 1

Data_3 = pd.read_excel("3.4.2.xlsx")
sns.set()
plt.rcParams['font.sans-serif']='SimHei'#设置中文显示，必须放在sns.set之后
np.random.seed(0)
uniform_data = np.array((Data_3["新客户"],Data_3["老客户"])) #设置二维矩阵
f, ax = plt.subplots(figsize=(9, 6))

#heatmap后第一个参数是显示值,vmin和vmax可设置右侧刻度条的范围,
#参数annot=True表示在对应模块中注释值
# 参数linewidths是控制网格间间隔
#参数cbar是否显示右侧颜色条，默认显示，设置为None时不显示
#参数cmap可调控热图颜色
sns.heatmap(uniform_data, ax=ax,vmin=100,vmax=1300,cmap='YlOrRd',annot=True,linewidths=2,cbar=True)

ax.set_title('热力图') #plt.title('热图'),均可设置图片标题
ax.set_ylabel('新老客户')  #设置纵轴标签
ax.set_xlabel('资产阶段')  #设置横轴标签

#设置坐标字体方向，通过rotation参数可以调节旋转角度
label_y = ax.get_yticklabels()
plt.setp(label_y, rotation=360, horizontalalignment='right')
label_x = ax.get_xticklabels()
plt.setp(label_x, rotation=45, horizontalalignment='right')

plt.show()