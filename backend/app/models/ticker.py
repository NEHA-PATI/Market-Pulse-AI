# from pydantic import BaseModel
# from typing import Optional
# from datetime import datetime

# class Ticker(BaseModel):
#     id: str
#     name: str
#     exchange: Optional[str]
#     sector: Optional[str]
#     market_cap: Optional[float]
#     last_updated: Optional[datetime]

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Ticker(BaseModel):
    # CRITICAL: Maps Python 'id' to MongoDB '_id'.
    id: str = Field(alias="_id", description="The stock ticker symbol (e.g., INFY.NS).")
    name: str
    exchange: Optional[str]
    sector: Optional[str]
    market_cap: Optional[float]
    last_updated: Optional[datetime]
    
    # Configuration for Pydantic V2 to handle aliasing on input and output.
    model_config = {
        # This tells Pydantic to accept the field name 'id' OR the alias '_id' on input (422 fix).
        "populate_by_name": True,
        # This allows the model to be exported using the alias '_id' (500 fix).
        "by_alias": True, 
        "json_schema_extra": {
            "example": {
                "_id": "INFY.NS",
                "name": "Infosys Ltd",
                "exchange": "NSE",
                "sector": "IT",
                "market_cap": 1200000000000,
                "last_updated": "2025-10-26T12:00:00Z"
            }
        }
    }