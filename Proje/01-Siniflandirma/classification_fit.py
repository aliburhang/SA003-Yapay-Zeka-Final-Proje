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
from sklearn.neural_network import MLPClassifier  
from sklearn.tree import DecisionTreeClassifier 
from statistics import mean 
from statistics import stdev 
import os

currentFile = os.getcwd()


# n çalıştırma sayısı, l train - test ayırma oranı
def calistir(n, l):
    df = pd.read_csv('diabetes_prediction_dataset_edited.csv')

    sonuc_clf = []
    sonuc_dtc = []
    
    for i in range(n):
        #: Rasgele sirala
        df = df.sample(frac = 1.0)
        
        #: Train/test ayir
        limit = int(l * len(df))
        
        train = df[:limit]
        test = df[limit:]
        
        #: Girdi - Cikti olarak ayir
        train_y = train['Y']
        train_x = train.drop(columns = ['Y'])
    
        test_y = test['Y']
        test_x = test.drop(columns = ['Y'])
    
        clf = MLPClassifier(random_state=1, max_iter=7)
        dtc = DecisionTreeClassifier()
        
        clf.fit(train_x, train_y)
        dtc.fit(train_x, train_y)
    
        tahmin_clf = clf.predict( test_x )
        tahmin_dtc = dtc.predict( test_x )
    
        test_x['tahmin_clf'] = tahmin_clf
        test_x['tahmin_dtc'] = tahmin_dtc
        
        test_x['gercek'] = test_y
    
        test_x['sonuc_clf'] = test_x['tahmin_clf'] == test_x['gercek']
        test_x['sonuc_dtc'] = test_x['tahmin_dtc'] == test_x['gercek']
    
        sonuc_MLPClassifier = test_x['sonuc_clf'].mean()
        sonuc_DecisionTreeClassifier = test_x['sonuc_dtc'].mean()
        
        sonuc_clf.append(sonuc_MLPClassifier)
        sonuc_dtc.append(sonuc_DecisionTreeClassifier)
            
        test_x = test_x.drop(columns=['gercek', 'sonuc_clf', 'sonuc_dtc','tahmin_clf', 'tahmin_dtc'])
    
    return(sonuc_clf, sonuc_dtc)

"""
    print('diabetes_prediction_dataset_edited.csv isimli veri seti çalışılmıştır.')
    print('Her bir metot ile' ,n, 'adet fit işlemi yapılmıştır.')
    print('')
    print('MLPClassifier doğruluk oranları:' )  
    print('Ortalama değer ', "{:.5f}".format(mean(sonuc_clf)))
    print('Standart sapma ',  "{:.5f}".format(stdev(sonuc_clf)) )
    print('En yüksek değer ',  "{:.5f}".format(max(sonuc_clf) ))
    print('En düşük değer ',  "{:.5f}".format(min(sonuc_clf)) )
    print('')
    print('DecisionTreeClassifier doğruluk oranları:' )
    print('Ortalama değer ',  "{:.5f}".format(mean(sonuc_dtc) ))
    print('Standart sapma ',  "{:.5f}".format(stdev(sonuc_dtc) ))
    print('En yüksek değer ',  "{:.5f}".format(max(sonuc_dtc) ))
    print('En düşük değer ',  "{:.5f}".format(min(sonuc_dtc)))
"""

#calistir(5, 0.7")


