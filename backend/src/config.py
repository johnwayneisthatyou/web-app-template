from pydantic_settings import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    database_url: str = "sqlite:///./app.db"
    secret_key: str = "your-secret-key-here"
    debug: bool = False
    allowed_origins: str = "http://localhost:3000"  # Change to string
    port: int = int(os.getenv("PORT", 8000))

    class Config:
        env_file = ".env"

    @property
    def allowed_origins_list(self) -> List[str]:
        """Convert comma-separated string to list"""
        return [origin.strip() for origin in self.allowed_origins.split(",")]


settings = Settings()
