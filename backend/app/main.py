from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="MarketPulseAI Backend")

app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"message": "MarketPulseAI API is running 🚀"}
