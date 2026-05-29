import os
from typing import List
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Crop Disease Detection API"
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"

    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
    ]

    MAX_UPLOAD_SIZE_MB: int = 10
    ALLOWED_CONTENT_TYPES: List[str] = [
        "image/jpeg",
        "image/png",
        "image/webp",
        "image/jpg",
    ]

    class Config:
        env_file = ".env"
        case_sensitive = True

    def __init__(self, **data):
        super().__init__(**data)
        # Allow adding production CORS origins via environment variable
        cors_origins_env = os.getenv("CORS_ORIGINS", "")
        if cors_origins_env:
            origins = cors_origins_env.split(",")
            self.ALLOWED_ORIGINS.extend([origin.strip() for origin in origins])


settings = Settings()
