from uuid import UUID
from datetime import datetime
from pydantic import BaseModel

class SkillCreate(BaseModel):
    name: str
    description: str

class SkillResponse(BaseModel):
    id: UUID
    name: str
    description: str