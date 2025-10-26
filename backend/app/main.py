# backend/app/main.py
from fastapi import FastAPI
from app.api.routes import router as api_router

app = FastAPI(title="MarketPulse AI")

app.include_router(api_router, prefix="/api")

@app.get("/")
def root():
    return {"status": "ok", "service": "MarketPulse AI"}
