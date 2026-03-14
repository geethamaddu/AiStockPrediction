from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    google_api_key: str = os.getenv("GOOGLE_API_KEY", "")
    default_model: str = os.getenv("DEFAULT_MODEL", "gemini-2.0-flash")
    app_host: str = os.getenv("APP_HOST", "0.0.0.0")
    app_port: int = int(os.getenv("APP_PORT", "8000"))
    polygon_api_key: str = os.getenv("POLYGON_API_KEY", "")
    newsapi_key: str = os.getenv("NEWSAPI_KEY", "")
    fred_api_key: str = os.getenv("FRED_API_KEY", "")


settings = Settings()