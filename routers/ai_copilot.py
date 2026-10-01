import os
from fastapi import APIRouter
from schemas import AIChatRequest, AIChatResponse

router = APIRouter(prefix="/api/ai", tags=["Portfolio AI Assistant"])

KNOWLEDGE_BASE = {
    "django": "Vimal is an active contributor to Django core (PR #21875 - added qualname helper to django.utils.module_loading). He built 'socialFeed' using Django REST Framework with hybrid fan-out pipelines, keyset cursor pagination, and documented with 20 Architecture Decision Records (ADRs).",
    "fastapi": "Vimal uses FastAPI for high-performance microservices, including the 'AI Agent Evaluation & Reliability Platform', 'EdgeFlow' API Gateway (with rate-limiting and model failover), and high-throughput async data APIs.",
    "tensorflow": "Vimal contributed to Google TensorFlow (PR #127639), adding a float64 regression test harness for tf.math.log_sigmoid second derivative calculations in core Python API test suites.",
    "celery": "Vimal has 3 merged PRs in Celery (#10605, #10606, #10607), fixing database backend stamping metadata, task children propagation, and multi-server URL sanitization in distributed worker queues.",
    "huggingface": "Vimal contributed 2 PRs to Hugging Face Transformers (#48489, #48197) optimizing SigLIP2 Flash Attention code examples and VibeVoice speech documentation.",
    "projects": "Vimal has engineered 5 flagship systems: (1) AI Agent Evaluation & Reliability Platform, (2) socialFeed Engine with 20 ADRs, (3) DevPilot Codebase Intelligence, (4) FluxMesh Distributed Orchestrator, (5) EdgeFlow API Gateway.",
    "experience": "Vimal Sahani is a B.Tech IT student ('27) at IIIT Bhopal with 19+ merged pull requests across Google TensorFlow, Django, Celery, and Microsoft PyRIT, holding GitHub Pro, Pull Shark x2, and Galaxy Brain achievements.",
    "internship": "Vimal is actively seeking Software Engineering / Backend Engineering & AI Systems internships. You can reach out at vimalsahani2005@gmail.com or via https://vimalsahani.me."
}

@router.post("/chat", response_model=AIChatResponse)
def chat_with_portfolio_ai(request: AIChatRequest):
    q = request.question.lower()
    matched_skills = []
    response_parts = []

    for key, info in KNOWLEDGE_BASE.items():
        if key in q:
            matched_skills.append(key)
            response_parts.append(info)

    if not response_parts:
        if any(w in q for w in ["who", "vimal", "about", "bio"]):
            answer = KNOWLEDGE_BASE["experience"]
        elif any(w in q for w in ["contact", "email", "hire", "job", "intern"]):
            answer = KNOWLEDGE_BASE["internship"]
        elif any(w in q for w in ["pr", "open source", "contribution"]):
            answer = f"{KNOWLEDGE_BASE['django']} {KNOWLEDGE_BASE['tensorflow']} {KNOWLEDGE_BASE['celery']}"
        else:
            answer = "Vimal Sahani is a Backend & AI Systems Engineer at IIIT Bhopal with 19+ merged PRs across Google TensorFlow, Django, and Celery. Ask me about his Django experience, Celery contributions, AI Agent platform, or internship availability!"
    else:
        answer = " ".join(response_parts)

    return AIChatResponse(
        answer=answer,
        matched_skills=matched_skills or ["General Overview"],
        sources=["https://vimalsahani.me", "https://github.com/VimalN2005"]
    )
