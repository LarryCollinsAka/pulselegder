import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    CIRCLE_API_KEY: str = os.getenv("CIRCLE_API_KEY", "")
    CIRCLE_ENTITY_SECRET: str = os.getenv("CIRCLE_ENTITY_SECRET", "")
    CIRCLE_WALLET_ID: str = os.getenv("CIRCLE_WALLET_ID", "")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
