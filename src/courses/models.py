from uuid import UUID
from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

class CourseCreate(BaseModel):
    title: str
    description: str
    instructor: str
    duration: int
    level: str
    time_interval: str
    skill_requirements: str

class CourseUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    instructor: Optional[str] = None
    duration: Optional[int]
    level: Optional[str] = None
    time_interval: Optional[str] = None
    skill_requirements: Optional[str] = None
    

class CourseResponse(BaseModel):
    id: UUID
    title: str
    description: str
    instructor: str
    duration: int
    level: str
    time_interval: str
    skill_requirements: str
    last_login_at: datetime

class CourseList(BaseModel):
    items: List[CourseResponse]
    total: int