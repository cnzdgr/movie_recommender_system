Datasets are taken from:
https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset
It contains 26m ratings from 270k users. 45k movies in total.
Movies are released on or before July 2017 (no recent movies).

Folders are:

movies_metadata.csv: 
Contains all metadata regarding movies. Title, overview(short description), original language are especially important.

keywords.csv:
contains all keyword tags that are relevant to the movie.

links.csv:
contains mapping of different movie Id's.
(i)movieId, (ii)ImdbId, (iii)tmdbId

credits.csv:
contains names of important cast members, and movie tags as stringfied JSON object

ratings.csv:
Ratings of users for movies in (1-5 scale).
Note: movieId column in this file is actually tmdbId.