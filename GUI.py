import tkinter as tk
import pandas as pd
from tkinter import ttk
df = pd.read_csv("AppleStore.csv", sep=",", index_col=0)
root = tk.Tk()
root.geometry('1920x900')
root.resizable(True, True)
root.title("DataAnalysis")
ROWS_PER_PAGE = 10
current_page = 0
import tkinter as tk
def clear_window():
    #clear screen
    for widget in root.winfo_children():
        widget.destroy()
def show_menu():
    #show menu option
    clear_window()
    label = tk.Label(root, text="------ Data Analysis ------", font=("Times New Roman", 20, "bold"), 
                     bg="lightblue", fg="darkblue", padx=10, pady=10)
    label.pack(pady=20)
    label_menu = tk.Label(root, text="MENU", font=("Times New Roman", 20, "bold"))
    label_menu.pack(pady=10)
    button_frame = tk.Frame(root)
    button_frame.pack(pady=20) 
    button_view = tk.Button(button_frame, text="View Data", font=("Times New Roman", 15), width=15, command=lambda:show_page(current_page))
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

def next_page():
    #to next page
    global current_page
    if (current_page + 1) * ROWS_PER_PAGE < len(df):
        current_page += 1
        show_page(current_page)

def prev_page():
    #to previous page
    global current_page
    if current_page > 0:
        current_page -= 1
        show_page(current_page)


def show_page(page):
    #show current page
    global current_page
    for widget in root.winfo_children():
        widget.destroy()
    frame = tk.Frame(root)
    frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    columns = list(df.columns)
    tree = ttk.Treeview(frame, columns=columns, show="headings", height=ROWS_PER_PAGE)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor="center")
    start = page * ROWS_PER_PAGE
    end = start + ROWS_PER_PAGE
    for index, row in df.iloc[start:end].iterrows():
        tree.insert("", "end", values=list(row))
    tree.pack(expand=True, fill=tk.BOTH)
    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)
    prev_button = tk.Button(button_frame, text="Trang trước", command=prev_page, state=tk.DISABLED)
    prev_button.pack(side=tk.LEFT, padx=5, pady=5)
    next_button = tk.Button(button_frame, text="Trang sau", command=next_page, state=tk.DISABLED)
    next_button.pack(side=tk.RIGHT, padx=5, pady=5)
    back_button = tk.Button(button_frame, text="Back", command=show_menu)
    back_button.pack(side= tk.LEFT, padx=5, pady=5)
    current_page = page
    prev_button.config(state=tk.NORMAL if current_page > 0 else tk.DISABLED)
    next_button.config(state=tk.NORMAL if (current_page + 1) * ROWS_PER_PAGE < len(df) else tk.DISABLED)
show_menu()
root.mainloop()
