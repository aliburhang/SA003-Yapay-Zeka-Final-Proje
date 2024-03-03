#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 11:34:30 2024

@author: aliburhanguncan
"""

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import sys
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

df = pd.read_csv("House_Price_Prediction_challenge_org.csv")

# df.info()

"""
İçeride boş data yok.
Object olan üç sütun var: POSTED_BY, BHK_OR_RK, ADDRESS
TARGET(PRICE_IN_LACS) hedef sütunu ve adını Y yapalım.
"""

df.rename(columns = {'TARGET(PRICE_IN_LACS)':'Y'}, inplace = True) 

# Y'nin Range'i çok geniş, + - anomalileri çıkaralım.

# print(df.describe())
q1 = df['Y'].quantile(0.25)
q3 = df['Y'].quantile(0.75)
iqr = q3 - q1
iqr = iqr * 1.5
alt_limit = q1 - iqr
ust_limit = q3 + iqr

df = df[df['Y'] >= alt_limit]
df = df[df['Y'] <= ust_limit]

#: Tekrardan shuffle yapalim
df = df.sample(frac = 1.0)

#: Ortalama fiyati alıp, sonuçlardan çıkaralım. Daha dar bir aralıkta tahmin yapabilmek için.
price_mean = df['Y'].mean()

df['Y'] = df['Y'] - price_mean

# print(df['POSTED_BY'].value_counts())

# smoking_history 6 adet var. Sayıca çok eşit olmasalar da dummy indexe çok uzak değil. Dummy index yapılabilir.

df = pd.get_dummies( df, columns=[ 'POSTED_BY' ] )

# print(df['BHK_OR_RK'].value_counts())

# Bu sütun için type of property deniyor. Fakat RK'nın oranı aşırı derecede az. 

# ortalama_BHK = df[df['BHK_OR_RK'] == 'BHK']['Y'].mean()
# ortalama_RK = df[df['BHK_OR_RK'] == 'RK']['Y'].mean()

# Sadece RK ve sadece BHK olanların Y sütunu ortalamalarına bakıldı. Çok bir fark yok aralarında. Bu sütun siliniyor.

df = df.drop(columns=['BHK_OR_RK'])

# ADDRESS sütununun virgülden önceki değerleri daha lokal sonraki değerleri Şehir gibi. Sütun ',' ile ayrılığ value countlarına bakılacak. 

# Öncesinde karışıklık olma olasılığını azaltmak için çift virgüllü ve boşluklu durumlar kaldırılacak.

df['ADDRESS'] = df['ADDRESS'].str.replace(" ","")
df['ADDRESS'] = df['ADDRESS'].str.replace(",,",",")

df['LOCAL'] = df['ADDRESS'].str.split(',').str.get(0)
df['CITY'] = df['ADDRESS'].str.split(',').str.get(1)

df = df.drop(columns=['ADDRESS'])

# LOCAL içinde de CITY içinde de çok fazla değer mevcut. Target average bunlar için en uygunu olabilir.

city_prices = {}
for s in df['CITY'].unique():
    city_prices[ s ] = df[ df['CITY'] == s ]['Y'].mean()

df['CITY_PRICE'] = df['CITY'].map( city_prices )
df = df.drop(columns=['CITY'])

local_prices = {}
for s in df['LOCAL'].unique():
    local_prices[ s ] = df[ df['LOCAL'] == s ]['Y'].mean()

df['LOCAL_PRICE'] = df['LOCAL'].map( local_prices )
df = df.drop(columns=['LOCAL'])

# Dataları kontrol ederken SQUARE_FT sütununda çok yüksek gerçek dışı değerler olduğunu görüyoruz. Bu sütuna da bir üst limit tanımlaması yapılacak.

q1 = df['SQUARE_FT'].quantile(0.25)
q3 = df['SQUARE_FT'].quantile(0.75)
iqr = q3 - q1
iqr = iqr * 1.5
ust_limit = q3 + iqr

df = df[df['SQUARE_FT'] <= ust_limit]

# Sayısal olmayan değer kalmadı. Şimdi LONGITUDE ve LATITUDE ne yapabileceğimize bakalım.

"""
#* Sadece koordinatlari aldik
coords = df[['LONGITUDE', 'LATITUDE']]
#* Scale ettik
scaler = MinMaxScaler()
scaler.fit(coords)
scaled = scaler.transform(coords)
#* Kumelendirdik
kmeans = KMeans(n_clusters=10, random_state=0, n_init="auto")
kmeans.fit(scaled)
#* Her bir satirdaki veriyi, hangi cluster'a ait diye yaziyoruz
df['cluster_index'] = kmeans.predict( scaled )

for c in df.groupby(by = ['cluster_index']):
    print(c[0], len(c[1]))

print(df['LONGITUDE'].corr(df['Y']))
print(df['LATITUDE'].corr(df['Y']))

print(df['cluster_index'].corr(df['Y']))

İlk olarak gruplandırmaya çalıştık fakat gruplandırma sonucu korelasyon her seferinde değişken geldiği için olduğu gibi bırakmaya karar verdim.
"""

"""
# Aşağıda 5% altında korelasyona sahip olanlar PCA ile birleştirildi, fakat birleşimde 5%'yi geçmedi.
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

df.to_csv("House_Price_Prediction_challenge_edited.csv",index=False)


