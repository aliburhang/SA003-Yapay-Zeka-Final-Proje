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

from math import sqrt

def calistir():
    
    df = pd.read_csv('Customers_edited.csv')
    
    pca_10 = PCA(n_components=10)
    
    pca_2 = PCA(n_components=2)
    
    pca_10.fit(df)
    
    pca_2.fit(df)
    
    transformed_data_pca_10 = pca_10.transform(df)
    
    transformed_data_pca_2 = pca_2.transform(df)
    
    detransformed_data_pca_10 = pca_10.inverse_transform(transformed_data_pca_10)
    
    detransformed_data_pca_2 = pca_2.inverse_transform(transformed_data_pca_2)
    
    detransformed_data_pca_10 = detransformed_data_pca_10.round(0)
    
    detransformed_data_pca_2 = detransformed_data_pca_2.round(0)
    
    difference_matrix_pca_10 = df - detransformed_data_pca_10
    
    difference_matrix_pca_2 = df - detransformed_data_pca_2
    
    difference_matrix_pca_10 = abs(difference_matrix_pca_10)
    
    difference_matrix_pca_2 = abs(difference_matrix_pca_2)
    
    def square_root_of_squares(row):
        squares = row.apply(lambda x: x**2)
        sum_of_squares = squares.sum()
        return np.sqrt(sum_of_squares)
    
    df['Square_Root_of_Squares_pca_10'] = difference_matrix_pca_10.apply(square_root_of_squares, axis=1)
    
    df['Square_Root_of_Squares_pca_2'] = difference_matrix_pca_2.apply(square_root_of_squares, axis=1)
    
    msre_2 = df['Square_Root_of_Squares_pca_2'].mean()  
    
    msre_10 = df['Square_Root_of_Squares_pca_10'].mean()
 
    return(msre_2,msre_10)   
 
"""
    print("")
    print("Açıklama")
    print("")
    print("1. Kullanılan datada bir hedef sütun yoktur.")
    print("2. Burada PCA 2 ve 10 kümeli olacak şekilde çalıştırılmıştır.")
    print("3. Hata için şu şekilde bir modelleme yapılmıştır:")
    print("   3.1. Elde edilen PCA datası detransform edilmiştir.")
    print("   3.2. Detransform datası ile orjinal dataframein farkının mutlak değeri alınmıştır.")
    print("   3.3. Her bir satır için bu mutlak değerlerin karelerinin toplamının karekökü alınıp dataframein orjinal haline yeni sütunlar olarak eklenmiştir.")
    print("   3.4. Son durumda PCA'in 2 ve 10 kümeli hali için hatayı temsil eden yeni iki sütun oluşmuştur.")
    print("   3.5. Bu sütunların ortalaması da bu çalışmada hata olarak tanımlanmıştır.")
    print("")
    print("10 kümeli PCA için hata:", round(msre_10,4))
    print("2 kümeli PCA için hata:", round(msre_2,4))
    print("")
    print("Sistemde hata hesaplanırken detransform edilen datanın ve orjinal datanın sıralamaları önemli olduğu için shuffle yapılmamış ve sistem 1'den fazla kez itere edilecek şekilde kodlanmamıştır.")
"""
    
