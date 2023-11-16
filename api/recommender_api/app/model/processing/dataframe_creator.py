'''
Creates required dataframes by combining datasets
and deleting unnecessary columns
'''
import os
import sys
import numpy as np
import pandas as pd
from collections import Counter
from ast import literal_eval

# Adding the ROOT path 
d = os.getcwd()
par_3 = os.path.dirname(os.path.dirname(os.path.dirname(d)))
sys.path.append(par_3)

from app.model.model_config import config
from app.model.model_config import DATAFRAME_DIR, TRAINED_MODEL_DIR, config
from app.model.processing.data_manager import load_dataset


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
    #df_meta_clean.drop_duplicates(inplace=True)

    return df_meta_clean


def rating_df() -> pd.DataFrame:
    '''A single dataframe containing movie ratings'''
    
    # Checks less voted movies
    less_voted = less_voted_movies(metadata_df())
    
    df = load_dataset(file_name=config.a_config.ratings_file)
    df = df[['userId', 'movieId',  'rating']]
    df = df[~df['movieId'].isin(less_voted)]
    df = less_active_voters_filter(df)
    return df


def rating_matrix(rating_df):  
    rating_matrix = rating_df.pivot_table(index='movieId',  columns='userId', values='rating')
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
    less_voted = df[df['vote_count'] < config.m_config.vote_count_lower_bound]
    less_voted = less_voted['movieId']
    return less_voted.tolist()


def less_active_voters_filter(df: pd.DataFrame) -> list:
    
    user_groupby = pd.Series(Counter(df['userId']))
    freq_voters = user_groupby.loc[lambda x : x > 50]
    freq_voters = np.array(freq_voters.index)
    df = df[df['userId'].isin(freq_voters)]
    return df
# ------------------- HELPER FUNCTIONS ----------------------




if __name__ == "__main__":
    metadata_frame = metadata_df()
    clean_metadata_frame = clean_metadata_df(metadata_frame)
    clean_metadata_frame.to_csv("metadata.csv")
    
    ratings_df = rating_df()
    rating_mtx = rating_matrix(ratings_df)
    filled_mtx = filled_rating_matrix(rating_mtx)
    filled_mtx.to_csv("rating_matrix.csv")

    