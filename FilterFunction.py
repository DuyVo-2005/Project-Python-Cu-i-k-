import pandas as pd

# Define the filter_data module
def filter_data(dataframe, column, condition, value):
    """
    Filters a DataFrame based on a condition for a specific column.
    
    Args:
        dataframe (pd.DataFrame): The input DataFrame to filter.
        column (str): The column to apply the filter on.
        condition (str): The condition as a string (e.g., '>', '<', '==', '!=', '>=', '<=').
        value: The value to compare against (int, float, or str).
        
    Returns:
        pd.DataFrame: A filtered DataFrame matching the condition.
    """
    if column not in dataframe.columns:
        raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
    
    # Generate the filter condition dynamically
    if condition == '>':
        return dataframe[dataframe[column] > value]
    elif condition == '<':
        return dataframe[dataframe[column] < value]
    elif condition == '==':
        return dataframe[dataframe[column] == value]
    elif condition == '!=':
        return dataframe[dataframe[column] != value]
    elif condition == '>=':
        return dataframe[dataframe[column] >= value]
    elif condition == '<=':
        return dataframe[dataframe[column] <= value]
    elif condition == 'contains':
        if not isinstance(value, str):
            raise ValueError("The 'contains' condition requires a string value.")
        return dataframe[dataframe[column].str.contains(value, na=False, case=False)]
    else:
        raise ValueError(f"Condition '{condition}' is not supported.")

