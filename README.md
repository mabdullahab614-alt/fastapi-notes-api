<div align="center">

<!-- Animated Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:120a05,40:ff6b35,100:ffb300&height=220&section=header&text=📝%20Notes%20API&fontSize=52&fontColor=ffffff&animation=twinkling&fontAlignY=42&desc=Async%20REST%20API%20·%20FastAPI%20·%20SQLAlchemy%202.0%20·%20Live%20on%20Render&descAlignY=62&descSize=18&descFontColor=ffb300" width="100%"/>

<!-- Live Demo Badge -->
<br/>
<a href="https://fastapi-notes-api-6rpc.onrender.com/docs">
  <img src="https://img.shields.io/badge/🚀%20LIVE%20API-OPEN%20SWAGGER%20DOCS-ff6b35?style=for-the-badge&labelColor=120a05&color=ff6b35" alt="Live API"/>
</a>

<br/><br/>

<!-- Stats Badges -->
<img src="https://img.shields.io/badge/Endpoints-5%20CRUD-ffb300?style=flat-square&labelColor=1a0f05"/>
<img src="https://img.shields.io/badge/Framework-FastAPI-ff6b35?style=flat-square&labelColor=1a0f05&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/ORM-SQLAlchemy%202.0%20Async-ffb300?style=flat-square&labelColor=1a0f05"/>
<img src="https://img.shields.io/badge/Database-SQLite-ff6b35?style=flat-square&labelColor=1a0f05&logo=sqlite&logoColor=white"/>
<img src="https://img.shields.io/badge/Validation-Pydantic%20v2-ffb300?style=flat-square&labelColor=1a0f05"/>
<img src="https://img.shields.io/badge/Python-3.13-blue?style=flat-square&labelColor=1a0f05&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Deploy-Render-ff6b35?style=flat-square&labelColor=1a0f05"/>
<img src="https://img.shields.io/badge/Status-Live%20%F0%9F%9F%A2-ffb300?style=flat-square&labelColor=1a0f05"/>
<a href="#-license"><img src="https://img.shields.io/badge/License-All%20Rights%20Reserved-DC2626?style=flat-square&labelColor=1a0f05"/></a>

</div>

---

## 🌍 About

**Notes API** is a fully asynchronous REST backend that lets users **create, read, update and delete notes**. Built with **FastAPI** and **async SQLAlchemy 2.0**, it ships with automatic interactive documentation (Swagger UI) and is deployed live on Render.

This is **Day 1** of my daily AI-engineering project challenge — the foundation that later days (PostgreSQL, JWT auth, RAG) build on.

> ✨ **Built by Abdullah Javid** | AI Developer & Backend Builder

---

## 🚀 Live Demo

<div align="center">

