from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from database import engine, get_db
from src.user.model import Base
from src.user import api as user_api
from src.entry import api as entry_api
from src.competition import api as competion_api
from env_loader import env

# app = FastAPI()

app = FastAPI(debug=env("DEBUG", "false").lower() == "true")

Base.metadata.create_all(engine)

app.include_router(user_api.Router)
app.include_router(entry_api.Router)
app.include_router(competion_api.Router)



@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}


