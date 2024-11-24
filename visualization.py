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

# Biểu đồ 3: phân phối kích thước ứng dụng
def plot_size_distribution(df):
    plt.figure(figsize=(10, 6))
    plt.hist(df['size_bytes'], bins=50, color='green', edgecolor='black')
    plt.title('Distribution of App Sizes')
    plt.xlabel('App Size (normalized)')
    plt.ylabel('Frequency')
    plt.xscale('log')  # Sử dụng thang log
    plt.show()

# Biểu đồ 4: phân phối đánh giá trung bình
def plot_user_rating_distribution(df):
    plt.figure(figsize=(10, 6))
    plt.hist(df['user_rating'], bins=5, color='purple', edgecolor='black')
    plt.title('Distribution of User Ratings')
    plt.xlabel('User Rating')
    plt.ylabel('Frequency')
    plt.show()

# Biểu đồ 5: đánh giá trung bình theo thể loại
def plot_avg_rating_by_genre(df):
    avg_rating_by_genre = df.groupby('prime_genre')['user_rating'].mean().sort_values()
    plt.figure(figsize=(12, 8))
    avg_rating_by_genre.plot(kind='barh', color='coral', edgecolor='black')
    plt.title('Average User Rating by Genre')
    plt.xlabel('Average Rating')
    plt.ylabel('Genre')
    plt.show()

# HBiểu đồ 6: tổng số lượt đánh giá theo thể loại
def plot_total_ratings_by_genre(df):
    total_rating_by_genre = df.groupby('prime_genre')['rating_count_tot'].sum().sort_values()
    plt.figure(figsize=(12, 8))
    total_rating_by_genre.plot(kind='barh', color='teal', edgecolor='black')
    plt.title('Total Ratings by Genre')
    plt.xlabel('Total Ratings')
    plt.ylabel('Genre')
    plt.show()

# Biểu đồ 7: giá trung bình theo thể loại
def plot_avg_price_by_genre(df):
    avg_price_by_genre = df.groupby('prime_genre')['price'].mean().sort_values()
    plt.figure(figsize=(12, 8))
    avg_price_by_genre.plot(kind='barh', color='blue', edgecolor='black')
    plt.title('Average Price by Genre')
    plt.xlabel('Average Price (USD)')
    plt.ylabel('Genre')
    plt.show()

# Biểu đồ 8: số ứng dụng theo xếp hạng nội dung
def plot_apps_by_content_rating(df):
    content_rating_counts = df['cont_rating'].value_counts()
    plt.figure(figsize=(10, 6))
    content_rating_counts.plot(kind='bar', color='cyan', edgecolor='black')
    plt.title('Number of Apps by Content Rating')
    plt.xlabel('Content Rating')
    plt.ylabel('Number of Apps')
    plt.show()

# Biểu đồ 9: tỷ lệ ứng dụng miễn phí so với trả phí theo 5 thể loại hàng đầu
def plot_free_vs_paid_by_top_5_genres(df):
    top_5_genres = df['prime_genre'].value_counts().index[:5]
    df_top_5 = df[df['prime_genre'].isin(top_5_genres)]
    genre_paid_free_top_5 = df_top_5.groupby(['prime_genre', 'is_free']).size().unstack(fill_value=0)
    genre_paid_free_top_5['free %'] = (genre_paid_free_top_5[True] / genre_paid_free_top_5.sum(axis=1)) * 100
    genre_paid_free_top_5['paid %'] = (genre_paid_free_top_5[False] / genre_paid_free_top_5.sum(axis=1)) * 100

    fig, axes = plt.subplots(1, 5, figsize=(20, 5))
    for ax, genre in zip(axes, top_5_genres):
        data = genre_paid_free_top_5.loc[genre, ['free %', 'paid %']]
        ax.pie(data, labels=data.index, autopct='%1.1f%%', startangle=90, colors=['green', 'gold'])
        ax.set_title(genre)
    plt.suptitle("Percentage of Free vs Paid Apps by Top 5 Genres", fontsize=16)
    plt.tight_layout()
    plt.show()

# Biểu đồ 10: tỷ lệ các ứng dụng theo số thiết bị hỗ trợ
def plot_apps_by_supported_devices(df):
    device_support_counts = df['sup_devices.num'].value_counts().sort_index()
    plt.figure(figsize=(10, 6))
    device_support_counts.plot(kind='bar', color='gold', edgecolor='black')
    plt.title('Number of Apps by Supported Devices')
    plt.xlabel('Number of Supported Devices')
    plt.ylabel('Number of Apps')
    plt.show()
