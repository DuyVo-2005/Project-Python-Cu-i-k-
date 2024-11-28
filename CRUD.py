import pandas as pd
import search_function_for_console as f

file_path = "AppleStore.csv"
my_df = pd.read_csv(file_path)
my_df = my_df.loc[:, ~my_df.columns.str.contains("^Unnamed")]


# function to check input data type and request re-entry if incorrect
def get_valid_input(prompt, expected_type, allowed_values=None):
    while True:
        user_input = input(prompt)
        try:
            value = expected_type(user_input)
            if allowed_values and value not in allowed_values:
                print(f"Error: Value must be one of {allowed_values}. Please try again")
                continue
            return value
        except ValueError:
            print(
                f"Error: Invalid input. Expected a value of type {expected_type.__name__}. Please try again"
            )


# 1. CREATE a new row in the data set
def add_new_row(my_df, file_path):
    print("\nEnter the details for the new app:")
    new_app = {
        "id": get_valid_input("Enter the app ID (integer): ", int),
        "track_name": input("Enter the app name: "),
        "size_bytes": get_valid_input("Enter the app size (in bytes, integer): ", int),
        "currency": input("Enter the currency: "),
        "price": get_valid_input("Enter the app price (float): ", float),
        "rating_count_tot": get_valid_input(
            "Enter the total rating count (integer): ", int
        ),
        "user_rating": get_valid_input(
            "Enter the user rating (float, 0.0 - 5.0): ", float
        ),
        "user_rating_ver": get_valid_input(
            "Enter the user rating for the version (float, 0.0 - 5.0): ", float
        ),
        "ver": input("Enter the version: "),
        "cont_rating": input("Enter the content rating: "),
        "prime_genre": input("Enter the primary genre: "),
        "sup_devices.num": get_valid_input(
            "Enter the number of supported devices (integer): ", int
        ),
    }

    # create DataFrame from new application and merge into current DataFrame
    new_app_df = pd.DataFrame(new_app, index=[0])
    updated_df = pd.concat([my_df, new_app_df], ignore_index=True)

    # save data
    updated_df.to_csv(file_path, index=False)
    print(f"Dataset updated and saved to {file_path}")
    return updated_df


# 2. read data from the my_dfset
def read_data(my_df):
    print()
    print("Reading dataset:")
    print(my_df.head(10))
    print(my_df.describe())


# 3. Update the information of the app
def Update(my_df):
    """Update columns except no. columns from the DataFrame that the user selects from the menu"""
    # Menu
    while True:
        f.Search(my_df)

        if f.choice == 0:
            break

        if f.c == "0":
            break
        else:

            # Show app in list search for user to choice
            while True:
                print()
                idx = 0
                for i in f.list_search:
                    idx += 1
                    print(idx, i)

                if len(f.list_search) != 0:
                    print("Enter 0 to exit")
                    choice_2 = int(
                        input(
                            "Enter the number corresponding to the app name you want to update: "
                        )
                    )

                    if choice_2 == 0:
                        break

                    if choice_2 < 0 or choice_2 > len(f.list_search):
                        print("ERROR!")
                    else:

                        # Get the row index of the selected app
                        idx_drop = my_df[
                            my_df["track_name"] == f.list_search[choice_2 - 1]
                        ].index

                        # Show option for user to choice
                        while True:
                            app_row = my_df.loc[idx_drop]

                            index = 0
                            print()
                            for column in app_row.columns:
                                index += 1
                                print(f"{index} {column}: {app_row.iloc[0][column]}")

                            print("Enter 0 to exit")
                            choice_3 = int(
                                input(
                                    "Enter the number corresponding to the information of the app you want to update: "
                                )
                            )

                            if choice_3 == 0:
                                break

                            if choice_3 < 1 or choice_3 > len(my_df.columns):
                                print("ERROR!")
                            else:

                                # Update new information with the selected column
                                column_to_update = my_df.columns[choice_3 - 1]
                                dtype = my_df[column_to_update].dtype

                                while True:
                                    try:
                                        new_value = input(
                                            f"Enter the new information for '{column_to_update}' (type: {dtype}): "
                                        )
                                        if pd.api.types.is_integer_dtype(dtype):
                                            new_value = int(new_value)
                                        elif pd.api.types.is_float_dtype(dtype):
                                            new_value = float(new_value)
                                        elif pd.api.types.is_string_dtype(dtype):
                                            if column_to_update == "currency":
                                                if not new_value.isalpha():
                                                    raise ValueError(
                                                        "Value must only contain letters"
                                                    )
                                                else:
                                                    new_value = str(new_value)
                                            if column_to_update == "cont_rating":
                                                if (
                                                    not new_value.isdigit()
                                                    and not new_value.endswith("+")
                                                ):
                                                    raise ValueError(
                                                        "Value must only contain numbers and '+'"
                                                    )
                                                else:
                                                    new_value = str(new_value)
                                            new_value = str(new_value)
                                        else:
                                            raise ValueError(
                                                f"Unsupported data type: {dtype}"
                                            )
                                        my_df.loc[idx_drop, column_to_update] = (
                                            new_value
                                        )
                                        break
                                    except ValueError as e:
                                        print(
                                            f"Invalid input! Please enter a value of type {dtype}. Error: {e}"
                                        )

                                # Check if column_to_update is "track_name": update list search
                                if column_to_update == "track_name":
                                    if f.c.lower() not in new_value.lower():
                                        f.list_search.remove(
                                            f.list_search[choice_2 - 1]
                                        )
                                    else:
                                        f.list_search[choice_2 - 1] = new_value

                                # Overwrite the file and update list search
                                my_df.to_csv("AppleStore.csv")
                                print("Updated successfully!")
                else:
                    print("No result!")
                    break


# 4. Delete row
def Delete(my_df):
    """Allows the user to delete an app from the DataFrame by selecting it from a menu"""
    # Menu
    while True:
        f.Search(my_df)

        if f.choice == 0:
            break

        if f.c == "0":
            break

        else:
            while True:

                # Show app in list search for user to choice
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

                        # Delete the row with the selected app name
                        idx_drop = my_df[
                            my_df["track_name"] == f.list_search[choice - 1]
                        ].index
                        my_df.drop(idx_drop, inplace=True)

                        # Overwrite the file and update list search
                        my_df.to_csv("AppleStore.csv")
                        f.list_search.remove(f.list_search[choice - 1])
                        print("Deleted successfully!")

                else:
                    print("No result!")
                    break


def console():
    while True:
        print()
        print("0. Exit")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        choice_user = int(input("Your choice: "))

        if choice_user == 0:
            break

        elif choice_user == 1:
            add_new_row(my_df, file_path)

        elif choice_user == 2:
            read_data(my_df)

        elif choice_user == 3:
            Update(my_df)

        elif choice_user == 4:
            Delete(my_df)
            
        else:
            print("ERROR!")
