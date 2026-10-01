# 🚀 Vimal Sahani — Portfolio Backend API Service

High-performance, scalable backend engine powering **[vimalsahani.me](https://vimalsahani.me)**.

Built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL/SQLite** to support:
- 📸 **Photo & Media Uploads** (`POST /api/upload`) with MIME validation & unique UUID hashing.
- 📦 **Dynamic Project Management** (`GET /api/projects`, `POST /api/projects`) with admin secret authentication.
- 📬 **Recruiter Inquiries** (`POST /api/contact`, `GET /api/contact/messages`).
- 🤖 **Portfolio AI Copilot** (`POST /api/ai/chat`) answering recruiter questions regarding open source contributions, architecture decisions, and tech stack.
- ⚡ **Auto OpenAPI Docs** accessible at `/docs` (Swagger UI) and `/redoc`.

---

## 🛠️ Quick Local Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the development server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
Open **`http://localhost:8000/docs`** to see the interactive Swagger UI API documentation.

---

## ☁️ Deployment to Render (100% Free)

1. Create a new public repository on GitHub: `VimalN2005/portfolio-backend`
2. Push this directory to the repository:
   ```bash
   git init
   git add .
   git commit -m "Initial commit of portfolio backend"
   git remote add origin https://github.com/VimalN2005/portfolio-backend.git
   git branch -M main
   git push -u origin main
   ```
3. Go to [Render.com](https://render.com) -> **New Web Service** -> Connect `portfolio-backend`.
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Click **Deploy**!
