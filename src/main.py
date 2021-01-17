from functools import lru_cache
from fastapi import Depends, FastAPI
from .config import Settings

app = FastAPI()


@lru_cache()
def get_settings():
    return Settings()


@app.get("/")
async def info(settings: Settings = Depends(get_settings)):
    return {
        "app_name": settings.app_name,
        "password": settings.password
    }
