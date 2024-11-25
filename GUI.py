import tkinter as tk
import pandas as pd
from tkinter import ttk
from tkinter import messagebox
import search_module
import CRUD
import sort
import clearning
import visual
import module_for_data_normalization

df = pd.read_csv("AppleStore.csv", sep=",")
df = clearning.fill_na_value(df)
df = module_for_data_normalization.normalize_data(df)
root = tk.Tk()
root.geometry('1920x900')
root.resizable(True, True)
root.title("DataAnalysis")
ROWS_PER_PAGE = 15
current_page = 0
import tkinter as tk
def clear_window():
    """Xoa mang hinh"""
    for widget in root.winfo_children():
        widget.destroy()
def show_menu():
    """Hien thi giao dien tuy chon"""
    clear_window()
    label = tk.Label(root, text="------ Data Analysis ------", font=("Times New Roman", 20, "bold"), 
                     bg="lightblue", fg="darkblue", padx=10, pady=10)
    label.pack(pady=20)
    label_menu = tk.Label(root, text="MENU", font=("Times New Roman", 20, "bold"))
    label_menu.pack(pady=10)
    button_frame = tk.Frame(root)
    button_frame.pack(pady=20) 
    button_view = tk.Button(button_frame, text="View Data", font=("Times New Roman", 15), width=15, command=lambda:show_page(df, current_page))
    button_view.grid(row=0, column=0, padx=10, pady=10)
    button_add = tk.Button(button_frame, text="Add Data", font=("Times New Roman", 15), width=15, command=show_add_form)
    button_add.grid(row=0, column=1, padx=10, pady=10)
    button_update = tk.Button(button_frame, text="Update Data", font=("Times New Roman", 15), width=15, command=show_update_form)
    button_update.grid(row=0, column=2, padx=10, pady=10)
    button_delete = tk.Button(button_frame, text="Delete Data", font=("Times New Roman", 15), width=15, command=show_delete_form)
    button_delete.grid(row=1, column=0, padx=10, pady=10)
    button_sort = tk.Button(button_frame, text="Sort Data", font=("Times New Roman", 15), width=15, command=show_sort_form)
    button_sort.grid(row=1, column=1, padx=10, pady=10)
    button_search = tk.Button(button_frame, text="Search Data", font=("Times New Roman", 15), width=15, command=show_search_form)
    button_search.grid(row=1, column=2, padx=10, pady=10)
    button_visual = tk.Button(button_frame, text="Visualization", font=("Times New Roman", 15), width=15, command=show_plot_form)
    button_visual.grid(row=2, column=1, padx=5, pady=10)
def show_add_form():
    """Hien thi giao dien update"""
    clear_window()
    label = tk.Label(root, text="ADD DATA", font=("Times New Roman", 20, "bold"))
    label.pack(pady=10)

    # Frame chua form nhap du lieu
    form_frame = tk.Frame(root)
    form_frame.pack(pady=20)
    # danh sach cac truong can nhap
    fields = ["no.",
        "id", "track_name", "size_bytes", "currency", "price",
        "rating_count_tot", "user_rating", 
        "user_rating_ver", "ver", "cont_rating", "prime_genre", 
        "sup_devices.num"
    ]
    entries = {}
    # Tao cac o nhap du lieu
    for i, field in enumerate(fields):
        label = tk.Label(form_frame, text=field, font=("Times New Roman", 15))
        label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
        entry = tk.Entry(form_frame, font=("Times New Roman", 15), width=30)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[field] = entry

    #ham save
    def save_data():
        new_data = {field: entry.get() for field, entry in entries.items()}
        CRUD.Create(df, new_data)
        df.to_csv("AppleStore.csv", index=False)
        messagebox.showinfo("Notification", "Dataset updated and saved")

    save_button = tk.Button(root, text="Save", font=("Times New Roman", 15), command=save_data)
    save_button.pack(pady=10)

    # Nut back
    back_button = tk.Button(root, text="Back to menu", font=("Times New Roman", 15), command=show_menu)
    back_button.pack(pady=10)

