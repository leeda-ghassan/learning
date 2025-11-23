from typing import Optional
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class AnalysisHistoryCreate(BaseModel):
    user_id: UUID
    input_text: str


class AnalysisHistory(BaseModel):
    id: UUID
    user_id: UUID
    input_text: str
    sentiment_label: str
    confidence_score: str
    created_at: datetime
    updated_at: datetime
    last_analysis_at: datetime


class ModelPerformanceCreate(BaseModel):
    model_version: str
    accuracy: str
    fl_score: int


class ModelPerformance(BaseModel):
    id: UUID
    model_version: str
    accuracy: str
    fl_score: int
    training_date: datetime
    is_active: datetime
    created_at: datetime
    updated_at: datetime


class UserRequest(BaseModel):
    username: str
    email: str
    password: str


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


class UserResponse(BaseModel):
    id: UUID
    username: str
    email: str
