'''
Uses the saved model and makes prediction
'''
import sys
import os 
import typing as t
import pandas as pd
from pathlib import Path

d = os.getcwd()
par = os.path.dirname(d)
par_par = os.path.dirname(par)
sys.path.append(par_par)
    
from app.model.model_config import config
from app.model.processing.data_manager import load_model

save_file_model = f"{config.a_config.save_file_model}{config.a_config.version}.pkl"
prediction_model = load_model(file_name=save_file_model)


def make_prediction(*,input_movie: str]) -> list[list]:
    """Make a prediction using a saved model pipeline."""
    dist, idx = prediction_model(input_movie)
    
    validated_data, errors = validate_inputs(input_data=data)
    results = {"predictions": None, "version": config.a_config.version, "errors": errors}

    if not errors:
        predictions = _titanic_pipe.predict(
            X=validated_data[config.m_config.features]
        )
        results = {
            "predictions": predictions,
            "version": config.a_config.version,
            "errors": errors,
        }
        
    return results

'''
# Use if you need to check the function make_prediction
from processing.data_manager import load_dataset
data = load_dataset(file_name=config.a_config.test_data_file)
new_preds = make_prediction(input_data=data)
result = pd.DataFrame(new_preds['predictions'], columns=["Survived"])
result.to_csv('result.csv', index=False)
'''