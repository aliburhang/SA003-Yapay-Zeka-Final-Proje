#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 15:18:58 2024

@author: aliburhanguncan
"""

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import sys

df = pd.read_csv("diabetes_prediction_dataset_org.csv")

# df.info()

"""
İçeride boş data yok.
Object olan iki sütun var: gender ve smoking_history
diabetes hedef sütunu ve adını Y yapalım.
"""

df.rename(columns = {'diabetes':'Y'}, inplace = True) 

#print(df['gender'].value_counts())

# gender içinde 18 adet other var silinebilir. Geri kalanlar 1-0 map yapılabilir.

df = df.loc[df["gender"] != 'Other' ]

df['gender'] = df['gender'].map({'Female': 1, 'Male': 0})

# print(df['smoking_history'].value_counts())

# smoking_history 6 adet var. Sayıca da yüksekler. Dummy index yapılabilir.

df = pd.get_dummies( df, columns=[ 'smoking_history' ] )

# Diğer sütunlarda tekil değer kaldımı kontrol edelim.

names = ['age', 'hypertension', 'heart_disease', 'bmi', 'HbA1c_level', 'blood_glucose_level']

# for i in names:
#    print(i, '\n',df[i].value_counts(), '\n')

#print("Y ile Age", df['age'].corr( df['y'] ))

#for i in df:
    #print(i, df[i].corr( df['Y']), '\n')
    
    
"""
Aşağıda 5% altında korelasyona sahip olanlar PCA ile birleştirildi, fakat birleşimde 5%'yi geçmedi.
delete = []
for c in df:
    corr = abs(df[c].corr(df['Y']))
    if corr < 0.05:
        delete.append( c )
        print(c, corr)
        
print(delete)
pca = PCA(n_components=1)
pca.fit( df[ delete ] )
df['PCA'] = pca.transform( df[delete] )

for c in delete:
    del df[c]
    
print(df['PCA'].corr(df['Y']))
"""

""" Fakat sistemde genel olarak yüksek korelasyonlu sütunlar mevcut. 5% altındakiler silinip fit işlemine gidilecek."""

for i in df:
    if df[i].corr(df['Y']) < 0.05:
        del df[i]

# Datanın son halini yazalım.

df.to_csv("diabetes_prediction_dataset_edited.csv",index=False)
