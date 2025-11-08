from pydantic_settings import BaseSettings
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    # App
    APP_NAME: str = "Pinterest Growth Platform"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # Database
    DATABASE_URL: str
    REDIS_URL: str

    # Supabase
    SUPABASE_URL: str = ""
    SUPABASE_ANON_KEY: str = ""

    # API Keys
    OPENAI_API_KEY: str
    ANTHROPIC_API_KEY: str = ""

    # Pinterest API
    PINTEREST_APP_ID: str
    PINTEREST_APP_SECRET: str = ""
    PINTEREST_CLIENT_ID: str = ""
    PINTEREST_ACCESS_TOKEN: str = ""
    PINTEREST_REDIRECT_URI: str = ""

    # Image Generation
    FAL_API_KEY: str = ""
    STABILITY_API_KEY: str = ""
    REPLICATE_API_TOKEN: str = ""

    # Cloud Storage
    AWS_ACCESS_KEY_ID: str = ""
    AWS_SECRET_ACCESS_KEY: str = ""
    AWS_S3_BUCKET: str = ""
    AWS_REGION: str = "us-east-1"

    CLOUDINARY_CLOUD_NAME: str = ""
    CLOUDINARY_API_KEY: str = ""
    CLOUDINARY_API_SECRET: str = ""

    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # CORS
    ALLOWED_ORIGINS: str = "http://localhost:3000,http://localhost:3001"

    # Celery
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str

    @property
    def cors_origins(self) -> List[str]:
        return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(",")]

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
