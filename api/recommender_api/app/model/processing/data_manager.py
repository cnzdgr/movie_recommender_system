import os
import sys
import joblib
import pandas as pd
from typing import List
from pathlib import Path
from sklearn.pipeline import Pipeline

# Adding the ROOT path 
d = os.getcwd()
par_3 = os.path.dirname(os.path.dirname(os.path.dirname(d)))
sys.path.append(par_3)

from app.model.model_config import DATASET_DIR, DATAFRAME_DIR, TRAINED_MODEL_DIR, config


def load_dataset(*, file_name: str) -> pd.DataFrame:
    '''Load the dataset as raw, without any cleaning'''
    df = pd.read_csv(Path(f"{DATASET_DIR}/{file_name}"))    
    return df


def save_model(*, model_to_keep: Pipeline, model_type: str) -> None:
    '''
    Saves the model (output of the pipeline) and removes previous models
    By this way, we will be sure there is only 1 model 
    '''   
    save_file_root = f"{config.a_config.save_file_model}{config.a_config.version}"
    save_file_name = save_file_root+f"_{model_type}.pkl"
    save_path = TRAINED_MODEL_DIR / save_file_name

    remove_old_model(files_to_keep=[save_file_root+"_knn.pkl", save_file_root+"_sentence_transformer.pkl"])
    
    joblib.dump(model_to_keep, save_path)
    

def load_model(*, file_name: str) -> Pipeline:
    '''Load a trained model'''

    file_path = TRAINED_MODEL_DIR / file_name
    return joblib.load(filename=file_path)


def save_dataframe(*, df, df_name:str) -> None:
    save_path = DATAFRAME_DIR / df_name
    df.to_csv(save_path)

    
def load_dataframe(*, df_name:str) -> pd.DataFrame():
    file_path = DATAFRAME_DIR / df_name
    df = pd.read_csv(file_path)
    
    return df


def remove_old_model(*, files_to_keep: List[str]) -> None:
    '''
    To remove old model/s (output of the training pipeline).
    To be sure there is one-to-one mapping between package version
    and model version to be used in other parts
    '''
    
    for model_file in TRAINED_MODEL_DIR.iterdir():
        if model_file.name not in files_to_keep:
            model_file.unlink()
