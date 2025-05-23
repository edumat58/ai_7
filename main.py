import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

### TASK 1
print("=" * 50)
print("TASK 1: Load the datasets")
print("-" * 50)
# TO DO:
# Load "ratings.csv" and "movies.csv" from the "data" directory using pandas.
# ratings should contain userId, movieId, rating, timestamp
# movies should contain movieId, title, genres

### TASK 2
print("=" * 50)
print("TASK 2: Describe the dataset")
print("-" * 50)
# TO DO:
# - How many ratings are there?
# - How many unique movies?
# - How many unique users?
# - Average ratings per user?
# - Average ratings per movie?

print("Number of ratings:", n_ratings)
print("Number of unique movieId's:", n_movies)
print("Number of unique users:", n_users)
print("Average ratings per user:", round(n_ratings/n_users, 2))
print("Average ratings per movie:", round(n_ratings/n_movies, 2))

### TASK 3
print("=" * 50)
print("TASK 3: User frequency")
print("-" * 50)
# TO DO:
# Count how many ratings each user has made

user_freq.head()
print(user_freq.head())

### TASK 4
print("=" * 50)
print("TASK 4: Average rating per movie")
print("-" * 50)
# TO DO:
# Calculate the average rating for each movie

print(mean_rating)

### TASK 5
print("=" * 50)
print("TASK 5: Find best and worst rated movies")
print("-" * 50)
# TO DO:
# - Find the movieId of the movie with lowest average rating
# - Find the movieId of the movie with highest average rating
# - Use the movieId to get the title and genres from the movies dataset

# Lowest rated movies
print("Lowest rated movie:", lowest_rated)
print("Title:", lowest_rated_movie['title'])
print("Genres:", lowest_rated_movie['genres'])

# Highest rated movies
print("Highest rated movie:", highest_rated)
print("Title:", highest_rated_movie['title'])
print("Genres:", highest_rated_movie['genres'])

### TASK 6
print("=" * 50)
print("TASK 6: Compute movie statistics")
print("-" * 50)
# TO DO:
# For each movieId, compute the number of ratings and the average rating

### TASK 7
print("=" * 50)
print("TASK 7: Create the sparse rating matrix")
print("-" * 50)
# TO DO:
# - Map userId and movieId to matrix indices
# - Build a sparse matrix where rows are movies and columns are users

### TASK 8
print("=" * 50)
print("TASK 8: KNN Recommendation Function")
print("-" * 50)
# TO DO:
# Write a function that:
# - receives a movieId, the matrix, k (number of neighbors)
# - returns a list of similar movieIds based on cosine similarity

### TASK 9
print("=" * 50)
print("TASK 9: Run recommendation")
print("-" * 50)
# TO DO:
# - Create a dictionary from movieId to title
# - Ask user to input a movie title
# - Get the movieId and run the KNN function to get recommendations
# - Print the recommended titles

