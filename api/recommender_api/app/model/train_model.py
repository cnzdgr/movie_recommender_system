'''
Calling the functions to create required dataframes
And training required models and saving .pkl files
'''
import os
import sys
import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Adding the ROOT path 
d = os.getcwd()
par_2 = os.path.dirname(os.path.dirname(d))
sys.path.append(par_2)

from app.model.model_config import config
from app.model.processing.data_manager import load_dataframe, save_model
from app.model.processing.dataframe_creator import create_all_dataframes


def run_training() -> None:
    
    # Run the below line if dataframes are not already created
    #create_all_dataframes()
    rating_matrix = load_dataframe(df_name='rating_matrix_id.csv')
    rating_matrix = rating_matrix.iloc[: , 1:]
    
    
    knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=2)
    knn.fit(rating_matrix)

    save_model(model_to_keep=knn, model_type='knn')

if __name__ == "__main__":
    run_training()