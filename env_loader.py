import os
from pathlib import Path
from dotenv import load_dotenv

# Get project root directory
BASE_DIR = Path(__file__).resolve().parent

# Load .env file
load_dotenv(BASE_DIR / ".env")


def env(key, default=None):
    return os.getenv(key, default)
