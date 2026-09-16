from fastapi import FastAPI
from app.config import api_key

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Expense Tracker API is running"}


@app.get("/secret-status")
def secret_status():
    return {"api_key_loaded": bool(api_key)}
