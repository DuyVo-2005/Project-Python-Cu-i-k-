import pandas as pd
import function as f

my_df = pd.read_csv("C:\\Users\hienvp\Documents\Project_Python\AppleStore.csv")


while True:
    print()
    print("0. Exit ")
    print("1. Delete column")
    print("2. Delete app")
    choice = int(input("Choose your action: "))

    if choice == 0:
        break

    elif choice == 1:
        print("Enter the name of the column you want to delete: ", end="")
        f.Search(my_df.head(0))

        while True:
            print()
            idx = 0
            for i in f.list_search:
                idx += 1
                print(idx, i)

            if len(f.list_search) != 0:
                print("Enter 0 to exit")
                choice = int(
                    input(
                        "Enter the number corresponding to the column name you want to delete: "
                    )
                )

                if choice == 0:
                    break

                if choice < 0 or choice > len(f.list_search):
                    print("ERROR!")

                else:
                    my_df.drop(columns=f.list_search[choice - 1], inplace=True)
                    f.list_search.remove(f.list_search[choice - 1])
                    print("Deleted successfully!")

            else:
                print("No result!")
                break

    elif choice == 2:
        print("Enter the name of the app you want to delete: ", end="")
        f.Search(my_df["track_name"])

        while True:
            print()
            idx = 0
            for i in f.list_search:
                idx += 1
                print(idx, i)

            if len(f.list_search) != 0:
                print("Enter 0 to exit")
                choice = int(
                    input(
                        "Enter the number corresponding to the app name you want to delete: "
                    )
                )

                if choice == 0:
                    break

                if choice < 0 or choice > len(f.list_search):
                    print("ERROR!")

                else:
                    idx_drop = my_df[
                        my_df["track_name"] == f.list_search[choice - 1]
                    ].index
                    my_df.drop(idx_drop, inplace=True)
                    f.list_search.remove(f.list_search[choice - 1])
                    print("Deleted successfully!")

            else:
                print("No result!")
                break

    else:
        print("ERROR!")
