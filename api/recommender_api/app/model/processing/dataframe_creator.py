'''
Creates required dataframes by combining datasets
and deleting unnecessary columns
'''

import os
import sys
import pandas as pd
from pathlib import Path
from typing import List

# Adding the ROOT path 
d = os.getcwd()
par_3 = os.path.dirname(os.path.dirname(os.path.dirname(d)))
sys.path.append(par_3)

from app.model.model_config import config
from app.model.processing.data_manager import load_dataset

def metadata_df() -> pd.DataFrame:
    '''A single dataframe containing all required movie metadata'''
    
    # Reading the main metadata file and keeping only related columns
    df_meta = load_dataset(file_name=config.a_config.metadata_file)
    df_meta = df_meta[['adult', 'genres', 'id', 'imdb_id', 'original_language', 'original_title', 'overview', 'runtime', 'title', 'vote_average', 'vote_count']]
    df_meta.rename(columns={'id': 'tmdbId'}, inplace=True)
    df_meta.rename(columns={'imdb_id': 'imdbId'})
    df_meta["tmdbId"] =pd.to_numeric(df_meta['tmdbId'], errors='coerce',downcast="integer")
        
    df_links = load_dataset(file_name=config.a_config.links_file)
    df_links = df_links[['movieId', 'tmdbId']]
    df_meta = pd.merge(df_links, df_meta, how='inner', on='tmdbId')
    df_meta["movieId"] =pd.to_numeric(df_meta['movieId'], errors='coerce',downcast="integer")
    df_meta.dropna(subset=["movieId", "tmdbId", "overview"],inplace=True)

    df_keywords = load_dataset(file_name=config.a_config.keywords_file)
    df_keywords.rename(columns={'id': 'tmdbId'}, inplace=True)
    df_meta = pd.merge(df_meta, df_keywords, how='left', on='tmdbId')
    
    return df_meta


def less_voted_movies():
    df = metadata_df()
    less_voted = df[df['vote_count'] < 200]
    less_voted = less_voted['movieId']
    return less_voted
    

def rating_df() -> pd.DataFrame:
    '''A single dataframe containing movie ratings'''
    
    less_voted = less_voted_movies()
    less_voted = less_voted.values.tolist()
    
    df = load_dataset(file_name=config.a_config.ratings_file)
    df = df[['userId', 'movieId',  'rating']]
    df = df[~df['movieId'].isin(less_voted)]
    print("len is:", len(df))
    return df

def rating_matrix():
    
    df = rating_df()
    df_matrix =  df[['userId', 'movieId', 'rating']]
    rating_matrix = df_matrix.pivot_table(index='movieId',  columns='userId', values='rating')
    return rating_matrix

a = rating_matrix()
#a.to_csv("trial.csv")
