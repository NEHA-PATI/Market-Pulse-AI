# from fastapi import APIRouter, HTTPException
# from typing import List
# from app.db import database
# from app.models.ticker import Ticker
# from app.models.news_cache import NewsCache 

# router = APIRouter()

# # --- TICKER ROUTES ---

# @router.post("/ticker", response_model=dict)
# async def add_ticker(ticker: Ticker):
#     """Adds a new ticker, using the ticker symbol as the MongoDB _id."""
#     collection = database.get_collection("tickers")
    
#     # CRITICAL FIX: Query MongoDB using "_id" key
#     existing = await collection.find_one({"_id": ticker.id}) 
#     if existing:
#         raise HTTPException(status_code=400, detail="Ticker already exists")
    
#     # CRITICAL FIX: Use .model_dump(by_alias=True) to save Python 'id' as MongoDB '_id'
#     await collection.insert_one(ticker.model_dump(by_alias=True))
#     return {"message": "Ticker added successfully"}

# @router.get("/ticker/{ticker_id}", response_model=Ticker)
# async def get_ticker(ticker_id: str):
#     """Retrieves a single ticker by its ID."""
#     collection = database.get_collection("tickers")
#     # CRITICAL FIX: Query MongoDB using "_id" key
#     ticker_data = await collection.find_one({"_id": ticker_id})
    
#     if not ticker_data:
#         raise HTTPException(status_code=404, detail="Ticker not found")
    
#     # Return the Pydantic model (which maps MongoDB's "_id" back to Python's "id")
#     return Ticker(**ticker_data).model_dump(by_alias=True)

# # --- NEWS CACHE ROUTES ---

# @router.post("/news", response_model=dict)
# async def add_news_item(news_item: NewsCache):
#     """Adds a new news item to the 'news' collection."""
#     collection = database.get_collection("news")
    
#     # news items use a generated ObjectId, so we just insert the model dump.
#     await collection.insert_one(news_item.model_dump(by_alias=True))
    
#     return {"message": "News item added successfully", "ticker": news_item.ticker}

# @router.get("/news/{ticker_id}", response_model=List[NewsCache])
# async def get_news_by_ticker(ticker_id: str):
#     """Retrieves all news items for a specific ticker."""
#     collection = database.get_collection("news")
    
#     # Query for all documents where the 'ticker' field matches the provided ticker_id
#     news_cursor = collection.find({"ticker": ticker_id})
#     news_list = await news_cursor.to_list(length=100) 
    
#     if not news_list:
#         return []
    
#     # Convert MongoDB dicts to Pydantic models and export them
#     return [NewsCache(**item).model_dump(by_alias=True) for item in news_list]

from fastapi import APIRouter, HTTPException
from app.db import database
from app.models.ticker import Ticker
from app.models.news_cache import NewsCache
from app.models.prediction import Prediction
from app.models.leaderboard import Leaderboard

router = APIRouter()

# -----------------------
# 1️⃣ Tickers
# -----------------------
@router.post("/ticker")
async def add_ticker(ticker: Ticker):
    collection = database.get_collection("tickers")
    existing = await collection.find_one({"_id": ticker._id})
    if existing:
        raise HTTPException(status_code=400, detail="Ticker already exists")
    await collection.insert_one(ticker.dict())
    return {"message": "Ticker added successfully"}

@router.get("/ticker/{ticker_id}")
async def get_ticker(ticker_id: str):
    collection = database.get_collection("tickers")
    ticker = await collection.find_one({"_id": ticker_id})
    if not ticker:
        raise HTTPException(status_code=404, detail="Ticker not found")
    return ticker


# -----------------------
# 2️⃣ News Cache
# -----------------------
@router.post("/news")
async def add_news(news: NewsCache):
    collection = database.get_collection("news_cache")
    await collection.insert_one(news.dict())
    return {"message": "News inserted successfully"}

@router.get("/news/{ticker}")
async def get_news(ticker: str):
    collection = database.get_collection("news_cache")
    cursor = collection.find({"ticker": ticker}).sort("published_at", -1)
    results = await cursor.to_list(length=20)
    return results


# -----------------------
# 3️⃣ Predictions
# -----------------------
@router.post("/predict")
async def add_prediction(prediction: Prediction):
    collection = database.get_collection("predictions")
    await collection.insert_one(prediction.dict())
    return {"message": "Prediction stored successfully"}

@router.get("/predict/{ticker}")
async def get_predictions(ticker: str):
    collection = database.get_collection("predictions")
    cursor = collection.find({"ticker": ticker}).sort("created_at", -1)
    results = await cursor.to_list(length=10)
    return results


# -----------------------
# 4️⃣ Leaderboard
# -----------------------
@router.post("/leaderboard")
async def add_leaderboard(board: Leaderboard):
    collection = database.get_collection("leaderboards")
    await collection.insert_one(board.dict())
    return {"message": "Leaderboard added"}

@router.get("/leaderboard/{date}")
async def get_leaderboard(date: str):
    collection = database.get_collection("leaderboards")
    data = await collection.find_one({"_id": date})
    if not data:
        raise HTTPException(status_code=404, detail="Leaderboard not found")
    return data