def show_update_form():
    """Hien thi giao dien update"""
    clear_window()

    # Tieu de
    label = tk.Label(root, text="Update Data", font=("Times New Roman", 20, "bold"))
    label.pack(pady=10)

    # frame tim kiem
    search_frame = tk.Frame(root)
    search_frame.pack(pady=20)

    tk.Label(search_frame, text="track name:", font=("Times New Roman", 15)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
    search_entry = tk.Entry(search_frame, font=("Times New Roman", 15), width=30)
    search_entry.grid(row=0, column=1, padx=10, pady=5)

    # frame hien thi thong tin
    info_frame = tk.Frame(root)
    info_frame.pack(pady=20)

    # Lay danh sach cac cot
    columns = list(df.columns)

    def search_app():
        #Tim kiem theo track name
        for widget in info_frame.winfo_children():
            widget.destroy()

        app_name = search_entry.get()
        filtered_df = df[df["track_name"].str.contains(app_name, case=False)]

        if filtered_df.empty:
            messagebox.showinfo(
                "Notification", f"No item found with name '{app_name}'."
            )
            return

        # Hien thi thong tin tim kiem duoc
        tk.Label(info_frame, text=f"Found {len(filtered_df)} item(s):", font=("Times New Roman", 15, "bold")).pack()


        # form cap nhat
        update_frame = tk.Frame(root)
        update_frame.pack(pady=20)

        tk.Label(update_frame, text="Select Column:", font=("Times New Roman", 15)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        column_combobox = ttk.Combobox(update_frame, values=columns, font=("Times New Roman", 15))
        column_combobox.grid(row=0, column=1, padx=10, pady=5)
        column_combobox.current(0)

        tk.Label(update_frame, text="New Value:", font=("Times New Roman", 15)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        value_entry = tk.Entry(update_frame, font=("Times New Roman", 15), width=30)
        value_entry.grid(row=1, column=1, padx=10, pady=5)

        def save_update():
            #Luu thay doi
            column_to_update = column_combobox.get()
            new_value = value_entry.get()

            for idx in filtered_df.index:
                message = CRUD.Update(df, filtered_df.loc[idx, "track_name"], column_to_update, new_value)
            messagebox.showinfo(
                "Notification", "Dataset updated and saved"
            )

        save_button = tk.Button(update_frame, text="Save", font=("Times New Roman", 15), command=save_update)
        save_button.grid(row=2, column=0, columnspan=2, pady=10)
    # Tao nut tim kiem
    search_button = tk.Button(search_frame, text="Search", font=("Times New Roman", 15), command=search_app)
    search_button.grid(row=0, column=2, padx=10, pady=5)

    # Tao nut back to menu
    back_button = tk.Button(root, text="Back to menu", font=("Times New Roman", 15), command=show_menu)
    back_button.pack(pady=10)



def show_delete_form():
    """
    Hiển thị giao diện để xóa ứng dụng.
    """
    clear_window()

    # Tao tieu de
    label = tk.Label(root, text="Delete", font=("Times New Roman", 20, "bold"))
    label.pack(pady=10)

    # Frame tim kiem
    search_frame = tk.Frame(root)
    search_frame.pack(pady=20)

    tk.Label(search_frame, text="Item Name:", font=("Times New Roman", 15)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
    search_entry = tk.Entry(search_frame, font=("Times New Roman", 15), width=30)
    search_entry.grid(row=0, column=1, padx=10, pady=5)

    # Frame hien thi ke qua
    result_frame = tk.Frame(root)
    result_frame.pack(pady=20)

    def search_app():
        #Tim kiem va hien thi ke qua tim kiem
        for widget in result_frame.winfo_children():
            widget.destroy()

        app_name = search_entry.get()
        filtered_df = df[df["track_name"].str.contains(app_name, case=False)]

        if filtered_df.empty:
            messagebox.showinfo(
                "Notification", f"No item found with name '{app_name}'."
            )
            return

        tk.Label(result_frame, text=f"Found {len(filtered_df)} item(s):", font=("Times New Roman", 15, "bold")).pack()
        # for idx, row in filtered_df.iterrows():
        #     tk.Label(result_frame, text=f"- {row['track_name']} (ID: {row['id']})", font=("Times New Roman", 15)).pack()

        # frame xoa
        delete_frame = tk.Frame(root)
        delete_frame.pack(pady=20)

        def delete_app():
            #Xoa khoi dataframe
            for idx in filtered_df.index:
                app_to_delete = filtered_df.loc[idx, "track_name"]
                message = CRUD.Delete(df, app_to_delete)
                tk.Label(root, text=message, font=("Times New Roman", 15), fg="green").pack(pady=10)
            search_app()
            messagebox.showinfo("Notification", "Delete Successfully!")
            

        delete_button = tk.Button(delete_frame, text="Delete All", font=("Times New Roman", 15), command=delete_app)
        delete_button.pack(pady=10)

    # Tao nut tim kiem
    search_button = tk.Button(search_frame, text="Search", font=("Times New Roman", 15), command=search_app)
    search_button.grid(row=0, column=2, padx=10, pady=5)
    
    # Tao nut back to menu
    back_button = tk.Button(root, text="Back", font=("Times New Roman", 15), command=show_menu)
    back_button.pack(pady=10)


def show_search_form():
    "hien thi giao dien tim kiem"
    clear_window()

    # Tạo tiêu đề
    label = tk.Label(root, text="Search Data", font=("Times New Roman", 20, "bold"))
    label.pack(pady=10)

    # Frame tìm kiếm
    search_frame = tk.Frame(root)
    search_frame.pack(pady=20)

    # Label và Entry cho từ khóa tìm kiếm
    tk.Label(search_frame, text="Search by track name:", font=("Times New Roman", 15)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
    search_entry = tk.Entry(search_frame, font=("Times New Roman", 15), width=30)
    search_entry.grid(row=0, column=1, padx=10, pady=5)

    # Nút tìm kiếm
    search_button = tk.Button(search_frame, text="Search", font=("Times New Roman", 15), command=lambda: search_app(search_entry.get()))
    search_button.grid(row=0, column=2, padx=10, pady=5)

    # Nút quay lại menu
    back_button = tk.Button(root, text="Back to menu", font=("Times New Roman", 15), command=show_menu)
    back_button.pack(pady=10)
def search_app(search_term):
    "Tim tiem theo track name"
    clear_window()


    filtered_df = df[df["track_name"].str.contains(search_term, case=False, na=False)]

    if filtered_df.empty:
        messagebox.showinfo("Notification", f"No results found for '{search_term}'.")
        back_button = tk.Button(root, text="Back to menu", font=("Times New Roman", 15), command=show_menu)
        back_button.pack(pady=10)
        return


    tk.Label(root, text=f"Found {len(filtered_df)} result(s) for '{search_term}':", font=("Times New Roman", 15, "bold")).pack(pady=10)


    global current_page, ROWS_PER_PAGE
    current_page = 0


    show_page(filtered_df, current_page)

def show_page(filtered_df, page):
    """hien thong tin duoi dang phan trang"""
    for widget in root.winfo_children():
        widget.destroy()

    frame = tk.Frame(root)
    frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    columns = list(filtered_df.columns)
    tree = ttk.Treeview(frame, columns=columns, show="headings", height=ROWS_PER_PAGE)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor="center")
    tree.pack(expand=True, fill=tk.BOTH)


    start = page * ROWS_PER_PAGE
    end = start + ROWS_PER_PAGE
    for index, row in filtered_df.iloc[start:end].iterrows():
        tree.insert("", "end", values=list(row))


    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)


    prev_button = tk.Button(button_frame, text="Previous Page", command=lambda: prev_page(filtered_df), state=tk.DISABLED)
    prev_button.pack(side=tk.LEFT, padx=5, pady=5)

    next_button = tk.Button(button_frame, text="Next Page", command=lambda: next_page(filtered_df), state=tk.DISABLED)
    next_button.pack(side=tk.RIGHT, padx=5, pady=5)

    back_button = tk.Button(button_frame, text="Back to menu", command=show_menu)
    back_button.pack(side=tk.LEFT, padx=5, pady=5)
    prev_button.config(state=tk.NORMAL if current_page > 0 else tk.DISABLED)
    next_button.config(state=tk.NORMAL if (current_page + 1) * ROWS_PER_PAGE < len(filtered_df) else tk.DISABLED)
def next_page(filtered_df):
    global current_page
    if (current_page + 1) * ROWS_PER_PAGE < len(filtered_df):
        current_page += 1
        show_page(filtered_df, current_page)
def prev_page(filtered_df):
    global current_page
    if current_page > 0:
        current_page -= 1
        show_page(filtered_df, current_page)

def show_sort_form():
    """sap xep theo cac tieu chi:
            size_bytes ascending
            size_bytes decreasin
            price ascending
            price decreasing
            user_rating ascending
            user_rating decreasing
            cont_rating ascending
            cont_rating decreasing
            sup_devices_num ascending
            sup_devices_num decreasing
    """
    clear_window()
    label_sort = tk.Label(root, text="Sort", font=("Times New Roman", 20, 'bold'))
    label_sort.pack(side="top", pady=20)
    frame = tk.Frame(root)
    frame.pack(pady=40)
    buttons = [
        ("size_bytes ascending", lambda: sort.size_bytes_ascending_sort(df)),
        ("size_bytes decreasing", lambda: sort.size_bytes_decreasing_sort(df)),
        ("price ascending", lambda: sort.price_ascending_sort(df)),
        ("price decreasing", lambda: sort.price_decreasing_sort(df)),
        ("user_rating ascending", lambda: sort.user_rating_ascending_sort(df)),
        ("user_rating decreasing", lambda: sort.user_rating_decreasing_sort(df)),
        ("cont_rating ascending", lambda: sort.cont_rating_ascending_sort(df)),
        ("cont_rating decreasing", lambda: sort.cont_rating_decreasing_sort(df)),
        ("sup_devices_num ascending", lambda: sort.sup_devices_num_ascending_sort_button(df)),
        ("sup_devices_num decreasing", lambda: sort.sup_devices_num_decreasing_sort_button(df)),
        ("Back to menu", show_menu)
    ]
    for index, (text, command) in enumerate(buttons):
        row = index // 3
        column = index % 3
        button = tk.Button(frame, text=text, font=("Times New Roman", 15), command=command)
        button.grid(row=row, column=column, padx=5, pady=10, sticky="ew")
    for col in range(3):
        frame.grid_columnconfigure(col, weight=1, uniform="equal")
def show_plot_form():
    "Tuy chon hien thi bieu do"
    clear_window()


    label_plot = tk.Label(root, text="Visualization", font=("Times New Roman", 20, 'bold'))
    label_plot.pack(side="top", pady=20)

    frame = tk.Frame(root)
    frame.pack(pady=40)

    buttons = [
        ("Genre Distribution", lambda: visual.plot_genre_distribution(df)),
        ("Rating Distribution", lambda: visual.plot_rating_distribution(df)),
        ("User Rating Distribution", lambda: visual.plot_user_rating_distribution(df)),
        ("Avg Rating by Genre", lambda: visual.plot_avg_rating_by_genre(df)),
        ("Total Ratings by Genre", lambda: visual.plot_total_ratings_by_genre(df)),
        ("Avg Price by Genre", lambda: visual.plot_avg_price_by_genre(df)),
        ("Apps by Content Rating", lambda: visual.plot_apps_by_content_rating(df)),
        ("Free vs Paid by Genre", lambda: visual.plot_free_vs_paid_by_genre(df, top_n=5)),
        ("Apps by Supported Devices", lambda: visual.plot_apps_by_supported_devices(df)),
        ("Back to menu", show_menu)
    ]
    for index, (text, command) in enumerate(buttons):
        row = index // 3  
        column = index % 3  

        button = tk.Button(frame, text=text, font=("Times New Roman", 15), command=command)
        button.grid(row=row, column=column, padx=5, pady=10, sticky="ew") 
    for col in range(3):
        frame.grid_columnconfigure(col, weight=1, uniform="equal")
show_menu()
root.mainloop()
