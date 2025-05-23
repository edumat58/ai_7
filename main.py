import numpy as np
import pandas as pd
from sklearn

### TASK 1
ratings = pd.read_csv("ratings.csv")
ratings.head()

movies = pd.read_csv("movies.csv")
movies.head()

### TASK 2

n_ratings = len(ratings)
n_movies = len(ratings['movieId'].unique())
n_users = len(ratings['userId'].unique())

print("Number of ratings:", n_ratings)
print("Number of unique movieId's:", n_movies)
print("Number of unique users:", n_users)
print("Average ratings per user:", round(n_ratings/n_users, 2))
print("Average ratings per movie:", round(n_ratings/n_movies, 2))

### TASK 3

