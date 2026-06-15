import os
from dotenv import load_dotenv


load_dotenv()


class Settings:
    PROJECT_NAME = "car price api"
    API_KEY = os.getenv("API_KEY", "DEMO-KEY")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "secret")
    JWT_ALGORITHM = "HS256"
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
    MODEL_PATH = "app/models/model.pkl"


setting = Settings()
