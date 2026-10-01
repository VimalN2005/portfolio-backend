# ⚡ Vimal Sahani — Portfolio Backend API Service

[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-009688.svg?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.11%20%7C%203.12-3776AB.svg?style=flat&logo=python&logoColor=white)](https://python.org)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-D71F00.svg?style=flat&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Ready-336791.svg?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Render](https://img.shields.io/badge/Render-Deployed-46E3B7.svg?style=flat&logo=render&logoColor=white)](https://render.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

High-performance, asynchronous RESTful API service powering **[vimalsahani.me](https://vimalsahani.me)**. Built with **FastAPI**, **SQLAlchemy ORM**, and **Pydantic v2** to provide media uploads, dynamic project management, recruiter inquiries, and an intelligent portfolio AI copilot.

---

## 🏛️ 2D System Architecture

```mermaid
flowchart TD
    Client["Client Browser (vimalsahani.me)"] -->|"HTTPS / JSON"| Gateway["Reverse Proxy / Cloudflare CDN"]
    
    subgraph FastAPI_Backend ["FastAPI Backend Application"]
        Gateway -->|"Port 8000"| App["FastAPI ASGI Core"]
        
        subgraph Middleware_Layer ["Middleware Layer"]
            App --> CORS["CORS Middleware (Allowed Origins)"]
            CORS --> Auth["Admin Secret Key Validator"]
        end
        
        subgraph Router_Layer ["API Routers (/api)"]
            Auth --> R_Upload["/api/upload (Media Upload)"]
            Auth --> R_Projects["/api/projects (Project CRUD)"]
            Auth --> R_Contact["/api/contact (Recruiter Inquiries)"]
            Auth --> R_AI["/api/ai/chat (Portfolio Copilot)"]
        end
        
        subgraph Service_Layer ["Service & Business Logic"]
            R_Upload --> V_Upload["MIME & Size Validator (Max 10MB)"]
            R_Projects --> V_Projects["Project Auto-Seeder & Serializer"]
            R_Contact --> V_Contact["Message Ingestion & Notification"]
            R_AI --> V_AI["Context Knowledge Retrieval Engine"]
        end
    end
    
    subgraph Data_Storage ["Persistence & Storage Layer"]
        V_Upload --> Disk["Static Storage / Cloudinary (static/uploads/)"]
        V_Upload -.-> DB[(PostgreSQL / SQLite)]
        V_Projects --> DB
        V_Contact --> DB
    end
```

---

## 🗄️ Entity-Relationship (ER) Diagram

```mermaid
erDiagram
    PROJECTS {
        int id PK "Primary Key (Auto-Increment)"
        string title "Project Name"
        text description "Detailed System Overview"
        string category "backend | ai | systems"
        string tech_stack "Comma-separated Technologies"
        string github_url "Source Code Repository URL"
        string live_url "Live Production Deployment URL"
        string image_url "Media Asset URL"
        datetime created_at "UTC Timestamp"
    }

    UPLOADED_MEDIA {
        int id PK "Primary Key (Auto-Increment)"
        string filename "Original File Name"
        string file_url "Public Static File Path"
        string content_type "MIME Type (image/png, image/jpeg, etc.)"
        datetime uploaded_at "UTC Timestamp"
    }

    CONTACT_MESSAGES {
        int id PK "Primary Key (Auto-Increment)"
        string name "Recruiter / Visitor Name"
        string email "Sender Contact Email"
        string subject "Inquiry Subject Line"
        text message "Full Message Content"
        datetime created_at "UTC Timestamp"
    }
```

---

## ⚡ Core API Endpoints

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :---: |
| `GET` | `/` | API status, health check & service metadata | No |
| `GET` | `/docs` | Interactive Swagger UI API documentation | No |
| `POST` | `/api/upload` | Upload photos and media assets with MIME checks | Optional |
| `GET` | `/api/projects` | List all projects (supports category filter) | No |
| `POST` | `/api/projects` | Add or update a portfolio project | **Yes** (`x-admin-key`) |
| `DELETE` | `/api/projects/{id}` | Delete a project by ID | **Yes** (`x-admin-key`) |
| `POST` | `/api/contact` | Submit recruiter inquiries & messages | No |
| `GET` | `/api/contact/messages` | Retrieve all incoming contact submissions | No |
| `POST` | `/api/ai/chat` | Query the portfolio AI copilot about Vimal's experience | No |

---

## 🔒 Security & Performance Features

- **Strict MIME Type Validation:** Restricts uploads strictly to `.png`, `.jpg`, `.jpeg`, `.webp`, `.gif`, `.svg`.
- **Payload Limits:** 10MB maximum file size guard preventing memory exhaustion and denial-of-service.
- **Admin Secret Header:** Modifying operations require header validation (`x-admin-key`).
- **CORS Protection:** Pre-configured for `https://vimalsahani.me`, `https://vimaln2005.github.io`, and local development ports.
- **Zero-Downtime Fallback:** Works on local SQLite with zero setup and automatically upgrades to PostgreSQL on cloud environments (`DATABASE_URL`).

---

## 🛠️ Local Development

```bash
# 1. Clone the repository
git clone https://github.com/VimalN2005/portfolio-backend.git
cd portfolio-backend

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start development server with hot-reload
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Access interactive Swagger docs at: **`http://localhost:8000/docs`**

---

## 🐳 Docker Deployment

```bash
# Build Docker image
docker build -t vimal-portfolio-backend .

# Run Docker container
docker run -d -p 8000:8000 --name portfolio-api vimal-portfolio-backend
```

---

## ☁️ 1-Click Render.com Deployment

This repository includes a native `render.yaml` blueprint:

1. Sign in to [Render.com](https://render.com) using your GitHub account.
2. Select **New +** $\rightarrow$ **Web Service**.
3. Connect `VimalN2005/portfolio-backend`.
4. Render will auto-detect settings from `render.yaml`:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Click **Deploy Web Service**!

---

## 👤 Author

**Vimal Sahani**  
B.Tech IT @ IIIT Bhopal ('27) • Backend & AI Systems Engineer  
- 🌐 Website: [vimalsahani.me](https://vimalsahani.me)  
- 🐙 GitHub: [@VimalN2005](https://github.com/VimalN2005)  
- 💼 LinkedIn: [vimal-sahani](https://www.linkedin.com/in/vimal-sahani)  
- 📧 Email: [vimalsahani2005@gmail.com](mailto:vimalsahani2005@gmail.com)
