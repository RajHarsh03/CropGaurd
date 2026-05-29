from typing import List, Optional
from pydantic import BaseModel


class Top5Prediction(BaseModel):
    class_name: str
    confidence: float
    confidence_pct: float


class PredictionResponse(BaseModel):
    success: bool
    class_name: str
    display_name: str
    plant: str
    disease: str
    confidence: float
    confidence_pct: float
    description: str
    symptoms: List[str]
    causes: str
    remedies: List[str]
    prevention: List[str]
    severity: str
    top5_predictions: List[Top5Prediction]
    filename: Optional[str] = None


class HealthResponse(BaseModel):
    status: str
    model_loaded: bool
    message: str
