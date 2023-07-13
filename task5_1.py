# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 15:57:46 2022

@author: lenovo
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

train_data = pd.read_excel("YC.xls")

# 列出对生存结果有影响的字段
predictors = ["IsActiveStatus", "IsActiveAssetStage", "CrCardAssetStage"]
# 存放不同参数取值，以及对应的精度，每一个元素都是一个三元组(a, b, c)
results = []
# 最小叶子结点的参数取值
sample_leaf_options = list(range(1, 500, 3))
# 决策树个数参数取值
n_estimators_options = list(range(1, 1000, 5))
groud_truth = train_data['Exited'][601:]

for leaf_size in sample_leaf_options:
    for n_estimators_size in n_estimators_options:
        alg = RandomForestClassifier(min_samples_leaf=leaf_size, n_estimators=n_estimators_size, random_state=50)
        alg.fit(train_data[predictors][:600], train_data['Exited'][:600])
        predict = alg.predict(train_data[predictors][601:])
        # 用一个三元组，分别记录当前的 min_samples_leaf，n_estimators， 和在测试数据集上的精度
        results.append((leaf_size, n_estimators_size, (groud_truth == predict).mean()))
        # 真实结果和预测结果进行比较，计算准确率
        print((groud_truth == predict).mean())

# 打印精度最大的那一个三元组
print(max(results, key=lambda x: x[2]))



