import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from DataCleaning import check_missing_value, fill_na_value
from module_for_data_normalization import normalize_data

df = pd.read_csv("AppleStore.csv")

# làm sạch dữ liệu
df = fill_na_value(df)

# chuẩn hóa dữ liệu
df = normalize_data(df)

# phân tích trực quan hóa dữ liệu
# Biểu đồ 1: phân phối thể loại ứng dụng
def plot_genre_distribution(df):
    genre_counts = df['prime_genre'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.bar(genre_counts.index, genre_counts.values, color='skyblue')
    plt.title('Distribution of App Genres')
    plt.xlabel('Genre')
    plt.ylabel('Number of Apps')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Biểu đồ 2: phân phối số lượt đánh giá
def plot_rating_distribution(df):
    plt.figure(figsize=(10, 6))
    plt.hist(df['rating_count_tot'], bins=50, color='orange', edgecolor='black')
    plt.title('Distribution of Total Ratings')
    plt.xlabel('Total Ratings (normalized)')
    plt.ylabel('Frequency')
    plt.yscale('log')  # Sử dụng thang log
    plt.show()

# Biểu đồ 3: phân phối đánh giá trung bình
def plot_user_rating_distribution(df):
    plt.figure(figsize=(10, 6))
    plt.hist(df['user_rating'], bins=5, color='purple', edgecolor='black')
    plt.title('Distribution of User Ratings')
    plt.xlabel('User Rating')
    plt.ylabel('Frequency')
    plt.show()

# Biểu đồ 4: đánh giá trung bình theo thể loại
def plot_avg_rating_by_genre(df):
    avg_rating_by_genre = df.groupby('prime_genre')['user_rating'].mean().sort_values()
    plt.figure(figsize=(12, 8))
    avg_rating_by_genre.plot(kind='barh', color='coral', edgecolor='black')
    plt.title('Average User Rating by Genre')
    plt.xlabel('Average Rating')
    plt.ylabel('Genre')
    plt.show()

# Biểu đồ 5: tổng số lượt đánh giá theo thể loại
def plot_total_ratings_by_genre(df):
    total_rating_by_genre = df.groupby('prime_genre')['rating_count_tot'].sum().sort_values()
    plt.figure(figsize=(12, 8))
    total_rating_by_genre.plot(kind='barh', color='teal', edgecolor='black')
    plt.title('Total Ratings by Genre')
    plt.xlabel('Total Ratings')
    plt.ylabel('Genre')
    plt.show()

# Biểu đồ 6: giá trung bình theo thể loại
def plot_avg_price_by_genre(df):
    avg_price_by_genre = df.groupby('prime_genre')['price'].mean().sort_values()
    plt.figure(figsize=(12, 8))
    avg_price_by_genre.plot(kind='barh', color='blue', edgecolor='black')
    plt.title('Average Price by Genre')
    plt.xlabel('Average Price (USD)')
    plt.ylabel('Genre')
    plt.show()

# Biểu đồ 7: số ứng dụng theo xếp hạng nội dung
def plot_apps_by_content_rating(df):
    content_rating_counts = df['cont_rating'].value_counts()
    plt.figure(figsize=(10, 6))
    content_rating_counts.plot(kind='bar', color='cyan', edgecolor='black')
    plt.title('Number of Apps by Content Rating')
    plt.xlabel('Content Rating')
    plt.ylabel('Number of Apps')
    plt.show()

# Biểu đồ 8: tỷ lệ ứng dụng miễn phí so với trả phí theo 5 thể loại hàng đầu
def plot_free_vs_paid_by_genre(df, top_n=5):
    # Chọn N thể loại hàng đầu theo số lượng ứng dụng
    top_genres = df['prime_genre'].value_counts().index[:top_n]

    # Lọc dữ liệu cho các thể loại hàng đầu
    df_top = df[df['prime_genre'].isin(top_genres)]

    # Tính phần trăm cho các ứng dụng miễn phí và trả phí
    genre_paid_free = df_top.groupby(['prime_genre', df_top['price'] == 0]).size().unstack(fill_value=0)
    genre_paid_free['free %'] = (genre_paid_free[True] / genre_paid_free.sum(axis=1)) * 100
    genre_paid_free['paid %'] = (genre_paid_free[False] / genre_paid_free.sum(axis=1)) * 100

    # Tạo biểu đồ hình tròn
    fig, axes = plt.subplots(1, top_n, figsize=(20, 5))
    for ax, genre in zip(axes, top_genres):
        data = genre_paid_free.loc[genre, ['free %', 'paid %']]
        ax.pie(data, labels=['Free %', 'Paid %'], autopct='%1.1f%%', startangle=90, colors=['green', 'gold'])
        ax.set_title(genre)

    plt.suptitle("Percentage of Free vs Paid Apps by Top Genres", fontsize=16)
    plt.tight_layout()
    plt.show()

# Biểu đồ 9: tỷ lệ các ứng dụng theo số thiết bị hỗ trợ
def plot_apps_by_supported_devices(df):
    device_support_counts = df['sup_devices.num'].value_counts().sort_index()
    plt.figure(figsize=(10, 6))
    device_support_counts.plot(kind='bar', color='gold', edgecolor='black')
    plt.title('Number of Apps by Supported Devices')
    plt.xlabel('Number of Supported Devices')
    plt.ylabel('Number of Apps')
    plt.show()
    
plot_genre_distribution(df)
plot_rating_distribution(df)
plot_user_rating_distribution(df)
plot_avg_rating_by_genre(df)
plot_total_ratings_by_genre(df)
plot_avg_price_by_genre(df)
plot_apps_by_content_rating(df)
plot_free_vs_paid_by_genre(df, top_n=5)
plot_apps_by_supported_devices(df)
