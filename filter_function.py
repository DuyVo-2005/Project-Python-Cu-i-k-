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
    
def console(dataframe):
    while True:
        print("0. Exit")
        print("1. id")
        print("2. size_bytes")
        print("3. price")
        print("4. rating_count_tot")
        print("5. user_rating")
        print("6. user_rating_ver")
        print("7. sup_devices.num")
        choice = int(input("Choose column you want to search by: "))
        
        if choice == 0:
            break
        
        condition = input("Enter condition (<, >, ==, !=, >=, <=): ")
        value = int(input("Enter value: "))
        
        if choice == 1:
            print(filter_data(dataframe, "id", condition, value))
            
        elif choice == 2:
            print(filter_data(dataframe, "size_bytes", condition, value))
            
        elif choice == 3:
            print(filter_data(dataframe, "price", condition, value))
            
        elif choice == 4:
            print(filter_data(dataframe, "rating_count_tot", condition, value))
        
        elif choice == 5:
            print(filter_data(dataframe, "user_rating", condition, value))
        
        elif choice == 6:
            print(filter_data(dataframe, "user_rating_ver", condition, value))
            
        elif choice == 7:
            print(filter_data(dataframe, "sup_devices.num", condition, value))
            
        else:
            print("ERROR!")