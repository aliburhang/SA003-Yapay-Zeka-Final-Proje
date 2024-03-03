#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 17:45:42 2024

@author: aliburhanguncan
"""

import tkinter as tk
from tkinter import messagebox
import subprocess
import os

current = os.getcwd()

def run_selected_script():
    selection = choice_var.get()
    if selection == "Sınıflandırma":
        subprocess.Popen([current + "/01-Siniflandirma/classification_run_file.py"], cwd = current + "/01-Siniflandirma/")
    elif selection == "Regresyon":
        subprocess.Popen([current + "/02-Regresyon/scoring_run_file.py"], cwd = current + "/02-Regresyon/")
    elif selection == "Kümeleme":
        subprocess.Popen([current + "/03-Kumeleme/clustering_run_file.py"], cwd = current + "/03-Kumeleme/")
    else:
        messagebox.showerror("Error", "Please select a script.")

# Create the main window
root = tk.Tk()
root.title("Ana Sayfa")
root.geometry("400x300")

# Create a label
label = tk.Label(root, text="Merhaba, lütfen çalıştırmak istediğin algoritmayı seç!")
label.pack()

# Create a dropdown menu
choices = ["Sınıflandırma", "Regresyon", "Kümeleme"]
choice_var = tk.StringVar(root)
choice_var.set(choices[0])  # Default selection
dropdown = tk.OptionMenu(root, choice_var, *choices)
dropdown.pack()

# Create a "Run" button
run_button = tk.Button(root, text="Çalıştır", command=run_selected_script)
run_button.pack()

# Run the Tkinter event loop
root.mainloop()