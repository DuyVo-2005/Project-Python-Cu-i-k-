import pandas as pd
import sort_function

def console(df):
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
            input(
                "Select the column number corresponding to the column you want to sort: "
            )
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
                        df = sort_function.size_bytes_ascending_sort(df)
                        print(df[["size_bytes"]])
                    else:
                        df = sort_function.size_bytes_decreasing_sort(df)
                        print(df[["size_bytes"]])
                elif choice == 2:
                    if order_choice == 1:
                        df = sort_function.price_ascending_sort(df)
                        print(df[["price"]])
                    else:
                        df = sort_function.price_decreasing_sort(df)
                        print(df[["price"]])
                elif choice == 3:
                    if order_choice == 1:
                        df = sort_function.user_rating_ascending_sort(df)
                        print(df[["user_rating"]])
                    else:
                        df = sort_function.user_rating_decreasing_sort(df)
                        print(df[["user_rating"]])
                elif choice == 4:
                    if order_choice == 1:
                        df = sort_function.user_rating_ver_ascending_sort(df)
                        print(df[["user_rating_ver"]])
                    else:
                        df = sort_function.user_rating_ver_decreasing_sort(df)
                        print(df[["user_rating_ver"]])
                elif choice == 5:
                    if order_choice == 1:
                        df = sort_function.cont_rating_ascending_sort(df)
                        print(df[["cont_rating"]])
                    else:
                        df = sort_function.cont_rating_decreasing_sort(df)
                        print(df[["cont_rating"]])
                else:
                    if order_choice == 1:
                        df = sort_function.sup_devices_num_ascending_sort(df)
                        print(df[["sup_devices.num"]])
                    else:
                        df = sort_function.sup_devices_num_decreasing_sort(df)
                        print(df[["sup_devices.num"]])
        # print(df["sup_devices.num"])#test kiểm tra từng cột cụ thể
        df.to_csv("AppleStore.csv")
