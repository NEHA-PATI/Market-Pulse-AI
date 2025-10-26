# backend/app/db.py
from motor.motor_asyncio import AsyncIOMotorClient
from urllib.parse import quote_plus
import os
from dotenv import load_dotenv

load_dotenv()  # loads backend/.env

MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DB = os.getenv("MONGODB_DB", "marketpulse")

# optional: if your password has special chars, ensure it's URL-encoded
# client = AsyncIOMotorClient(MONGODB_URI)  # simple use

client = AsyncIOMotorClient(MONGODB_URI, serverSelectionTimeoutMS=5000)
database = client[MONGODB_DB]

# Helper to get collection
def get_collection(name: str):
    return database[name]
