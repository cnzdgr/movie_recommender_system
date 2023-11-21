'''
Creates required dataframes by combining datasets
and deleting unnecessary columns
'''
import os
import sys
import numpy as np
import pandas as pd
from ast import literal_eval
from collections import Counter

# Adding the ROOT path 
d = os.getcwd()
par_3 = os.path.dirname(os.path.dirname(os.path.dirname(d)))
sys.path.append(par_3)

from app.model.model_config import config
from app.model.processing.data_manager import load_dataset, save_dataframe


def metadata_df() -> pd.DataFrame:
    '''A single dataframe containing all required movie metadata'''
    
    # Reading the main metadata file and keeping only related columns
    df_meta = load_dataset(file_name=config.a_config.metadata_file)
    df_meta = df_meta[config.m_config.metadata_vars]
    df_meta.rename(columns={'id': 'tmdbId'}, inplace=True)
    df_meta[config.m_config.main_key_value] =pd.to_numeric(df_meta[config.m_config.main_key_value], errors='coerce',downcast="integer")
    
    # Reading links file to get movieId for each movie
    df_links = load_dataset(file_name=config.a_config.links_file)
    df_links = df_links[config.m_config.link_vars]
    # Merging with the main df_meta
    df_meta = pd.merge(df_links, df_meta, how='inner', on=config.m_config.main_key_value)
    df_meta["movieId"] =pd.to_numeric(df_meta['movieId'], errors='coerce',downcast="integer")
    df_meta.dropna(subset=config.m_config.feature_to_must_have,inplace=True)

    # Reading keywords file and merging keywords with the main df
    df_keywords = load_dataset(file_name=config.a_config.keywords_file)
    df_keywords.rename(columns={'id': 'tmdbId'}, inplace=True)
    df_meta = pd.merge(df_meta, df_keywords, how='left', on=config.m_config.main_key_value)
    
    return df_meta


def clean_metadata_df(df_meta: pd.DataFrame) ->pd.DataFrame:
    '''
    Clean the keywords column by taking required value from the list of dictionaries
    And drop duplicate rows, if any
    '''
    df_meta_clean = df_meta
    df_meta_clean['keywords'] = df_meta_clean['keywords'].apply(lambda x: req_string(x))

    df_meta_clean['keywords'] = df_meta_clean['keywords'].apply(get_list)
    df_meta_clean.drop_duplicates(subset=['movieId'], inplace=True)

    return df_meta_clean

def overview_df(df_meta:pd.DataFrame) -> pd.DataFrame:
    less_voted = less_voted_movies(metadata_df())

    df_overview = df_meta[['movieId', 'original_title', 'overview']]
    df_overview = df_overview[~df_overview['movieId'].isin(less_voted)]
    return df_overview


def movie_name_mapper(df: pd.DataFrame) ->pd.DataFrame:
    return df[['movieId', 'original_title']]


def rating_df() -> pd.DataFrame:
    '''A single dataframe containing movie ratings'''
    
    # Checks less voted movies
    less_voted = less_voted_movies(metadata_df())
    
    df = load_dataset(file_name=config.a_config.ratings_file)
    df = df[['userId', 'movieId',  'rating']]
    df = df[~df['movieId'].isin(less_voted)]
    df = less_active_voters_filter(df)
    return df


def rating_matrix_id(rating_df):  
    rating_matrix = rating_df.pivot_table(index='movieId',  columns='userId', values='rating')
    return rating_matrix


def rating_matrix_name(rating_df):
    metadata = metadata_df()
    metadata = metadata[['movieId', 'original_title']]
    rating_matrix = pd.merge(rating_df, metadata, on="movieId",how="inner")
    rating_matrix.drop(['movieId'], axis=1, inplace=True)
    rating_matrix = rating_matrix.pivot_table(index='original_title', columns='userId', values='rating')
    return rating_matrix


def filled_rating_matrix(rat_matrix):
    rating_matrix_filled = rat_matrix.apply(lambda row: row.fillna(0), axis=1)
    return rating_matrix_filled

# ------------------- HELPER FUNCTIONS ----------------------
# Clean list of dictionaries (JSON) and create a list taking name keys
def get_list(x):
    if isinstance(x, list):
        names = [i['name'] for i in x]
        return names
    #Return empty list in case of missing/malformed data
    return []


# To prevent literal_eval raise an Exception and crash - for exception handling
def req_string(x):
    try:
        return literal_eval(str(x))   
    except Exception as e:
        return []
    
    
def less_voted_movies(df: pd.DataFrame) -> list:
    '''Eliminate movies that have less than specified votes(not famous)'''
    less_voted = df[df['vote_count'] < config.m_config.vote_count_lower_bound]
    less_voted = less_voted['movieId']
    return less_voted.tolist()


def less_active_voters_filter(df: pd.DataFrame) -> list:
    '''Eliminate voters that has voted for less than the specified amount'''
    user_groupby = pd.Series(Counter(df['userId']))
    freq_voters = user_groupby.loc[lambda x : x > config.m_config.voter_min_vote]
    freq_voters = np.array(freq_voters.index)
    df = df[df['userId'].isin(freq_voters)]
    return df

# ------------------- HELPER FUNCTIONS ----------------------

def create_all_dataframes():
    '''Creates all required dataframes'''
    metadata_frame = metadata_df()
    clean_metadata_frame = clean_metadata_df(metadata_frame)
    save_dataframe(df=clean_metadata_frame, df_name="metadata.csv")
    
    overview_frame = overview_df(metadata_frame)
    save_dataframe(df=overview_frame, df_name="overview.csv")
    
    ratings_df = rating_df()
    rating_mtx_id = rating_matrix_id(ratings_df)
    filled_mtx_id = filled_rating_matrix(rating_mtx_id)
    save_dataframe(df=filled_mtx_id, df_name="rating_matrix_id.csv")
    
    movie_name_map = movie_name_mapper(metadata_frame)
    save_dataframe(df=movie_name_map, df_name="movie_map.csv")
        
    '''
    # Currently not required
    rating_mtx_names = rating_matrix_name(ratings_df)
    filled_mtx_names = filled_rating_matrix(rating_mtx_names)
    save_dataframe(df=filled_mtx_names, df_name="rating_matrix_names.csv")
    '''
    
if __name__ == "__main__":
    create_all_dataframes()


    