[![Try Live](https://img.shields.io/badge/🚀%20Render-OPEN%20LIVE%20API-ff6b35?style=for-the-badge&labelColor=120a05)](https://fastapi-notes-api-6rpc.onrender.com/docs)

</div>

> ⏳ Hosted on Render's free tier — the first request after inactivity can take 30–60 seconds to wake the server.

---

## 🔌 API Endpoints

| # | Method | Path | Description | Success Code |
|---|--------|------|-------------|--------------|
| 1 | `GET` | `/` | Health check | 200 |
| 2 | `POST` | `/notes` | Create a note | 201 |
| 3 | `GET` | `/notes` | List all notes (newest first) | 200 |
| 4 | `GET` | `/notes/{id}` | Get a single note | 200 |
| 5 | `PUT` | `/notes/{id}` | Update a note | 200 |
| 6 | `DELETE` | `/notes/{id}` | Delete a note | 204 |

Missing notes return `404 {"detail": "Note not found"}`; invalid bodies return `422`.

### Example

```bash
curl -X POST https://fastapi-notes-api-6rpc.onrender.com/notes \
  -H "Content-Type: application/json" \
  -d '{"title": "My first note", "content": "FastAPI is working!"}'
```

```json
{
  "title": "My first note",
  "content": "FastAPI is working!",
  "id": 1,
  "created_at": "2026-11-15T06:45:09.826520"
}
```

---

## 🧠 Architecture

```
Client (Swagger UI / curl / frontend)
    ↓
FastAPI Router (async endpoints)
    ↓
Pydantic v2 (request / response validation)
    ↓
Dependency Injection → AsyncSession
    ↓
SQLAlchemy 2.0 (async ORM)
    ↓
aiosqlite → SQLite (notes.db)
```

**Key design choices:**
- **Fully async** — endpoints, DB sessions and queries all use `async`/`await`
- **Dependency injection** — `get_db()` yields one session per request
- **Lifespan handler** — tables are created automatically at startup
- **Schema separation** — `NoteIn` for input, `NoteOut` for output (adds `id`, `created_at`)

---

## 📁 Project Structure

```
fastapi-notes-api/
│
├── main.py                 # FastAPI app, models, schemas, endpoints
├── requirements.txt        # Python dependencies
├── .python-version         # Python version for Render
├── .gitignore              # Ignores venv, notes.db, caches
└── README.md               # Project documentation
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) | Web framework |
| ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white) | Async ORM |
| ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white) | Database |
| ![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white) | Data validation |
| ![Uvicorn](https://img.shields.io/badge/Uvicorn-499848?style=flat-square) | ASGI server |
| ![Render](https://img.shields.io/badge/Render-46E3B7?style=flat-square&logo=render&logoColor=black) | Deployment |
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) | Language |
| ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) | Version control |

---

## ⚡ Run Locally

```bash
# 1. Clone
git clone https://github.com/mabdullahab614-alt/fastapi-notes-api.git
cd fastapi-notes-api

# 2. Virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

# 3. Install & run
pip install -r requirements.txt
uvicorn main:app --reload
```

Open **http://127.0.0.1:8000/docs** for the interactive Swagger UI.

---

## 🌟 Key Features

- ⚡ **Async end-to-end** — non-blocking database access
- 📖 **Auto-generated docs** — Swagger UI at `/docs`
- ✅ **Input validation** — Pydantic v2 with clear 422 errors
- 🧯 **Proper error handling** — 404 for missing notes
- ☁️ **Deployed live** — free hosting on Render
- 🧩 **Extensible base** — ready for PostgreSQL and JWT auth

---

## 🗺️ Roadmap

| Day | Upgrade | Status |
|-----|---------|--------|
| 1 | Async CRUD API + deploy | ✅ Done |
| 2 | PostgreSQL (Neon) + JWT authentication | 🔜 Next |
| 3 | Document Q&A with RAG | ⏳ Planned |
| 7 | Docker + GitHub Actions CI | ⏳ Planned |

> ⚠️ **Note:** Render's free tier has an ephemeral filesystem, so the SQLite file resets on restart. Day 2 moves to PostgreSQL to fix this.

---

## 📜 License

**All Rights Reserved © 2026 Abdullah Javid**

This repository and its contents — including source code and documentation — are made publicly visible **for portfolio and demonstration purposes only**.

**No part of this repository may be copied, modified, distributed, sublicensed, or used** — in whole or in part, for personal, educational, or commercial purposes — without explicit prior written permission from the author.

Forking or cloning this repository does **not** grant any rights to use, reproduce, or redistribute its contents.

If you are interested in using any part of this project, please contact me directly for permission:

📧 **Email:** mabdullah.ab614@gmail.com
🔗 **GitHub:** [github.com/mabdullahab614-alt](https://github.com/mabdullahab614-alt)
💼 **LinkedIn:** [linkedin.com/in/abdullah-javid-b217a2384](https://www.linkedin.com/in/abdullah-javid-b217a2384/)

---

## 👨‍💻 Developer

<div align="center">

**Abdullah Javid**
AI Developer · ML Engineer · Backend Builder

[![GitHub](https://img.shields.io/badge/GitHub-mabdullahab614--alt-181717?style=flat-square&logo=github)](https://github.com/mabdullahab614-alt)
[![Email](https://img.shields.io/badge/Email-mabdullah.ab614%40gmail.com-ff2d2d?style=flat-square&logo=gmail&logoColor=white)](mailto:mabdullah.ab614@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Abdullah%20Javid-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abdullah-javid-b217a2384/)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Abdullah--Javid-yellow?style=flat-square&logo=huggingface)](https://huggingface.co/Abdullah-Javid)

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:ffb300,60:ff6b35,100:120a05&height=120&section=footer&text=📝%20Day%201%20of%20Daily%20AI%20Projects&fontSize=22&fontColor=ffffff&animation=twinkling&fontAlignY=65" width="100%"/>

**⭐ Star this repo if you found it useful!**

*📝 Notes API | Built by Abdullah Javid | FastAPI + Async SQLAlchemy*

</div>
