import asyncio
from datetime import datetime
from app.db import get_collection

async def main():
    coll = get_collection("leaderboards")

    await coll.insert_one({
        "_id": "2025-10-25",
        "items": [
            {"ticker": "INFY.NS", "predicted_trend": "Up", "confidence": 0.92},
            {"ticker": "TCS.NS", "predicted_trend": "Down", "confidence": 0.81},
            {"ticker": "RELIANCE.NS", "predicted_trend": "Up", "confidence": 0.88}
        ],
        "created_at": datetime.utcnow()
    })
    print("✅ Sample leaderboard inserted.")

if __name__ == "__main__":
    asyncio.run(main())
