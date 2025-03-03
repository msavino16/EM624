# Author:  Michael Savino

#"I pledge my honor that i have abided by the Stevens Honor System"

# Exercise 04
# Pandas program

# This program will intake a 3 files and convert them to pandas dataframes

# The program is written by loading in each dataset, then doing data manipulation

import pandas as pd

print ("\n run by Michael Savino")
print ()

#Load the three datasets movies.csv, tags.csv, and ratings.csv into three pandas DataFrames
#Print the first 5 rows of each of the 3 DataFrames. Leave a blank line before each DataFrame listing and print an appropriate heading.

movies_df = pd.read_csv('movies.csv')
ratings_df = pd.read_csv('ratings.csv')
tags_df = pd.read_csv('tags.csv')

print()
print("First five rows for movies.csv")
print(movies_df.head())

print()
print("First five rows for ratings.csv")
print(ratings_df.head())

print()
print("First five rows for tags.csv")
print(tags_df.head())

print()

#Create a single pandas DataFrame containing movieid; title; genres (all from movies.csv); rating (from ratings.csv); tag (from tags.csv). Make sure every row is referring to the same movieid.

merged_df = pd.merge(movies_df, ratings_df, on='movieId', how='inner')
merged_df = pd.merge(merged_df, tags_df, on=['movieId', 'userId'], how='left')

#Count the number of movies with rating 5 and then print 10 of them (any 10). For each movie,
# print title, genres and tag.

five_rating_df = merged_df[merged_df['rating'] == 5.0]
print("\nNumber of movies with rating 5:", len(five_rating_df))
print(five_rating_df[['title', 'genres', 'tag']].sample(10))

# Count and print also the two most frequent genres with rating 5, with
#  their occurrences (that is the number of times they appear).

top_genre_df = []

for genres in five_rating_df['genres']:
    split_genres = genres.split('|')
    for genre in split_genres:
        top_genre_df.append(genre)


top_genre_series = pd.Series(top_genre_df)

top_genre_count = top_genre_series.value_counts().head(2)
print("\nTwo most frequent genres with rating 5:")
print(top_genre_count)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Count the number of movies with rating 0.5 and then print 10 of them (any 10). For each movie,
# print title, genres and tag.

zero_five_rating_df = merged_df[merged_df['rating'] == 0.5]
print("\nNumber of movies with rating 0.5:", len(zero_five_rating_df))
print(zero_five_rating_df[['title', 'genres', 'tag']].sample(10))

# Count and print also the two most frequent genres with rating 0.5, with
#  their occurrences (that is the number of times they appear).

bottom_genre_df = []

for genres in zero_five_rating_df['genres']:
    split_genres = genres.split('|')
    for genre in split_genres:
        bottom_genre_df.append(genre)


bottom_genre_series = pd.Series(bottom_genre_df)

bottom_genre_count = bottom_genre_series.value_counts().head(2)
print("\nTwo most frequent genres with rating 0.5:")
print(bottom_genre_count)


#Print the 5 most frequent tags with the genres they are related to. For each tag, print tag, genre and count.

tag_genre_df = merged_df[['tag', 'genres']]
tag_counts = tag_genre_df['tag'].value_counts().head(5)

print("\nTop 5 most frequent tags with related genres:")
for tag in tag_counts.index:
    related_genres = tag_genre_df[tag_genre_df['tag'] == tag]['genres']
    
    genre_list = []
    for genre_string in related_genres:
        split_genres = genre_string.split('|')
        for genre in split_genres:
            genre_list.append(genre)
    
    genre_series = pd.Series(genre_list)
    genre_count = genre_series.value_counts()
    
    print(f"Tag: {tag}")
    print(f"Genres:\n{genre_count}")
    print(f"Count: {tag_counts[tag]}")
    print()

print('\nThanks for using this tool!\n')
 