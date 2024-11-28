def size_bytes_ascending_sort(df):
    """Function to sort ascendingly size_bytes column"""
    df.sort_values("size_bytes", ascending=True, inplace=True)
    return df


def size_bytes_decreasing_sort(df):
    """Function to sort decreasingly size_bytes column"""
    df.sort_values("size_bytes", ascending=False, inplace=True)
    return df


def price_ascending_sort(df):
    """Function to sort ascendingly price column"""
    df.sort_values("price", ascending=True, inplace=True)
    return df


def price_decreasing_sort(df):
    """Function to sort decresingly price column"""
    df.sort_values("price", ascending=False, inplace=True)
    return df


def user_rating_ascending_sort(df):
    """Function to sort ascendingly user_rating column"""
    df.sort_values("user_rating", ascending=True, inplace=True)
    return df


def user_rating_decreasing_sort(df):
    """Function to sort decresingly user_rating column"""
    df.sort_values("user_rating", ascending=False, inplace=True)
    return df


def user_rating_ver_ascending_sort(df):
    """Function to sort ascendingly user_rating_ver column"""
    df.sort_values("user_rating_ver", ascending=True, inplace=True)
    return df


def user_rating_ver_decreasing_sort(df):
    """Function to sort decresingly user_rating_ver column"""
    df.sort_values("user_rating_ver", ascending=False, inplace=True)
    return df


def cont_rating_ascending_sort(df):
    """Function to sort ascendingly cont_rating column"""
    # create a temporary cont_rating_numeric_column to simplify integer number sort
    df["cont_rating_numeric_column"] = (
        df["cont_rating"].str.extract("(\d+)").astype(int)
    )  # Extract numeric characters from string, convert extracted numeric string to integer type.
    df.sort_values("cont_rating_numeric_column", ascending=True, inplace=True)
    df = df.drop(columns=["cont_rating_numeric_column"])  # delete temporary column
    return df


def cont_rating_decreasing_sort(df):
    """Function to sort decreasingly cont_rating column"""
    # create a temporary cont_rating_numeric_column to simplify integer number sort
    df["cont_rating_numeric_column"] = (
        df["cont_rating"].str.extract("(\d+)").astype(int)
    )  # Extract numeric characters from string, convert extracted numeric string to integer type.
    df.sort_values("cont_rating_numeric_column", ascending=False, inplace=True)
    df = df.drop(columns=["cont_rating_numeric_column"])  # delete temporary column
    return df


def sup_devices_num_ascending_sort(df):
    """Function to sort ascendingly sup_devices.num column"""
    df.sort_values("sup_devices.num", ascending=True, inplace=True)
    return df


def sup_devices_num_decreasing_sort(df):
    """Function to sort decresingly sup_devices.num column"""
    df.sort_values("sup_devices.num", ascending=False, inplace=True)
    return df
