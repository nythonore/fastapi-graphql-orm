from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_DEBUG: bool = True

    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"
    DB_DATABASE: str = "db"
    DB_USERNAME: str = "postgres"
    DB_PASSWORD: str = "password"

    class Config:
        env_file = ".env"


@lru_cache()
def load_settings():
    return Settings()


settings = load_settings()
