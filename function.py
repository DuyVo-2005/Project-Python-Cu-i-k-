import pandas as pd


def Search(my_df):
    global list_search
    global c
    global choice
    
    print()
    print("1. Search app by ID")
    print("2. Search app by Name")
    print("3. Search app by Version")
    print("4. Search app by Primary Genre")
    print("Enter 0 to exit")
    choice = int(input("Select the type of information you want to search for: "))

    if choice < 0 and choice > 4:
        print("ERROR!")
                
    if choice == 0:
        return
            
    print("Enter 0 to exit")
            
    if choice == 1:
        print("Enter the ID of the app: ", end="")
        x = "id"
            
    if choice == 2:
        print("Enter the Name of the app: ", end="")
        x = "track_name"
                
    if choice == 3:
        print("Enter the Version of the app: ", end="")
        x = "ver"
                
    if choice == 4:
        print("Enter the Primary Genre of the app: ", end="")
        x = "prime_genre"

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
