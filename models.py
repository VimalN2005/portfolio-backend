from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    category = Column(String(50), default="backend")  # backend, ai, systems
    tech_stack = Column(String(255), default="")      # comma-separated e.g. "FastAPI, Docker, Redis"
    github_url = Column(String(500), default="")
    live_url = Column(String(500), default="")
    image_url = Column(String(500), default="")
    created_at = Column(DateTime, default=datetime.utcnow)

class UploadedMedia(Base):
    __tablename__ = "uploaded_media"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    file_url = Column(String(500), nullable=False)
    content_type = Column(String(100), default="image/png")
    uploaded_at = Column(DateTime, default=datetime.utcnow)

class ContactMessage(Base):
    __tablename__ = "contact_messages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    email = Column(String(255), nullable=False)
    subject = Column(String(255), default="Portfolio Inquiry")
    message = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
