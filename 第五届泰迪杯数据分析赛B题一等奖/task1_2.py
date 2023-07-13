# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 09:02:22 2022

@author: lenovo
"""

import pandas as pd

Data_short = pd.read_excel("result1_1.xlsx")

# #由下到上 unemoloyed 0 technician 1 ... admin 10
# Data_short['job'].replace(regex=True,inplace=True,to_replace=r'unemployed',value=r'0')
# Data_short['job'].replace(regex=True,inplace=True,to_replace=r'technician',value=r'1')
# Data_short['job'].replace(regex=True,inplace=True,to_replace=r'student',value=r'2')
# Data_short['job'].replace(regex=True,inplace=True,to_replace=r'services',value=r'3')
# Data_short['job'].replace(regex=True,inplace=True,to_replace=r'self-employed',value=r'4')
# Data_short['job'].replace(regex=True,inplace=True,to_replace=r'retired',value=r'5')
# Data_short['job'].replace(regex=True,inplace=True,to_replace=r'management',value=r'6')
# Data_short['job'].replace(regex=True,inplace=True,to_replace=r'housemaid',value=r'7')
# Data_short['job'].replace(regex=True,inplace=True,to_replace=r'entrepreneur',value=r'8')
# Data_short['job'].replace(regex=True,inplace=True,to_replace=r'blue-collar',value=r'9')
# Data_short['job'].replace(regex=True,inplace=True,to_replace=r'admin.',value=r'10')
# #single 0 married 1 divorced 2
# Data_short['marital'].replace(regex=True,inplace=True,to_replace=r'single',value=r'0')
# Data_short['marital'].replace(regex=True,inplace=True,to_replace=r'married',value=r'1')
# Data_short['marital'].replace(regex=True,inplace=True,to_replace=r'divorced',value=r'2')
# # illiterate 0 junior college 1 high school 2 undergraduate 3 postgraduate 4
# Data_short['education'].replace(regex=True,inplace=True,to_replace=r'illiterate',value=r'0')
# Data_short['education'].replace(regex=True,inplace=True,to_replace=r'junior college',value=r'1')
# Data_short['education'].replace(regex=True,inplace=True,to_replace=r'high school',value=r'2')
# Data_short['education'].replace(regex=True,inplace=True,to_replace=r'undergraduate',value=r'3')
# Data_short['education'].replace(regex=True,inplace=True,to_replace=r'postgraduate',value=r'4')
# # no 0 yes 1
# Data_short['default'].replace(regex=True,inplace=True,to_replace=r'no',value=r'0')
# Data_short['default'].replace(regex=True,inplace=True,to_replace=r'yes',value=r'1')
# # no 0 yes 1
# Data_short['housing'].replace(regex=True,inplace=True,to_replace=r'no',value=r'0')
# Data_short['housing'].replace(regex=True,inplace=True,to_replace=r'yes',value=r'1')
# # no 0 yes 1
# Data_short['loan'].replace(regex=True,inplace=True,to_replace=r'no',value=r'0')
# Data_short['loan'].replace(regex=True,inplace=True,to_replace=r'yes',value=r'1')
# #telephone 1 cellular 0
# Data_short['contact'].replace(regex=True,inplace=True,to_replace=r'telephone',value=r'0')
# Data_short['contact'].replace(regex=True,inplace=True,to_replace=r'cellular',value=r'1')
# #jan 1 feb 2 ... dec 12
# Data_short['month'].replace(regex=True,inplace=True,to_replace=r'jan',value=r'1')
# Data_short['month'].replace(regex=True,inplace=True,to_replace=r'feb',value=r'2')
# Data_short['month'].replace(regex=True,inplace=True,to_replace=r'mar',value=r'3')
# Data_short['month'].replace(regex=True,inplace=True,to_replace=r'apr',value=r'4')
# Data_short['month'].replace(regex=True,inplace=True,to_replace=r'may',value=r'5')
# Data_short['month'].replace(regex=True,inplace=True,to_replace=r'jun',value=r'6')
# Data_short['month'].replace(regex=True,inplace=True,to_replace=r'jul',value=r'7')
# Data_short['month'].replace(regex=True,inplace=True,to_replace=r'aug',value=r'8')
# Data_short['month'].replace(regex=True,inplace=True,to_replace=r'sep',value=r'9')
# Data_short['month'].replace(regex=True,inplace=True,to_replace=r'oct',value=r'10')
# Data_short['month'].replace(regex=True,inplace=True,to_replace=r'nov',value=r'11')
# Data_short['month'].replace(regex=True,inplace=True,to_replace=r'dec',value=r'12')
# #mon 1 tue 2 ... fri 5
# Data_short['day_of_week'].replace(regex=True,inplace=True,to_replace=r'mon',value=r'1')
# Data_short['day_of_week'].replace(regex=True,inplace=True,to_replace=r'tue',value=r'2')
# Data_short['day_of_week'].replace(regex=True,inplace=True,to_replace=r'wed',value=r'3')
# Data_short['day_of_week'].replace(regex=True,inplace=True,to_replace=r'thu',value=r'4')
# Data_short['day_of_week'].replace(regex=True,inplace=True,to_replace=r'fri',value=r'5')
# #failure 0 nonexistent 1 success 2
# Data_short['poutcome'].replace(regex=True,inplace=True,to_replace=r'failure',value=r'0')
# Data_short['poutcome'].replace(regex=True,inplace=True,to_replace=r'nonexistent',value=r'1')
# Data_short['poutcome'].replace(regex=True,inplace=True,to_replace=r'success',value=r'2')
# # no 0 yes 1
# Data_short['y'].replace(regex=True,inplace=True,to_replace=r'no',value=r'0')
# Data_short['y'].replace(regex=True,inplace=True,to_replace=r'yes',value=r'1')




# Data_short.to_excel("result1_3.xlsx",index=None)