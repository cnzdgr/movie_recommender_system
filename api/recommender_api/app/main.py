import os
import sys
from typing import Any

# Adding the main folder to sys.path
d = os.getcwd()
sys.path.append(os.path.dirname(d))

from loguru import logger
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi import APIRouter, FastAPI, Request
from app.api import api_router
from app.api_config import settings



root_router = APIRouter()

app = FastAPI(
    title="/api/movie_recommender_api")

@root_router.get("/")
def index(request: Request) -> Any:
    '''Default HTML response for the main page, directing to docs'''
    body = (
        "<html>"
        "<body style='padding: 10px;'>"
        "<h1>Welcome to the Movie Recommender API</h1>"
        "<div>"
        "Check the docs: <a href='/docs'>here</a>"
        "</div>"
        "</body>"
        "</html>"
    )
    
    return HTMLResponse(content=body)


app.include_router(api_router)
app.include_router(root_router)

origins = ["*"]

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


if __name__ == "__main__":
    import uvicorn
    logger.warning("Running in development mode.")

    uvicorn.run(app, host="localhost", port=8001, log_level="debug")