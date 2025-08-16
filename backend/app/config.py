# app/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    redis_url: str
    regrid_api_key: str
    google_api_key: str
    clickup_api_key: str
    secret_key: str
    access_token_expire_minutes: int
    jwt_algorithm: str

    class Config:
        env_file = ".env"


def get_settings():
    return Settings()
