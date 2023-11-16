

import os
import sys
import numpy as np
import pandas as pd
from collections import Counter
from ast import literal_eval
from sklearn.neighbors import NearestNeighbors


# Adding the ROOT path 
d = os.getcwd()
par_3 = os.path.dirname(os.path.dirname(os.path.dirname(d)))
sys.path.append(par_3)

from app.model.model_config import config
from app.model.processing.data_manager import load_dataset
from app.model.processing.data_manager import save_model
from app.model.processing.dataframe_creator import filled_rating_matrix


def run_training() -> None:
    
    rating_matrix_filled = filled_rating_matrix()
    
    knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=2)
    knn.fit(rating_matrix_filled)


    save_model(model_to_keep=knn)


if __name__ == "__main__":
    run_training()