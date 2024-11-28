import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import data_cleaning
import data_normalization

# load the dataset
df = pd.read_csv("AppleStore.csv")

# clean missing data
data_cleaning.start_cleaning(df)

# normalize the data for better visualization
df = data_normalization.normalize_data(df)


# visualization Functions
# distribution of App Genres
def plot_genre_distribution(df):
    """
    Visualizes the distribution of app genres
    """
    genre_counts = df["prime_genre"].value_counts()
    plt.figure(figsize=(10, 6))
    plt.bar(genre_counts.index, genre_counts.values, color="skyblue")
    plt.title("Distribution of App Genres")
    plt.xlabel("Genre")
    plt.ylabel("Number of Apps")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# distribution of Total Ratings
def plot_rating_distribution(df):
    """
    Visualizes the distribution of total ratings
    """
    plt.figure(figsize=(10, 6))
    plt.hist(df["rating_count_tot"], bins=50, color="orange", edgecolor="black")
    plt.title("Distribution of Total Ratings")
    plt.xlabel("Total Ratings (normalized)")
    plt.ylabel("Frequency")
    plt.yscale("log")  # use log scale for better visualization
    plt.show()


# average User Rating by Genre
def plot_avg_rating_by_genre(df):
    """
    Visualizes the average user rating for each app genre
    """
    avg_rating_by_genre = df.groupby("prime_genre")["user_rating"].mean().sort_values()
    plt.figure(figsize=(12, 8))
    avg_rating_by_genre.plot(kind="barh", color="coral", edgecolor="black")
    plt.title("Average User Rating by Genre")
    plt.xlabel("Average Rating")
    plt.ylabel("Genre")
    plt.show()


# total Ratings by Genre
def plot_total_ratings_by_genre(df):
    """
    Visualizes the total number of ratings for each genre
    """
    total_rating_by_genre = (
        df.groupby("prime_genre")["rating_count_tot"].sum().sort_values()
    )
    plt.figure(figsize=(12, 8))
    total_rating_by_genre.plot(kind="barh", color="teal", edgecolor="black")
    plt.title("Total Ratings by Genre")
    plt.xlabel("Total Ratings")
    plt.ylabel("Genre")
    plt.show()


# average Price by Genre
def plot_avg_price_by_genre(df):
    """
    Visualizes the average app price for each genre
    """
    avg_price_by_genre = df.groupby("prime_genre")["price"].mean().sort_values()
    plt.figure(figsize=(12, 8))
    avg_price_by_genre.plot(kind="barh", color="blue", edgecolor="black")
    plt.title("Average Price by Genre")
    plt.xlabel("Average Price (USD)")
    plt.ylabel("Genre")
    plt.show()


# number of Apps by Content Rating
def plot_apps_by_content_rating(df):
    """
    Visualizes the distribution of apps by content rating
    """
    content_rating_counts = df["cont_rating"].value_counts()
    plt.figure(figsize=(10, 6))
    content_rating_counts.plot(kind="bar", color="cyan", edgecolor="black")
    plt.title("Number of Apps by Content Rating")
    plt.xlabel("Content Rating")
    plt.ylabel("Number of Apps")
    plt.show()


# free vs Paid Apps by Top Genres
def plot_free_vs_paid_by_genre(df, top_n=5):
    """
    Visualizes the percentage of free vs. paid apps in the top N genres
    """
    # Identify the top N genres by app count
    top_genres = df["prime_genre"].value_counts().index[:top_n]

    # Filter data to include only apps in the top N genres
    df_top = df[df["prime_genre"].isin(top_genres)]

    # Calculate the distribution of free and paid apps by genre
    genre_paid_free = (
        df_top.groupby(["prime_genre", df_top["price"] == 0])
        .size()
        .unstack(fill_value=0)
    )
    genre_paid_free.columns = ["Paid", "Free"]
    genre_paid_free["Free %"] = (
        genre_paid_free["Free"] / genre_paid_free.sum(axis=1)
    ) * 100
    genre_paid_free["Paid %"] = (
        genre_paid_free["Paid"] / genre_paid_free.sum(axis=1)
    ) * 100

    # Plot pie charts for each genre
    fig, axes = plt.subplots(1, top_n, figsize=(20, 5))
    for ax, genre in zip(axes, top_genres):
        data = genre_paid_free.loc[genre, ["Free %", "Paid %"]]
        ax.pie(
            data,
            labels=["Free %", "Paid %"],
            autopct="%1.1f%%",
            startangle=90,
            colors=["green", "gold"],
        )
        ax.set_title(genre)

    # Set a global title and adjust layout
    plt.suptitle("Percentage of Free vs Paid Apps by Top Genres", fontsize=16)
    plt.tight_layout()
    plt.show()


# Biểu đồ 3: Phân phối kích thước ứng dụng
def plot_sizebytes_distribution(df):
    """
    Visualizes the distribution of app size
    """
    plt.figure(figsize=(10, 6))
    plt.hist(df["size_bytes"], bins=50, color="green", edgecolor="black")
    plt.title("Distribution of App Sizes")
    plt.xlabel("App Size (bytes)")
    plt.ylabel("Frequency")
    plt.xscale("log")  # Sử dụng thang log
    plt.show()


def console():
    while True:
        print("0. Exit")
        print("1. Graph for genre distribution")
        print("2. Graph for rating distribution")
        print("3. Graph for average rating by genre")
        print("4. Graph for total ratings by genre")
        print("5. Graph for average price by genre")
        print("6. Graph for apps by content rating")
        print("7. Graph for free vs paid by genre")
        print("8. Graph for size bytes distribution")
        choice = int(input("Your choice: "))

        if choice == 0:
            break

        elif choice == 1:
            plot_genre_distribution(df)

        elif choice == 2:
            plot_rating_distribution(df)

        elif choice == 3:
            plot_avg_rating_by_genre(df)

        elif choice == 4:
            plot_total_ratings_by_genre(df)

        elif choice == 5:
            plot_avg_price_by_genre(df)

        elif choice == 6:
            plot_apps_by_content_rating(df)

        elif choice == 7:
            plot_free_vs_paid_by_genre(df, top_n=5)

        else:
            plot_sizebytes_distribution(df)
