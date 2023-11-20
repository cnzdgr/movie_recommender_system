'''
Uses the saved model and makes prediction
'''
import sys
import os 
import pandas as pd

d = os.getcwd()
par = os.path.dirname(d)
par_par = os.path.dirname(par)
sys.path.append(par_par)
    
from app.model.model_config import config
from app.model.processing.data_manager import load_model, load_dataframe

save_file_knn = f"{config.a_config.save_file_model}{config.a_config.version}_knn.pkl"
prediction_model = load_model(file_name=save_file_knn)


def make_prediction(*,input_movie: str) -> dict:
    """Make a prediction using a saved model pipeline."""
    rating_matrix = load_dataframe(df_name='rating_matrix_id.csv')
    name_mapper = load_dataframe(df_name='movie_map.csv')
    movieId = name_mapper.loc[name_mapper['original_title'] == input_movie]['movieId'].values[0]
    rec_list = []
    movie_ratings = rating_matrix.loc[rating_matrix['movieId']==movieId].values.reshape(1,-1)[0][1:].reshape(1,-1)
    
    dist, idx = prediction_model.kneighbors(movie_ratings,n_neighbors=20)
    for i in range(0, len(dist.flatten())):
        movie_idx = rating_matrix.iloc[idx.flatten()[i]]['movieId']
        movie_name = name_mapper.loc[name_mapper['movieId'] == movie_idx]['original_title'].values[0]
        movie_dist = dist.flatten()[i]
        rec_list.append((movie_name, movie_dist))

    results = {
        "predictions": rec_list,
        "version": config.a_config.version,
        }
    return results

# Use if you need to check the function make_prediction
new_preds = make_prediction(input_movie='Ace Ventura: When Nature Calls')
result = pd.DataFrame(new_preds)
result.to_csv('result.csv', index=False)
