from dotenv import load_dotenv
from app.config import settings
DATABASE_URL = settings.DATABASE_URL

# Load environment variables from .env file
load_dotenv()

class Settings:
    """
    Configuration class to access environment variables.
    """
    DATABASE_URL = settings.DATABASE_URL

# Create a single instance of Settings to use across the app
settings = Settings()
