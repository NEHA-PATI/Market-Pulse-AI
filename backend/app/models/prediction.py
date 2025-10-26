from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime

class Prediction(BaseModel):
    ticker: str
    model_version: str
    prediction_date: str
    predicted_price: float
    predicted_trend: str
    confidence: float
    features_snapshot: Optional[Dict]
    created_at: Optional[datetime] = datetime.utcnow()
