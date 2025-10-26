from pydantic import BaseModel
from typing import List
from datetime import datetime

class LeaderboardItem(BaseModel):
    ticker: str
    predicted_trend: str
    confidence: float

class Leaderboard(BaseModel):
    id: str   # snapshot date
    items: List[LeaderboardItem]
    created_at: datetime
