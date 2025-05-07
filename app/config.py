import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()

@dataclass
class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:1234@localhost:5432/name_db")
    DEBUG: bool = os.getenv("DEBUG", "true").lower() == "true"

settings = Settings()