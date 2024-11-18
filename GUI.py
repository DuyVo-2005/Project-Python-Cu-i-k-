import tkinter as tk
import pandas as pd
from tkinter import ttk
df = pd.read_csv("AppleStore.csv", sep=",")
root = tk.Tk()
root.geometry('1920x900')
root.resizable(True, True)
root.title("DataAnalysis")

import tkinter as tk

def show_menu():
    label = tk.Label(root, text="------ Data Analysis ------", font=("Times New Roman", 20, "bold"), 
                     bg="lightblue", fg="darkblue", padx=10, pady=10)
    label.pack(pady=20)
    label_menu = tk.Label(root, text="MENU", font=("Times New Roman", 20, "bold"))
    label_menu.pack(pady=10)
    button_frame = tk.Frame(root)
    button_frame.pack(pady=20) 
    button_view = tk.Button(button_frame, text="View Data", font=("Times New Roman", 15), width=15)
    button_view.grid(row=0, column=0, padx=10, pady=10)
    button_add = tk.Button(button_frame, text="Add Data", font=("Times New Roman", 15), width=15)
    button_add.grid(row=0, column=1, padx=10, pady=10)
    button_update = tk.Button(button_frame, text="Update Data", font=("Times New Roman", 15), width=15)
    button_update.grid(row=0, column=2, padx=10, pady=10)
    button_delete = tk.Button(button_frame, text="Delete Data", font=("Times New Roman", 15), width=15)
    button_delete.grid(row=1, column=0, padx=10, pady=10)
    button_sort = tk.Button(button_frame, text="Sort Data", font=("Times New Roman", 15), width=15)
    button_sort.grid(row=1, column=1, padx=10, pady=10)
    button_search = tk.Button(button_frame, text="Search Data", font=("Times New Roman", 15), width=15)
    button_search.grid(row=1, column=2, padx=10, pady=10)
show_menu()
root.mainloop()

