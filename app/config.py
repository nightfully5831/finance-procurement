import os
from pathlib import Path
from pydantic_settings import BaseSettings  # ✅ Correct import
from dotenv import load_dotenv
from datetime import timedelta

# Load environment variables
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

    # Allowed Hosts (CORS)
    ALLOWED_HOSTS: list = [
        "localhost",
        "localhost:8000",
        "127.0.0.1",
        "16.171.11.180",
        "asseter.onrender.com",
        "asserter.vercel.app",
        "procure-bridge.vercel.app"
    ]
    
    CORS_ORIGINS: list = [
        "http://127.0.0.1",
        "http://localhost",
        "16.171.11.180",
        "http://localhost:3000",
        "http://localhost:8080",
        "http://localhost:5000",
        "https://procure-bridge.vercel.app",
        "https://asseter.onrender.com",
        "https://asserter.vercel.app",
    ]
    
    # Database Configuration (PostgreSQL)
    DATABASE_URL: str = f"postgres://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

    # JWT Authentication
    ACCESS_TOKEN_LIFETIME: timedelta = timedelta(days=1)
    REFRESH_TOKEN_LIFETIME: timedelta = timedelta(days=7)
    JWT_ALGORITHM: str = "HS256"

    # Email Configuration
    EMAIL_HOST: str = os.getenv("EMAIL_HOST", "smtp.gmail.com")
    EMAIL_PORT: int = int(os.getenv("EMAIL_PORT") or "587")
    EMAIL_USE_SSL: bool = os.getenv("EMAIL_USE_SSL", "False").lower() == "true"
    EMAIL_HOST_USER: str = os.getenv("EMAIL_HOST_USER", "")
    EMAIL_HOST_PASSWORD: str = os.getenv("EMAIL_HOST_PASSWORD", "")
    DEFAULT_FROM_EMAIL: str = os.getenv("DEFAULT_FROM_EMAIL", "")

    # Site Configuration
    DOMAIN: str = "asserter.vercel.app"
    SITE_NAME: str = "Asseter"
    SITE_ID: int = 1

# ✅ Initialize settings instance
settings = Settings()

TORTOISE_ORM = {
    "connections": {
        "default": "postgresql://nft_ori1_user:Gqv43oNIiA81uCAxaqj9b0F56jJJSA6I@dpg-cv46vbd2ng1s73degku0-a.oregon-postgres.render.com/nft_ori1"
    },
    "apps": {
        "models": {
            "models": ["app.models.assets", "app.models.company", "app.models.depreciation", "app.models.user", "aerich.models"],
            "default_connection": "default",
        }
    }
}

