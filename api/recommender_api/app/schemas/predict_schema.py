'''
Schema for the API request and response
'''

from typing import List, Optional
from pydantic import BaseModel


class PredictionResults(BaseModel):
    predictions: Optional[List[tuple]]
    version: str


class MovieInputSchema(BaseModel):
    Movie: Optional[str]


class MovieDataInput(BaseModel):
    inputs: List[MovieInputSchema]

    class Config:
        json_schema_extra = {
            "example": {
                "inputs": [
                    {
                        "Movie": "Batman Begins",
                    }
                ]
            }
        }
