# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 16:00:35 2022

@author: lenovo
"""

import pandas as pd
import numpy as np

# 3.4.1
Data_1 = pd.read_csv("long-customer-test.csv")

Data_1.insert(loc=10, column='Status', value='0')
Data_1.insert(loc=11, column='AssetStage', value='0')

Data_1['Status'] = np.where((Data_1['Tenure'] <= 3)&(Data_1['Tenure'] >= 0),'新客户',Data_1['Status'])
Data_1['Status'] = np.where((Data_1['Tenure'] <= 6)&(Data_1['Tenure'] > 3),'稳定客户',Data_1['Status'])
Data_1['Status'] = np.where((Data_1['Tenure'] > 6)&(Data_1['Tenure'] <= 100),'老客户',Data_1['Status'])

Data_1['AssetStage'] = np.where((Data_1['Balance'] <= 50000)&(Data_1['Balance'] >= 0),'低资产',Data_1['AssetStage'])
Data_1['AssetStage'] = np.where((Data_1['Balance'] <= 90000)&(Data_1['Balance'] > 50000),'中下资产',Data_1['AssetStage'])
Data_1['AssetStage'] = np.where((Data_1['Balance'] > 90000)&(Data_1['Balance'] <= 120000),'中上资产',Data_1['AssetStage'])
Data_1['AssetStage'] = np.where(Data_1['Balance'] > 120000,'高资产',Data_1['AssetStage'])

Data_1.to_excel("result_test.xlsx",index=None)

Data_2 = pd.read_excel("result_test.xlsx")

Data_2.insert(loc=12, column='IsActiveStatus', value='0')
Data_2.insert(loc=13, column='IsActiveAssetStage', value='0')
Data_2.insert(loc=14, column='CrCardAssetStage', value='0')

Data_2['IsActiveStatus'] = np.where((Data_2['Status'] == "新客户")&(Data_2['IsActiveMember'] == 0),0,Data_2['IsActiveStatus'])
Data_2['IsActiveStatus'] = np.where((Data_2['Status'] == "稳定客户")&(Data_2['IsActiveMember'] == 0),1,Data_2['IsActiveStatus'])
Data_2['IsActiveStatus'] = np.where((Data_2['Status'] == "老客户")&(Data_2['IsActiveMember'] == 0),2,Data_2['IsActiveStatus'])
Data_2['IsActiveStatus'] = np.where((Data_2['Status'] == "新客户")&(Data_2['IsActiveMember'] == 1),3,Data_2['IsActiveStatus'])
Data_2['IsActiveStatus'] = np.where((Data_2['Status'] == "稳定客户")&(Data_2['IsActiveMember'] == 1),4,Data_2['IsActiveStatus'])
Data_2['IsActiveStatus'] = np.where((Data_2['Status'] == "老客户")&(Data_2['IsActiveMember'] == 1),5,Data_2['IsActiveStatus'])

Data_2['IsActiveAssetStage'] = np.where((Data_2['AssetStage'] == "低资产")&(Data_2['IsActiveMember'] == 0),0,Data_2['IsActiveAssetStage'])
Data_2['IsActiveAssetStage'] = np.where((Data_2['AssetStage'] == "中下资产")&(Data_2['IsActiveMember'] == 0),1,Data_2['IsActiveAssetStage'])
Data_2['IsActiveAssetStage'] = np.where((Data_2['AssetStage'] == "中上资产")&(Data_2['IsActiveMember'] == 0),2,Data_2['IsActiveAssetStage'])
Data_2['IsActiveAssetStage'] = np.where((Data_2['AssetStage'] == "高资产")&(Data_2['IsActiveMember'] == 0),3,Data_2['IsActiveAssetStage'])
Data_2['IsActiveAssetStage'] = np.where((Data_2['AssetStage'] == "低资产")&(Data_2['IsActiveMember'] == 1),6,Data_2['IsActiveAssetStage'])
Data_2['IsActiveAssetStage'] = np.where((Data_2['AssetStage'] == "中下资产")&(Data_2['IsActiveMember'] == 1),7,Data_2['IsActiveAssetStage'])
Data_2['IsActiveAssetStage'] = np.where((Data_2['AssetStage'] == "中上资产")&(Data_2['IsActiveMember'] == 1),8,Data_2['IsActiveAssetStage'])
Data_2['IsActiveAssetStage'] = np.where((Data_2['AssetStage'] == "高资产")&(Data_2['IsActiveMember'] == 1),9,Data_2['IsActiveAssetStage'])

Data_2['CrCardAssetStage'] = np.where((Data_2['AssetStage'] == "低资产")&(Data_2['HasCrCard'] == 0),0,Data_2['CrCardAssetStage'])
Data_2['CrCardAssetStage'] = np.where((Data_2['AssetStage'] == "中下资产")&(Data_2['HasCrCard'] == 0),2,Data_2['CrCardAssetStage'])
Data_2['CrCardAssetStage'] = np.where((Data_2['AssetStage'] == "中上资产")&(Data_2['HasCrCard'] == 0),2,Data_2['CrCardAssetStage'])
Data_2['CrCardAssetStage'] = np.where((Data_2['AssetStage'] == "高资产")&(Data_2['HasCrCard'] == 0),5,Data_2['CrCardAssetStage'])
Data_2['CrCardAssetStage'] = np.where((Data_2['AssetStage'] == "低资产")&(Data_2['HasCrCard'] == 1),6,Data_2['CrCardAssetStage'])
Data_2['CrCardAssetStage'] = np.where((Data_2['AssetStage'] == "中下资产")&(Data_2['HasCrCard'] == 1),7,Data_2['CrCardAssetStage'])
Data_2['CrCardAssetStage'] = np.where((Data_2['AssetStage'] == "中上资产")&(Data_2['HasCrCard'] == 1),9,Data_2['CrCardAssetStage'])
Data_2['CrCardAssetStage'] = np.where((Data_2['AssetStage'] == "高资产")&(Data_2['HasCrCard'] == 1),9,Data_2['CrCardAssetStage'])

Data_2.to_excel("result_test处理.xlsx",index=None)