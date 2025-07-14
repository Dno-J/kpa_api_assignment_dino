from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Settings:
    """
    Configuration class to access environment variables.
    """
    DATABASE_URL: str = os.getenv("DATABASE_URL")

# Create a single instance of Settings to use across the app
settings = Settings()
