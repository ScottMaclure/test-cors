from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# https://fastapi.tiangolo.com/tutorial/cors/
allowed_origins = [
    'http://foo.local:8000',
    'http://bar.local:8000',
]

app.add_middleware(CORSMiddleware,
    allow_origins=allowed_origins,
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=10  # caching
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/api/v1/renewToken")
async def renew_token():
    return {
        "TODO": "Return new token",
        "timestamp": f"{datetime.now()}"
    }
