from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from database import get_db
from models import Project
from schemas import ProjectCreate, ProjectResponse
import os

router = APIRouter(prefix="/api/projects", tags=["Projects"])

ADMIN_SECRET = os.getenv("ADMIN_SECRET_KEY", "vimal2026")

INITIAL_PROJECTS = [
    {
        "title": "AI Agent Evaluation & Reliability Platform",
        "description": "Production-ready benchmarking platform to evaluate LLM agents on accuracy, latency, tool invocation fidelity, and hallucination drift. Features automated CI evaluation pipelines, Dockerized runtime, Redis cache, and asynchronous Celery workers.",
        "category": "ai",
        "tech_stack": "FastAPI, Docker, Celery, Redis, GitHub Actions CI",
        "github_url": "https://github.com/VimalN2005/AI-Agent-Evaluation-Reliability-Platform",
        "live_url": "https://vimalsahani.me",
        "image_url": ""
    },
    {
        "title": "socialFeed: High-Throughput Feed Engine",
        "description": "Distributed feed generation engine built with Django REST Framework and FastAPI. Engineered with hybrid fan-out on write/read, keyset cursor pagination for zero offset skips, Min-Heap ranking, Redis caching, and documented with 20 Architectural Decision Records (ADRs).",
        "category": "backend",
        "tech_stack": "Django REST, FastAPI, PostgreSQL, Redis, WebSockets",
        "github_url": "https://github.com/VimalN2005/socialFeed",
        "live_url": "https://vimalsahani.me",
        "image_url": ""
    },
    {
        "title": "DevPilot: RAG Codebase Intelligence",
        "description": "Production-grade developer intelligence platform for GitHub codebases. Integrates AST parsing, RAG-powered vector search across repositories, automated issue debugging, and contextual pull request reviews with LLMs.",
        "category": "ai",
        "tech_stack": "Python, RAG & Vector DB, LLM Orchestration, FastAPI",
        "github_url": "https://github.com/VimalN2005/DevPilot",
        "live_url": "https://vimalsahani.me",
        "image_url": ""
    },
    {
        "title": "FluxMesh: Distributed Job Orchestrator",
        "description": "Distributed task and job orchestration platform with intelligent scheduling, exponential backoff retries, multi-tier task priorities, worker node heartbeat coordination, and fault-tolerant state recovery.",
        "category": "backend",
        "tech_stack": "Python Asyncio, Distributed Queues, Worker Heartbeat, Redis",
        "github_url": "https://github.com/VimalN2005/FluxMesh",
        "live_url": "https://vimalsahani.me",
        "image_url": ""
    },
    {
        "title": "EdgeFlow: High-Performance API & Model Gateway",
        "description": "Low-latency API reverse-proxy gateway engineered for intelligent request routing, token bucket rate limiting, distributed caching, circuit breaker retries, and automated service & LLM model failover across backend nodes.",
        "category": "backend",
        "tech_stack": "FastAPI, Rate Limiting, Circuit Breakers, Redis Cache",
        "github_url": "https://github.com/VimalN2005/EdgeFlow",
        "live_url": "https://vimalsahani.me",
        "image_url": ""
    }
]

@router.get("", response_model=list[ProjectResponse])
def get_projects(category: str = None, db: Session = Depends(get_db)):
    projects = db.query(Project).all()
    
    # Auto-seed initial top projects if DB is empty
    if not projects:
        for p_data in INITIAL_PROJECTS:
            new_p = Project(**p_data)
            db.add(new_p)
        db.commit()
        projects = db.query(Project).all()

    if category and category != "all":
        projects = [p for p in projects if p.category == category]
    return projects

@router.post("", response_model=ProjectResponse)
def create_project(
    project_in: ProjectCreate,
    x_admin_key: str = Header(None),
    db: Session = Depends(get_db)
):
    if x_admin_key != ADMIN_SECRET:
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid Admin Secret Key")

    new_project = Project(**project_in.model_dump())
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project

@router.delete("/{project_id}")
def delete_project(
    project_id: int,
    x_admin_key: str = Header(None),
    db: Session = Depends(get_db)
):
    if x_admin_key != ADMIN_SECRET:
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid Admin Secret Key")

    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    db.delete(project)
    db.commit()
    return {"success": True, "message": f"Project {project_id} deleted"}
