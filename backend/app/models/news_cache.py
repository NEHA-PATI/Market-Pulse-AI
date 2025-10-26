# from pydantic import BaseModel
# from typing import Optional, Dict
# from datetime import datetime

# class NewsCache(BaseModel):
#     ticker: str
#     source: Optional[str]
#     title: str
#     summary: Optional[str]
#     url: Optional[str]
#     published_at: datetime
#     fetched_at: datetime
#     sentiment: Optional[float]
#     raw_sentiment_output: Optional[Dict]


from pydantic import BaseModel, Field
from typing import Optional, Dict
from datetime import datetime

class NewsCache(BaseModel):
    # MongoDB will auto-generate this ObjectId on insertion.
    id: Optional[str] = Field(alias="_id", default=None, description="MongoDB document ID (auto-generated).")
    ticker: str
    source: Optional[str]
    title: str
    summary: Optional[str]
    url: Optional[str]
    published_at: datetime
    fetched_at: datetime
    sentiment: Optional[float]
    raw_sentiment_output: Optional[Dict]
    
    # Configuration for Pydantic V2 to handle aliasing
    model_config = {
        "populate_by_name": True,
        "by_alias": True,
        "json_schema_extra": {
            "example": {
                "ticker": "INFY.NS",
                "source": "MoneyControl",
                "title": "Infosys shares jump 3% after Q3 results",
                "published_at": "2024-01-12T09:00:00Z",
                "fetched_at": "2024-01-12T10:00:00Z",
                "sentiment": 0.85,
            }
        }
    }