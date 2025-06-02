from pydantic_settings import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    database_url: str = "sqlite:///./app.db"  # Default fallback
    secret_key: str = "your-secret-key-here"
    debug: bool = False
    allowed_origins: List[str] = ["http://localhost:3000"]
    port: int = int(os.getenv("PORT", 8000))

    class Config:
        env_file = ".env"


settings = Settings()
