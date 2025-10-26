# backend/app/api/routes.py
from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/predict/{ticker}")
async def predict_ticker(ticker: str):
    # call your pipeline: fetch price, news, sentiment, run model
    return JSONResponse({"ticker": ticker, "prediction": "up", "confidence": 0.72})

@router.get("/stock/{ticker}")
async def stock_details(ticker: str):
    return {"ticker": ticker, "prices": []}
