from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

class ProjectCreate(BaseModel):
    title: str
    description: str
    category: str = "backend"
    tech_stack: str = ""
    github_url: Optional[str] = ""
    live_url: Optional[str] = ""
    image_url: Optional[str] = ""

class ProjectResponse(ProjectCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class ContactCreate(BaseModel):
    name: str
    email: str
    subject: Optional[str] = "Portfolio Contact"
    message: str

class ContactResponse(ContactCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class AIChatRequest(BaseModel):
    question: str

class AIChatResponse(BaseModel):
    answer: str
    matched_skills: list[str] = []
    sources: list[str] = []
