# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 14:03:22 2022

@author: lenovo
"""

import pandas as pd
import numpy as np

Data_1 = pd.read_excel("result3.xlsx")

Data_1.insert(loc=13, column='IsActiveStatus', value='0')
Data_1.insert(loc=14, column='IsActiveAssetStage', value='0')
Data_1.insert(loc=15, column='CrCardAssetStage', value='0')

Data_1['IsActiveStatus'] = np.where((Data_1['Status'] == "新客户")&(Data_1['IsActiveMember'] == 0),0,Data_1['IsActiveStatus'])
Data_1['IsActiveStatus'] = np.where((Data_1['Status'] == "稳定客户")&(Data_1['IsActiveMember'] == 0),1,Data_1['IsActiveStatus'])
Data_1['IsActiveStatus'] = np.where((Data_1['Status'] == "老客户")&(Data_1['IsActiveMember'] == 0),2,Data_1['IsActiveStatus'])
Data_1['IsActiveStatus'] = np.where((Data_1['Status'] == "新客户")&(Data_1['IsActiveMember'] == 1),3,Data_1['IsActiveStatus'])
Data_1['IsActiveStatus'] = np.where((Data_1['Status'] == "稳定客户")&(Data_1['IsActiveMember'] == 1),4,Data_1['IsActiveStatus'])
Data_1['IsActiveStatus'] = np.where((Data_1['Status'] == "老客户")&(Data_1['IsActiveMember'] == 1),5,Data_1['IsActiveStatus'])

Data_1['IsActiveAssetStage'] = np.where((Data_1['AssetStage'] == "低资产")&(Data_1['IsActiveMember'] == 0),0,Data_1['IsActiveAssetStage'])
Data_1['IsActiveAssetStage'] = np.where((Data_1['AssetStage'] == "中下资产")&(Data_1['IsActiveMember'] == 0),1,Data_1['IsActiveAssetStage'])
Data_1['IsActiveAssetStage'] = np.where((Data_1['AssetStage'] == "中上资产")&(Data_1['IsActiveMember'] == 0),2,Data_1['IsActiveAssetStage'])
Data_1['IsActiveAssetStage'] = np.where((Data_1['AssetStage'] == "高资产")&(Data_1['IsActiveMember'] == 0),3,Data_1['IsActiveAssetStage'])
Data_1['IsActiveAssetStage'] = np.where((Data_1['AssetStage'] == "低资产")&(Data_1['IsActiveMember'] == 1),6,Data_1['IsActiveAssetStage'])
Data_1['IsActiveAssetStage'] = np.where((Data_1['AssetStage'] == "中下资产")&(Data_1['IsActiveMember'] == 1),7,Data_1['IsActiveAssetStage'])
Data_1['IsActiveAssetStage'] = np.where((Data_1['AssetStage'] == "中上资产")&(Data_1['IsActiveMember'] == 1),8,Data_1['IsActiveAssetStage'])
Data_1['IsActiveAssetStage'] = np.where((Data_1['AssetStage'] == "高资产")&(Data_1['IsActiveMember'] == 1),9,Data_1['IsActiveAssetStage'])

Data_1['CrCardAssetStage'] = np.where((Data_1['AssetStage'] == "低资产")&(Data_1['HasCrCard'] == 0),0,Data_1['CrCardAssetStage'])
Data_1['CrCardAssetStage'] = np.where((Data_1['AssetStage'] == "中下资产")&(Data_1['HasCrCard'] == 0),2,Data_1['CrCardAssetStage'])
Data_1['CrCardAssetStage'] = np.where((Data_1['AssetStage'] == "中上资产")&(Data_1['HasCrCard'] == 0),2,Data_1['CrCardAssetStage'])
Data_1['CrCardAssetStage'] = np.where((Data_1['AssetStage'] == "高资产")&(Data_1['HasCrCard'] == 0),5,Data_1['CrCardAssetStage'])
Data_1['CrCardAssetStage'] = np.where((Data_1['AssetStage'] == "低资产")&(Data_1['HasCrCard'] == 1),6,Data_1['CrCardAssetStage'])
Data_1['CrCardAssetStage'] = np.where((Data_1['AssetStage'] == "中下资产")&(Data_1['HasCrCard'] == 1),7,Data_1['CrCardAssetStage'])
Data_1['CrCardAssetStage'] = np.where((Data_1['AssetStage'] == "中上资产")&(Data_1['HasCrCard'] == 1),9,Data_1['CrCardAssetStage'])
Data_1['CrCardAssetStage'] = np.where((Data_1['AssetStage'] == "高资产")&(Data_1['HasCrCard'] == 1),9,Data_1['CrCardAssetStage'])

Data_1.to_excel("result4.xlsx",index=None)