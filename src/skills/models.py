from uuid import UUID
from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List

class SkillCreate(BaseModel):
    name: str
    description: str

class SkillUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class SkillResponse(BaseModel):
    id: UUID
    name: str
    description: str
    created_at: datetime
    updated_at: datetime

class SkillList(BaseModel):
    items: List[SkillResponse]
    total: int