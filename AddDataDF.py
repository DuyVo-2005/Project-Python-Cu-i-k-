import pandas as pd

file_path = 'AppleStore.csv'
data = pd.read_csv(file_path)

print("Initial dataset:")
print(data.head())

def add_new_row():
    new_app = {}
    new_app['id'] = int(input("Enter the app ID: "))
    new_app['track_name'] = input("Enter the app name: ")
    new_app['size_bytes'] = int(input("Enter the app size (in bytes): "))
    new_app['currency'] = input("Enter the currency: ")
    new_app['price'] = float(input("Enter the app price: "))
    new_app['rating_count_tot'] = int(input("Enter the total rating count: "))
    new_app['rating_count_ver'] = int(input("Enter the version rating count: "))
    new_app['user_rating'] = float(input("Enter the user rating: "))
    new_app['user_rating_ver'] = float(input("Enter the user rating for the version: "))
    new_app['ver'] = input("Enter the version: ")
    new_app['cont_rating'] = input("Enter the content rating: ")
    new_app['prime_genre'] = input("Enter the primary genre: ")
    new_app['sup_devices.num'] = int(input("Enter the number of supported devices: "))
    new_app['ipadSc_urls.num'] = int(input("Enter the number of iPad screenshots: "))
    new_app['lang.num'] = int(input("Enter the number of languages: "))
    new_app['vpp_lic'] = int(input("Enter the VPP license (0 or 1): "))

    new_app_df = pd.DataFrame(new_app, index=[0])
    return pd.concat([data, new_app_df], ignore_index=True)

def add_new_column():
    column_name = input("Enter the name of the new column: ")
    default_value = input("Enter the default value for the new column: ")
    
    data[column_name] = default_value
    return data

while True:
    choice = input("Do you want to add a new row or a new column? (Enter 'row' or 'column', or 'exit' to quit): ").strip().lower()
    
    if choice == 'row':
        data = add_new_row()
        print("\nUpdated dataset with the new app entry:")
        print(data.tail())
    elif choice == 'column':
        data = add_new_column()
        print("\nUpdated dataset with the new column:")
        print(data.tail())
    elif choice == 'exit':
        break
    else:
        print("Invalid choice. Please enter 'row', 'column', or 'exit'")