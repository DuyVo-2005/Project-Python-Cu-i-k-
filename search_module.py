import pandas as pd


def Search(my_df, x):
    global list_search
    global c

    list_search = []
    c = input()
    
    if x == "id":
        filtered_data = my_df[my_df[x].astype(str) == c]
    else:
        filtered_data = my_df[my_df[x].astype(str).str.contains(c, case=False)]

    list_search = filtered_data["track_name"].tolist()

    if not list_search:
        print("Not found!")
    return list_search
