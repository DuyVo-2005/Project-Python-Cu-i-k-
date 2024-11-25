import pandas as pd
from ydata_profiling import ProfileReport

def generate_data_report(df):
    """
    Generates a detailed profiling report for the given DataFrame and displays it within a Jupyter notebook.

    Parameters:
    ----------
    df : pd.DataFrame
        The DataFrame to be profiled.

    Returns:
    -------
    None
    """
    profile = ProfileReport(df, title='Reviewing Data', explorative=True)
    profile.to_notebook_iframe()


def clean_incorrect_data(df, column_rules):
    """
    Fix incorrect data based on column rules.
    param df: DataFrame to clean.
    param column_rules: Dictionary of rules for each column (e.g., ranges or conditions).
    return: Cleaned DataFrame.
    """
    
    for column, rule in column_rules.items():
        if 'range' in rule:
            min_val, max_val = rule['range']
            df = df[(df[column] >= min_val) & (df[column] <= max_val)]
        if 'type' in rule:
            df = df[df[column].apply(lambda x: isinstance(x, rule['type']))]
    return df

def remove_duplicates(df, subset=None):
    """
    Remove duplicate rows from the DataFrame.
    :param df: DataFrame to clean.
    :param subset: Subset of columns to check for duplicates.
    :return: DataFrame without duplicates.
    """
    return df.drop_duplicates(subset=subset)

def fix_mislabeled_data(df, label_column, correct_labels):
    """
    Fix mislabeled data based on a list of correct labels.
    :param df: DataFrame to clean.
    :param label_column: The column containing labels to verify.
    :param correct_labels: A list of valid labels.
    :return: DataFrame with corrected labels.
    """
    df = df[df[label_column].isin(correct_labels)]
    return df

def handle_missing_data(df, strategy='drop', fill_values=None):
    """
    Handle missing data in the DataFrame.
    :param df: DataFrame to clean.
    :param strategy: Strategy to handle missing values ('drop' or 'fill').
    :param fill_values: Dictionary of fill values for columns if strategy is 'fill'.
    :return: Cleaned DataFrame.
    """
    if strategy == 'drop':
        return df.dropna()
    elif strategy == 'fill' and fill_values:
        return df.fillna(fill_values)
    return df

def start_cleaning(df):
    # Step 1: Remove duplicates
    print("Removing duplicates...")
    df = remove_duplicates(df)

    # Step 2: Clean incorrect data (example rule)
    print("Cleaning incorrect data...")
    column_rules = {
        'price': {'range': (0, 1000)},  # Example: Price should be between 0 and 1000
        'user_rating': {'range': (0, 5)}  # Ratings should be between 0 and 5
    }
    df = clean_incorrect_data(df, column_rules)

    # Step 3: Handle missing data (if any)
    print("Handling missing data...")
    df = handle_missing_data(df, strategy='drop')

    # Step 4: Fix mislabeled data (example for genres)
    print("Fixing mislabeled data...")
    valid_genres = ['Games', 'Productivity', 'Weather', 'Shopping', 'Reference']
    df = fix_mislabeled_data(df, 'prime_genre', valid_genres)