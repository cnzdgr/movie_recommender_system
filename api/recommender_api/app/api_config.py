'''
Generaic API config file
'''

import logging
from typing import List
from pydantic import AnyHttpUrl, BaseModel

class LoggingSettings(BaseModel):
    LOGGING_LEVEL: int = logging.INFO
    

class Settings(BaseModel):
    API_V1_STR: str = "/api/v1"

    logging: LoggingSettings = LoggingSettings()

    # During local development
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost:3000",  # type: ignore
        "http://localhost:8000",  # type: ignore
        "https://localhost:3000",  # type: ignore
        "https://localhost:8000",  # type: ignore
    ]

    PROJECT_NAME: str = "Movie Recommender API"

    class Config:
        case_sensitive = True
        

settings = Settings()

