from datetime import datetime, timedelta

import jwt

from env_loader import env

SECRET_KEY = env("SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY must be set in the environment or .env file")

ALGORITHM = "HS256"
ACCESS_TOKEN = 60
REFRESH_TOKEN = 120


def create_access_token(data: dict):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.now() + timedelta(minutes=ACCESS_TOKEN)})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def create_refresh_token(data: dict):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.now() + timedelta(minutes=REFRESH_TOKEN)})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
