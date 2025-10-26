# import asyncio
# from datetime import datetime
# from app.db import get_collection

# async def main():
#     coll = get_collection("tickers")
#     await coll.insert_many([
#         {"_id": "INFY.NS", "name": "Infosys Ltd", "exchange": "NSE", "sector": "IT", "market_cap": 1200000000000, "last_updated": datetime.utcnow()},
#         {"_id": "TCS.NS", "name": "Tata Consultancy Services", "exchange": "NSE", "sector": "IT", "market_cap": 1300000000000, "last_updated": datetime.utcnow()}
#     ])
#     print("✅ Sample tickers inserted.")

# asyncio.run(main())


import asyncio
from datetime import datetime
from app.db import get_collection

async def main():
    coll = get_collection("tickers")

    await coll.insert_many([
        {
            "_id": "INFY.NS",
            "name": "Infosys Ltd",
            "exchange": "NSE",
            "sector": "IT",
            "market_cap": 1200000000000,
            "last_updated": datetime.utcnow()
        },
        {
            "_id": "TCS.NS",
            "name": "Tata Consultancy Services",
            "exchange": "NSE",
            "sector": "IT",
            "market_cap": 1300000000000,
            "last_updated": datetime.utcnow()
        },
        {
            "_id": "RELIANCE.NS",
            "name": "Reliance Industries Ltd",
            "exchange": "NSE",
            "sector": "Energy",
            "market_cap": 1500000000000,
            "last_updated": datetime.utcnow()
        }
    ])
    print("✅ Sample tickers inserted.")

if __name__ == "__main__":
    asyncio.run(main())
