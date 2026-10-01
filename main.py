import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from database import engine, Base
from routers import projects, upload, contact, ai_copilot

# Initialize database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Vimal Sahani - Portfolio API",
    description="High-performance backend API for Vimal Sahani's developer portfolio. Provides media uploads, dynamic projects, recruiter inquiries, and AI assistant.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS configuration - Allows requests from GitHub Pages and Custom Domain
ALLOWED_ORIGINS = [
    "https://vimalsahani.me",
    "http://vimalsahani.me",
    "https://vimaln2005.github.io",
    "http://localhost:3000",
    "http://localhost:5500",
    "http://localhost:8000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static folder for uploaded photos
UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(os.path.join(UPLOAD_DIR, "uploads"), exist_ok=True)
app.mount("/static", StaticFiles(directory=UPLOAD_DIR), name="static")

# Include Routers
app.include_router(projects.router)
app.include_router(upload.router)
app.include_router(contact.router)
app.include_router(ai_copilot.router)

@app.get("/", tags=["Health"])
def root():
    return {
        "status": "online",
        "service": "Vimal Sahani Portfolio API",
        "docs": "/docs",
        "author": "Vimal Sahani",
        "portfolio": "https://vimalsahani.me"
    }

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "healthy", "database": "connected"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
