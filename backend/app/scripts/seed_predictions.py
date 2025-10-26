import asyncio
from datetime import datetime
from app.db import get_collection

async def main():
    coll = get_collection("predictions")

    await coll.insert_many([
        {
            "ticker": "INFY.NS",
            "model_version": "lstm_v1",
            "prediction_date": "2025-10-27",
            "predicted_price": 1520.45,
            "predicted_trend": "Up",
            "confidence": 0.83,
            "features_snapshot": {"close_60": [1480, 1485, 1490], "sentiment_30": [0.2, 0.4, 0.6]},
            "created_at": datetime.utcnow()
        },
        {
            "ticker": "TCS.NS",
            "model_version": "lstm_v1",
            "prediction_date": "2025-10-27",
            "predicted_price": 3470.10,
            "predicted_trend": "Down",
            "confidence": 0.71,
            "features_snapshot": {"close_60": [3500, 3490, 3480], "sentiment_30": [0.3, 0.2, 0.1]},
            "created_at": datetime.utcnow()
        }
    ])
    print("✅ Sample predictions inserted.")

if __name__ == "__main__":
    asyncio.run(main())
