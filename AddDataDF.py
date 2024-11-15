import pandas as pd

file_path = 'AppleStore.csv'
data = pd.read_csv(file_path)

print("Initial dataset:")
print(data.head())

# 1. CREATE a new row in the dataset
def add_new_row(data):
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

# 2. READ data from the dataset
def read_data(data):
    print()
    print("Reading dataset:")
    print(data.head())
    print(data.describe())

# Menu-driven interface for CREATE and READ operations
while True:
    print()
    print("0. Exit")
    print("3. Create")
    print("4. Read")
    
    choice = input("Choose your action: ").strip()

    if choice == '0':
        print("Exiting...")
        break
    elif choice == '3':
        data = add_new_row(data)
        print()
        print("Updated dataset with the new app entry:")
        print(data.tail())
    elif choice == '4':
        read_data(data)
    else:
        print("Invalid choice. Please enter 0, 3, or 4")
