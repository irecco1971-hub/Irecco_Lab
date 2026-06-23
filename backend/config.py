# Application-wide configuration loaded from environment variables.

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql://postgres:postgres@localhost:5432/irecco_lab"
    secret_key: str = "change-me"
    debug: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
