# Advanced LangChain & LangGraph: Production RAG & Multi-Agent Systems (Part 1)

A production-oriented reference implementation for advanced prompt engineering, modular Retrieval-Augmented Generation (RAG) pipelines, and stateful multi-agent orchestration using LangChain and LangGraph.

This project focuses on real-world LLM engineering patterns including state management, deterministic routing, hybrid retrieval systems, and scalable agent workflows.

---

## 📌 Table of Contents

- Overview
- Key Features
- System Architecture
- Project Structure
- Quick Start
- Installation
- Configuration
- Usage
- Core Components
- Troubleshooting
- Roadmap
- License

---

## 🧠 Overview

This repository demonstrates production-grade AI system design:
- Advanced prompt engineering (CoT, Few-shot)
- RAG pipelines with vector storage
- Stateful multi-agent orchestration
- Hybrid memory systems

---

## ✨ Key Features

### ⚡ High-Performance LLM Inference
- Groq API integration

### 🔍 RAG Pipeline
- PDF ingestion
- Sentence Transformer embeddings
- ChromaDB vector storage

### 🧠 LangGraph Workflows
- Graph-based agent execution
- Conditional routing

### 🗄️ Hybrid Memory
- SQLite / PostgreSQL state
- Vector memory retrieval

---

## 🏗️ System Architecture

PDF → Loader → Chunking → Embeddings → ChromaDB → Retrieval → LangGraph → LLM → Response

---

## 📁 Project Structure

```
.
├── notebooks/       # Week 6 tutorial notebook
├── src/             # Shared config (env loading)
├── scripts/         # Maintenance utilities (e.g. sanitize_notebook.py)
├── data/            # Sample PDFs and RAG documents
├── .env.example     # Secret template (copy to .env)
├── requirements.txt
└── README.md
```

`chroma_db/`, `database/`, and `.env` are gitignored.

---

## ⚡ Quick Start

```bash
git clone <your-repo-url>
cd "Advanced LangChain & LangGraph (part 1)"
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux
pip install -r requirements.txt
copy .env.example .env          # then edit .env with your keys
jupyter notebook notebooks/week6_advanced_langgraph.ipynb
```

---

## ⚙️ Configuration

Copy `.env.example` to `.env` and set:

| Variable | Required | Description |
|----------|----------|-------------|
| `GROQ_API_KEY` | Yes | [Groq API key](https://console.groq.com/keys) |
| `POSTGRES_PASSWORD` | For DB cells | Local PostgreSQL password |
| `POSTGRES_HOST` | No | Default `localhost` |
| `POSTGRES_USER` | No | Default `postgres` |
| `POSTGRES_DB` | No | Default `langchain_db` |

**Never commit `.env` or print API keys in notebook outputs.**

---

## 🔒 Security

- API keys and DB passwords live only in `.env` (see `.env.example`).
- Do not print `GROQ_API_KEY` in notebook cells or commit notebook outputs.
- If a key was exposed, rotate it at [Groq Console](https://console.groq.com/keys) before pushing.

---

## 🐛 Troubleshooting

| Issue | Fix |
|-------|-----|
| `GROQ_API_KEY is not set` | Copy `.env.example` → `.env` and add your key |
| GitHub Push Protection | Remove secrets from files/history, rotate key, push again |
| ChromaDB errors | Delete `chroma_db/` and re-run ingestion cells |
| PostgreSQL errors | Ensure Postgres is running; check `.env` credentials |

---

## 🧭 Roadmap

- Multi-agent systems
- Tool calling agents
- FastAPI deployment
- LangSmith observability

---

## 📄 License

Educational use only.
