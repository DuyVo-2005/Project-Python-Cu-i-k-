import pandas as pd


def Search(my_df, x, c):
    if x == "id":
        return filtered_data = my_df[my_df[x].astype(str) == c]
    
    return filtered_data = my_df[my_df[x].astype(str).str.contains(c, case=False)]
