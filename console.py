import pandas as pd
import CRUD
import data_cleaning
import data_normalization
import data_visualization
import search_function_for_console
import sort_function_for_console
import filter_function 

file_path = "AppleStore.csv"
my_df = pd.read_csv(file_path)
my_df = my_df.loc[:, ~my_df.columns.str.contains("^Unnamed")]

while True:
    print()
    print("0. Exit")
    print("1. Create, Read, Update, Delete")
    print("2. Data cleaning")
    print("3. Normalization")
    print("4. Visualization")
    print("5. Search")
    print("6. Sort")
    print("7. Filter")
    choice1 = int(input("Your choice: "))

    if choice1 == 0:
        break

    elif choice1 == 1:
        CRUD.console()

    elif choice1 == 2:
        data_cleaning.start_cleaning(my_df)

    elif choice1 == 3:
        data_normalization.console(my_df)

    elif choice1 == 4:
        data_visualization.console()

    elif choice1 == 5:
        search_function_for_console.console(my_df)

    elif choice1 == 6:
        sort_function_for_console.console(my_df)
        
    elif choice1 == 7:
        filter_function.console(my_df)
        
    else:
        print("ERROR!")
