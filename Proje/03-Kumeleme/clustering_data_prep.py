#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 17:57:25 2024

@author: aliburhanguncan
"""

import pandas as pd
import numpy as np
import sys

df = pd.read_csv("Customers_org.csv")

# df.info()

df = df.dropna()

"""
İçeride 35 adet boş satır vardı, silindi.
Object olan iki sütun var: Gender, Profession
"""

df['Age_Group'] = pd.cut(df['Age'], bins=[0, 18, 25, 35, 45, 55, 65, float('inf')], labels=['Under 18', '18-24', '25-34', '35-44', '45-54', '55-64', '65+'])

df['Income_Group'] = pd.cut(df['Annual Income ($)'], bins=[0, 50000, 75000, 100000, 125000, 150000, 175000, float('inf')], labels=['Under 50k', '50-75k', '75-100k', '100-125k', '125-150k','150-175k','175k+'])

#for i in df.columns:
#    print(i,'\n',df[i].value_counts(),'\n')

df['Gender'] = df['Gender'].map({'Female': 1, 'Male': 0})

delete = ['CustomerID','Age','Annual Income ($)']
for i in delete:
    df = df.drop(columns = [i])
    
dummyler = ['Age_Group','Profession','Income_Group']
for i in dummyler:
    df = pd.get_dummies( df, columns=[ i ] )
    
df.to_csv("Customers_edited.csv",index=False)