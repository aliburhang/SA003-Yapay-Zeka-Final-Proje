#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 17:45:42 2024

@author: aliburhanguncan
"""
import tkinter as tk
from tkinter import messagebox
import clustering_fit
import os
from pathlib import Path
from datetime import datetime

def hesapla():
    try:
        msre_2, msre_10 = clustering_fit.calistir() 
        
        msre_2 = "{:.4f}".format(msre_2)
        msre_10 = "{:.4f}".format(msre_10)
        
        explanation = f"""
        1. Customers_edited.csv isimli veri seti çalışılmıştır.
        2. Kullanılan datada bir hedef sütun yoktur.
        3. Burada PCA 2 ve 10 kümeli olacak şekilde çalıştırılmıştır.
        4. Hata için şu şekilde bir modelleme yapılmıştır:
           4.1. Elde edilen PCA datası detransform edilmiştir.
           4.2. Detransform datası ile orjinal dataframein farkının mutlak değeri alınmıştır.
           4.3. Her bir satır için bu mutlak değerlerin karelerinin toplamının karekökü alınıp dataframein orjinal haline yeni sütunlar olarak eklenmiştir.
           4.4. Son durumda PCA'in 2 ve 10 kümeli hali için hatayı temsil eden yeni iki sütun oluşmuştur.
           4.5. Bu sütunların ortalaması da bu çalışmada hata olarak tanımlanmıştır.
        
        Yukarıda açıklanan hata modellemesine göre 2 durum için de hatalar şu şekildedir:
        2 kümeli PCA için hata: {msre_2}
        10 kümeli PCA için hata: {msre_10}
        
        Sistemde hata hesaplanırken detransform edilen datanın ve orjinal datanın sıralamaları önemli olduğu için shuffle yapılmamış ve sistem 1'den fazla kez itere edilecek şekilde kodlanmamıştır.
        """

        explanation_window = tk.Toplevel(root)
        explanation_window.title("Sonuçlar")
        explanation_window.geometry("600x400")

        explanation_text = tk.Text(explanation_window, wrap="word")
        explanation_text.insert(tk.END, explanation)
        explanation_text.pack(expand=True, fill="both")
        
        current_dir = os.getcwd() 
        upper_dir = Path(current_dir).parent.absolute()
        
        now = datetime.now()
        
        with open(str(upper_dir) + "/log_file.txt", "a") as file:
            file.write("Customers_edited.csv isimli veri seti " + str(now) +" tarih ve saatinde 2 kümeli PCA ve 10 kümeli PCA ile çalışılmıştır. \n")
        file.close()
    except ValueError:
        messagebox.showerror("Error", "Geçerli değerler giriniz.")
        
root = tk.Tk()
root.title("Kümeleme sayfası")
root.geometry("400x300")

# Create button to trigger calculation
calculate_button = tk.Button(root, text="Hesapla", command=hesapla)
calculate_button.pack()

# Run the main event loop
root.mainloop()