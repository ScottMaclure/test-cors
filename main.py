from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from datetime import datetime


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/api/v1/renewToken")
async def renew_token():
    return {
        "TODO": "Return new token",
        "timestamp": f"{datetime.now()}"
    }
