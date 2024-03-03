#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 17:45:42 2024

@author: aliburhanguncan
"""
import tkinter as tk
from tkinter import messagebox
import scoring_fit
from statistics import mean 
from statistics import stdev 
import os
from pathlib import Path
from datetime import datetime

def hesapla():
    try:
        # Get input values from entry widgets
        analiz_num = int(analiz_entry.get())
        oran_num = float(oran_entry.get())
        
        if 1 <= analiz_num <= 100:
            analiz_num = analiz_num
        else:
            messagebox.showerror("Error", "Analiz sayısı 1 ile 100 arasında bir sayı olamlı.")
            
        if 0.1 <= oran_num <= 0.9:
            oran_num = oran_num
        else:
            messagebox.showerror("Error", "Train oranı 0.1 ile 0.9 arasında bir sayı olmalı.")
            
        (sonuc_regr_r_squared, sonuc_regr_rmse, sonuc_regr_mae, sonuc_regr2_r_squared, sonuc_regr2_rmse, sonuc_regr2_mae) = scoring_fit.calistir(analiz_num, oran_num)
        
        mean_sonuc_regr_r_squared = "{:.5f}".format(mean(sonuc_regr_r_squared))
        stddev_sonuc_regr_r_squared = "{:.5f}".format(stdev(sonuc_regr_r_squared))
        max_sonuc_regr_r_squared = "{:.5f}".format(max(sonuc_regr_r_squared))
        min_sonuc_regr_r_squared = "{:.5f}".format(min(sonuc_regr_r_squared))
        
        mean_sonuc_regr_rmse = "{:.5f}".format(mean(sonuc_regr_rmse))
        stddev_sonuc_regr_rmse = "{:.5f}".format(stdev(sonuc_regr_rmse))
        max_sonuc_regr_rmse = "{:.5f}".format(max(sonuc_regr_rmse))
        min_sonuc_regr_rmse = "{:.5f}".format(min(sonuc_regr_rmse))
        
        mean_sonuc_regr_mae = "{:.5f}".format(mean(sonuc_regr_mae))
        stddev_sonuc_regr_mae = "{:.5f}".format(stdev(sonuc_regr_mae))
        max_sonuc_regr_mae = "{:.5f}".format(max(sonuc_regr_mae))
        min_sonuc_regr_mae = "{:.5f}".format(min(sonuc_regr_mae))
        
        mean_sonuc_regr2_r_squared = "{:.5f}".format(mean(sonuc_regr2_r_squared))
        stddev_sonuc_regr2_r_squared = "{:.5f}".format(stdev(sonuc_regr2_r_squared))
        max_sonuc_regr2_r_squared = "{:.5f}".format(max(sonuc_regr2_r_squared))
        min_sonuc_regr2_r_squared = "{:.5f}".format(min(sonuc_regr2_r_squared))
        
        mean_sonuc_regr2_rmse = "{:.5f}".format(mean(sonuc_regr2_rmse))
        stddev_sonuc_regr2_rmse = "{:.5f}".format(stdev(sonuc_regr2_rmse))
        max_sonuc_regr2_rmse = "{:.5f}".format(max(sonuc_regr2_rmse))
        min_sonuc_regr2_rmse = "{:.5f}".format(min(sonuc_regr2_rmse))
        
        mean_sonuc_regr2_mae = "{:.5f}".format(mean(sonuc_regr2_mae))
        stddev_sonuc_regr2_mae = "{:.5f}".format(stdev(sonuc_regr2_mae))
        max_sonuc_regr2_mae = "{:.5f}".format(max(sonuc_regr2_mae))
        min_sonuc_regr2_mae = "{:.5f}".format(min(sonuc_regr2_mae))
        
        explanation = f"""
        House_Price_Prediction_challenge_edited.csv isimli veri seti çalışılmıştır.
        Her bir metot ile {analiz_num} adet fit işlemi yapılmıştır.
        
        RandomForestRegressor ile R Square sonuçları:
        Ortalama değer {mean_sonuc_regr_r_squared}
        Standart sapma {stddev_sonuc_regr_r_squared}
        En yüksek değer {max_sonuc_regr_r_squared}
        En düşük değer {min_sonuc_regr_r_squared}
        
        RandomForestRegressor ile Root Mean Square Error sonuçları:
        Ortalama değer {mean_sonuc_regr_rmse}
        Standart sapma {stddev_sonuc_regr_rmse}
        En yüksek değer {max_sonuc_regr_rmse}
        En düşük değer {min_sonuc_regr_rmse}
        
        RandomForestRegressor ile Mean Absolute Error sonuçları:
        Ortalama değer {mean_sonuc_regr_mae}
        Standart sapma {stddev_sonuc_regr_mae}
        En yüksek değer {max_sonuc_regr_mae}
        En düşük değer {min_sonuc_regr_mae}
        
        GradientBoostingRegressor ile R Square sonuçları:
        Ortalama değer {mean_sonuc_regr2_r_squared}
        Standart sapma {stddev_sonuc_regr2_r_squared}
        En yüksek değer {max_sonuc_regr2_r_squared}
        En düşük değer {min_sonuc_regr2_r_squared}
        
        GradientBoostingRegressor ile Root Mean Square Error sonuçları:
        Ortalama değer {mean_sonuc_regr2_rmse}
        Standart sapma {stddev_sonuc_regr2_rmse}
        En yüksek değer {max_sonuc_regr2_rmse}
        En düşük değer {min_sonuc_regr2_rmse}
        
        GradientBoostingRegressor ile Mean Absolute Error sonuçları:
        Ortalama değer {mean_sonuc_regr2_mae}
        Standart sapma {stddev_sonuc_regr2_mae}
        En yüksek değer {max_sonuc_regr2_mae}
        En düşük değer {min_sonuc_regr2_mae}
        """

        explanation_window = tk.Toplevel(root)
        explanation_window.title("Sonuçlar")
        explanation_window.geometry("600x600")

        explanation_text = tk.Text(explanation_window, wrap="word")
        explanation_text.insert(tk.END, explanation)
        explanation_text.pack(expand=True, fill="both")
        
        current_dir = os.getcwd() 
        upper_dir = Path(current_dir).parent.absolute()
        
        now = datetime.now()
        
        with open(str(upper_dir) + "/log_file.txt", "a") as file:
            file.write("House_Price_Prediction_challenge_edited.csv isimli veri seti " + str(now) +" tarih ve saatinde RandomForestRegressor ve GradientBoostingRegressor ile çalışılmıştır. \n")
        file.close()
    except ValueError:
        messagebox.showerror("Error", "Geçerli değerler giriniz.")
        
root = tk.Tk()
root.title("Regresyon sayfası")
root.geometry("400x300")

analiz_label = tk.Label(root, text="Analiz sayısını giriniz. (1 ile 100 arası olmalı)")
analiz_label.pack()

analiz_entry = tk.Entry(root)
analiz_entry.pack()

oran_label = tk.Label(root, text="Train oranını giriniz. (0.1 ile 0.9 arası olmalı)")
oran_label.pack()

oran_entry = tk.Entry(root)
oran_entry.pack()

# Create button to trigger calculation
calculate_button = tk.Button(root, text="Hesapla", command=hesapla)
calculate_button.pack()

# Run the main event loop
root.mainloop()