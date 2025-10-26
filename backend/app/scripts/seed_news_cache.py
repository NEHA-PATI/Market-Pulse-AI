# import asyncio
# from datetime import datetime
# from app.db import get_collection

# async def main():
#     coll = get_collection("news")

#     current_time = datetime.utcnow()

#     # News items do not define _id; MongoDB generates a unique ObjectId for each.
#     await coll.insert_many([
#         {
#             "ticker": "INFY.NS",
#             "source": "Economic Times",
#             "title": "Infosys shares jump 3% after announcing new cloud partnership",
#             "summary": "The company has entered a multi-year deal with a leading European retailer, boosting market confidence.",
#             "url": "https://example.com/infosys-cloud-deal",
#             "published_at": datetime(2025, 10, 25, 10, 0, 0),
#             "fetched_at": current_time,
#             "sentiment": 0.92,
#             "raw_sentiment_output": {"model": "v1.0", "score": "positive"}
#         },
#         {
#             "ticker": "TCS.NS",
#             "source": "Bloomberg",
#             "title": "TCS reports steady growth amid tech spending slowdown",
#             "summary": "Management commentary was cautiously optimistic, signaling strong order book conversion.",
#             "url": "https://example.com/tcs-q3-results",
#             "published_at": datetime(2025, 10, 24, 15, 30, 0),
#             "fetched_at": current_time,
#             "sentiment": 0.65,
#             "raw_sentiment_output": {"model": "v1.0", "score": "neutral-positive"}
#         },
#     ])
#     print("✅ Sample news items inserted into 'news' collection.")

# if __name__ == "__main__":
#     # Ensure this script is run as a module from the backend root directory:
#     # python -m app.scripts.seed_news_cache
#     asyncio.run(main())


import asyncio
from datetime import datetime
from app.db import get_collection

async def main():
    coll = get_collection("news_cache")
    current_time = datetime.utcnow()

    await coll.insert_many([
        {
            "ticker": "INFY.NS",
            "source": "Economic Times",
            "title": "Infosys shares jump 3% after announcing new cloud partnership",
            "summary": "Infosys signed a multi-year deal with a leading European retailer.",
            "url": "https://example.com/infosys-news",
            "published_at": datetime(2025, 10, 25, 10, 0),
            "fetched_at": current_time,
            "sentiment": 0.92,
            "raw_sentiment_output": {"model": "bert_sent_v1", "score": "positive"}
        },
        {
            "ticker": "TCS.NS",
            "source": "Bloomberg",
            "title": "TCS reports steady growth amid tech slowdown",
            "summary": "TCS remained resilient despite macroeconomic headwinds.",
            "url": "https://example.com/tcs-news",
            "published_at": datetime(2025, 10, 24, 15, 30),
            "fetched_at": current_time,
            "sentiment": 0.65,
            "raw_sentiment_output": {"model": "bert_sent_v1", "score": "neutral"}
        }
    ])
    print("✅ Sample news_cache entries inserted.")

if __name__ == "__main__":
    asyncio.run(main())
