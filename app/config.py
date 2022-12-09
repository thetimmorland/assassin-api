from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    pghost: str | None
    pgport: int | None
    pguser: str | None
    pgpassword: str | None
    pgdatabase: str


@lru_cache()
def get_settings() -> Settings:
    return Settings()
