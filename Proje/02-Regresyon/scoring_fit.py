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
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from statistics import mean 
from statistics import stdev 
from math import sqrt

price_mean = 66.15371335381349

# n çalıştırma sayısı, l train - test ayırma oranı
def calistir(n, l):
    df = pd.read_csv('House_Price_Prediction_challenge_edited.csv')

    sonuc_regr_r_squared = []
    sonuc_regr_rmse = []
    sonuc_regr_mae = []

    sonuc_regr2_r_squared = []
    sonuc_regr2_rmse = []
    sonuc_regr2_mae = []
    
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
    
        regr = RandomForestRegressor(max_depth=7, random_state=0)
        regr2 = GradientBoostingRegressor(random_state=0)
        
        regr.fit(train_x, train_y)
        regr2.fit(train_x, train_y)
    
        tahmin_regr = regr.predict( test_x )
        tahmin_regr2 = regr2.predict( test_x )
    
        test_x['tahmin_regr'] = tahmin_regr
        test_x['tahmin_regr2'] = tahmin_regr2
        
        test_x['gercek'] = test_y

        test_x['gosterilecek_tahmin_regr'] = price_mean + test_x['tahmin_regr']
        test_x['gosterilecek_tahmin_regr2'] = price_mean + test_x['tahmin_regr2']

        test_x['gosterilecek_gercek'] = price_mean + test_x['gercek']
        
        r_squared = r2_score(test_x['gosterilecek_gercek'], test_x['gosterilecek_tahmin_regr'])
        r_squared2 = r2_score(test_x['gosterilecek_gercek'], test_x['gosterilecek_tahmin_regr2'])

        rmse = sqrt(mean_squared_error(test_x['gosterilecek_gercek'], test_x['gosterilecek_tahmin_regr']))
        rmse2 = sqrt(mean_squared_error(test_x['gosterilecek_gercek'], test_x['gosterilecek_tahmin_regr2']))

        mae = mean_absolute_error(test_x['gosterilecek_gercek'], test_x['gosterilecek_tahmin_regr'])
        mae2 = mean_absolute_error(test_x['gosterilecek_gercek'], test_x['gosterilecek_tahmin_regr2'])

        sonuc_regr_r_squared.append(r_squared)
        sonuc_regr_rmse.append(rmse)
        sonuc_regr_mae.append(mae)   
        
        sonuc_regr2_r_squared.append(r_squared2)
        sonuc_regr2_rmse.append(rmse2)
        sonuc_regr2_mae.append(mae2)  
        
    return(sonuc_regr_r_squared, sonuc_regr_rmse, sonuc_regr_mae, sonuc_regr2_r_squared, sonuc_regr2_rmse, sonuc_regr2_mae)

        #test_x = test_x.drop(columns=['gercek', 'sonuc_regr','tahmin_regr'])
"""
    print('House_Price_Prediction_challenge_edited.csv isimli veri seti çalışılmıştır.')
    print('Her bir metot ile' ,n, 'adet fit işlemi yapılmıştır.')
    print('')
    print('RandomForestRegressor ile R Square sonuçları:' )  
    print('Ortalama değer ', "{:.5f}".format(mean(sonuc_regr_r_squared)))
    print('Standart sapma ',  "{:.5f}".format(stdev(sonuc_regr_r_squared)) )
    print('En yüksek değer ',  "{:.5f}".format(max(sonuc_regr_r_squared) ))
    print('En düşük değer ',  "{:.5f}".format(min(sonuc_regr_r_squared)) )
    print('')
    print('RandomForestRegressor ile Root Mean Square Error sonuçları:' )  
    print('Ortalama değer ', "{:.5f}".format(mean(sonuc_regr_rmse)))
    print('Standart sapma ',  "{:.5f}".format(stdev(sonuc_regr_rmse)) )
    print('En yüksek değer ',  "{:.5f}".format(max(sonuc_regr_rmse) ))
    print('En düşük değer ',  "{:.5f}".format(min(sonuc_regr_rmse)) )
    print('')
    print('RandomForestRegressor ile Mean Absolute Error sonuçları:' )  
    print('Ortalama değer ', "{:.5f}".format(mean(sonuc_regr_mae)))
    print('Standart sapma ',  "{:.5f}".format(stdev(sonuc_regr_mae)) )
    print('En yüksek değer ',  "{:.5f}".format(max(sonuc_regr_mae) ))
    print('En düşük değer ',  "{:.5f}".format(min(sonuc_regr_mae)) )
    print('')
    print('')
    print('GradientBoostingRegressor ile R Square sonuçları:' )  
    print('Ortalama değer ', "{:.5f}".format(mean(sonuc_regr2_r_squared)))
    print('Standart sapma ',  "{:.5f}".format(stdev(sonuc_regr2_r_squared)) )
    print('En yüksek değer ',  "{:.5f}".format(max(sonuc_regr2_r_squared) ))
    print('En düşük değer ',  "{:.5f}".format(min(sonuc_regr2_r_squared)) )
    print('')
    print('GradientBoostingRegressor ile Root Mean Square Error sonuçları:' )  
    print('Ortalama değer ', "{:.5f}".format(mean(sonuc_regr2_rmse)))
    print('Standart sapma ',  "{:.5f}".format(stdev(sonuc_regr2_rmse)) )
    print('En yüksek değer ',  "{:.5f}".format(max(sonuc_regr2_rmse) ))
    print('En düşük değer ',  "{:.5f}".format(min(sonuc_regr2_rmse)) )
    print('')
    print('GradientBoostingRegressor ile Mean Absolute Error sonuçları:' )  
    print('Ortalama değer ', "{:.5f}".format(mean(sonuc_regr2_mae)))
    print('Standart sapma ',  "{:.5f}".format(stdev(sonuc_regr2_mae)) )
    print('En yüksek değer ',  "{:.5f}".format(max(sonuc_regr2_mae) ))
    print('En düşük değer ',  "{:.5f}".format(min(sonuc_regr2_mae)) )
    print('')
"""

# calistir(5, 0.7)


