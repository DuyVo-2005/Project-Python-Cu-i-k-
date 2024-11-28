import pandas as pd
import SortFunctionsForConsole

df = pd.read_csv(
    "AppleStore.csv"
)

while True:
    print("Sortable columns list")
    print("1. size_bytes column")
    print("2. price column")
    print("3. user_rating column")
    print("4. user_rating_ver column")
    print("5. cont_rating column")
    print("6. sup_devices.num column")
    print("7. exit")
    choice = int(
        input("Select the column number corresponding to the column you want to sort: ")
    )
    if choice == 7:
        break
    elif choice < 1 or choice > 7:
        print("The number you just selected is not valid! The program ends!")
        break
    else:
        print("Choose sort order")
        print("1. Ascending sort order")
        print("2. Decresing sort order")
        order_choice = int(input("Enter your chose (the corresponding number): "))
        if order_choice != 1 and order_choice != 2:
            print("The number you just selected is not valid! The program ends!")
        else:
            if choice == 1:
                if order_choice == 1:
                    df = SortFunctionsForConsole.size_bytes_ascending_sort(df)
                else:
                    df = SortFunctionsForConsole.size_bytes_decreasing_sort(df)
            elif choice == 2:
                if order_choice == 1:
                    df = SortFunctionsForConsole.price_ascending_sort(df)
                else:
                    df = SortFunctionsForConsole.price_decreasing_sort(df)
            elif choice == 3:
                if order_choice == 1:
                    df = SortFunctionsForConsole.user_rating_ascending_sort(df)
                else:
                    df = SortFunctionsForConsole.user_rating_decreasing_sort(df)
            elif choice == 4:
                if order_choice == 1:
                    df = SortFunctionsForConsole.user_rating_ver_ascending_sort(df)
                else:
                    df = SortFunctionsForConsole.user_rating_ver_decreasing_sort(df)
            elif choice == 5:
                if order_choice == 1:
                    df = SortFunctionsForConsole.cont_rating_ascending_sort(df)
                else:
                    df = SortFunctionsForConsole.cont_rating_decreasing_sort(df)
            else:
                if order_choice == 1:
                    df = SortFunctionsForConsole.sup_devices_num_ascending_sort(df)
                else:
                    df = SortFunctionsForConsole.sup_devices_num_decreasing_sort(df)
    # print(df["sup_devices.num"])#test kiểm tra từng cột cụ thể
    df.to_csv(
        "C:\\Users\\HP\\OneDrive\\Documents\\VÕ LÊ KHÁNH DUY\\python\\data normalization\\AppleStore.csv"
    )
