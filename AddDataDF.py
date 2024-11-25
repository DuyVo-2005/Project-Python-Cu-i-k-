import pandas as pd

file_path = "AppleStore.csv"
my_df = pd.read_csv(file_path)

print("Initial dataset:")
print(my_df.head(10))

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
            print(f"Error: Invalid input. Expected a value of type {expected_type.__name__}. Please try again")

# 1. CREATE a new row in the data set
def add_new_row(my_df, file_path):
    print("\nEnter the details for the new app:")
    new_app = {
        'id': get_valid_input("Enter the app ID (integer): ", int),
        'track_name': input("Enter the app name: "),
        'size_bytes': get_valid_input("Enter the app size (in bytes, integer): ", int),
        'currency': input("Enter the currency: "),
        'price': get_valid_input("Enter the app price (float): ", float),
        'rating_count_tot': get_valid_input("Enter the total rating count (integer): ", int),
        'user_rating': get_valid_input("Enter the user rating (float, 0.0 - 5.0): ", float),
        'user_rating_ver': get_valid_input("Enter the user rating for the version (float, 0.0 - 5.0): ", float),
        'ver': input("Enter the version: "),
        'cont_rating': input("Enter the content rating: "),
        'prime_genre': input("Enter the primary genre: "),
        'sup_devices.num': get_valid_input("Enter the number of supported devices (integer): ", int)
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

my_df = add_new_row(my_df, file_path)
read_data(my_df)
