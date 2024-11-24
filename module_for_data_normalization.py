import pandas as pd


def normalize_data(df):
    """Function to normalize two columns "rating_count_tot", "size_bytes"""
    # apply normalization techniques - max-abs scaling.
    for column in df[
        ["rating_count_tot", "size_bytes"]
    ].columns:  # take two columns "rating_count_tot", "size_bytes" for normalization
        df[column] = df[column] / df[column].abs().max()
    return df
