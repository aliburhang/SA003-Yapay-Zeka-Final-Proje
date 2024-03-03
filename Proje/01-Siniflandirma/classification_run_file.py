#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 17:45:42 2024

@author: aliburhanguncan
"""
import tkinter as tk
from tkinter import messagebox
import classification_fit
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
            
        MLPClassifier, DecisionTreeClassifier = classification_fit.calistir(analiz_num, oran_num)
        
        mean_MLPClassifier = "{:.5f}".format(mean(MLPClassifier))
        stddev_MLPClassifier = "{:.5f}".format(stdev(MLPClassifier))
        max_MLPClassifier = "{:.5f}".format(max(MLPClassifier))
        min_MLPClassifier = "{:.5f}".format(min(MLPClassifier))
        
        mean_DecisionTreeClassifier = "{:.5f}".format(mean(DecisionTreeClassifier))
        stddev_DecisionTreeClassifier = "{:.5f}".format(stdev(DecisionTreeClassifier))
        max_DecisionTreeClassifier = "{:.5f}".format(max(DecisionTreeClassifier))
        min_DecisionTreeClassifier = "{:.5f}".format(min(DecisionTreeClassifier))
        
        explanation = f"""
        diabetes_prediction_dataset_edited.csv isimli veri seti çalışılmıştır.
        Her bir metot ile {analiz_num} adet fit işlemi yapılmıştır.
        
        MLPClassifier doğruluk oranları:
        Ortalama değer {mean_MLPClassifier}
        Standart sapma {stddev_MLPClassifier}
        En yüksek değer {max_MLPClassifier}
        En düşük değer {min_MLPClassifier}
        
        DecisionTreeClassifier doğruluk oranları:
        Ortalama değer {mean_DecisionTreeClassifier}
        Standart sapma {stddev_DecisionTreeClassifier}
        En yüksek değer {max_DecisionTreeClassifier}
        En düşük değer {min_DecisionTreeClassifier}
        """

        explanation_window = tk.Toplevel(root)
        explanation_window.title("Sonuçlar")
        explanation_window.geometry("600x300")

        explanation_text = tk.Text(explanation_window, wrap="word")
        explanation_text.insert(tk.END, explanation)
        explanation_text.pack(expand=True, fill="both")
        
        current_dir = os.getcwd() 
        upper_dir = Path(current_dir).parent.absolute()
        
        now = datetime.now()
        
        with open(str(upper_dir) + "/log_file.txt", "a") as file:
            file.write("diabetes_prediction_dataset_edited.csv isimli veri seti " + str(now) +" tarih ve saatinde MLPClassifier ve DecisionTreeClassifier ile çalışılmıştır. \n")
        file.close()
    except ValueError:
        messagebox.showerror("Error", "Geçerli değerler giriniz.")
        
root = tk.Tk()
root.title("Sınıflandırma sayfası")
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