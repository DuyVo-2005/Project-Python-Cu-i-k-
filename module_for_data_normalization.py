import pandas as pd
import sys
import matplotlib.pyplot as plt
import sort_function

sys.path.append(
    "D:\\source-code\\analysis_data_package"
)  # thêm đường dẫn package vào sys.path
# print(sys.path)


def normalize_data(df):
    """Function to normalize two columns "rating_count_tot", "size_bytes"""
    # apply normalization techniques - max-abs scaling.
    for column in df[
        ["rating_count_tot", "size_bytes"]
    ].columns:  # take two columns "rating_count_tot", "size_bytes" for normalization
        df[column] = df[column] / df[column].abs().max()
    return df


def normalize_column(df: pd.DataFrame, column_name: str) -> pd.Series:
    """Function to normalize comlumns has name: "column_name"""
    df[column_name] = df[column_name] / df[column_name].abs().max()
    return df[column_name]


def plot_price_by_size_bytes(df):
    """Visualizes price according to size bytes"""
    df_copy = df.copy()

    plt.figure(figsize=(10, 6))
    df_copy["size_bytes"] = normalize_column(df_copy, "size_bytes")
    df_copy["price"] = normalize_column(df_copy, "price")
    plt.scatter(df_copy["price"], df_copy["size_bytes"])
    plt.xlabel("price")
    plt.ylabel("size_bytes")
    plt.title("Price according to size bytes Plot")
    plt.show()


def plot_size_bytes_by_rating_count_tot(df):
    """Visualizes size bytes according to rating_count_tot"""
    plt.figure(figsize=(10, 6))
    # plt.scatter(df["size_bytes"], df["rating_count_tot"])
    plt.bar(df["size_bytes"], df["rating_count_tot"])
    plt.xlabel("size bytes")
    plt.ylabel("rating_count_tot")
    plt.title("Size bytes according to rating count total Plot")
    plt.show()


def plot_size_bytes_by_rating_count_tot_with_normalization(df):
    """Visualizes size bytes according to rating_count_tot with normalization"""
    df_copy = df.copy()
    plt.figure(figsize=(10, 6))
    df_copy = normalize_data(df_copy)
    plt.bar(df_copy["size_bytes"], df_copy["rating_count_tot"])
    plt.xlabel("size bytes")
    plt.ylabel("rating_count_tot")
    plt.title("Size bytes according to rating count total with normalization Plot")
    plt.show()


def console(df):
    normalize_data(df)
    print("Data of two columns 'rating_count_tot', 'size_bytes' after normalization")
    print(df[["rating_count_tot", "size_bytes"]])
