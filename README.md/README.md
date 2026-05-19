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

Advanced-LangChain-LangGraph-Part1/
├── notebooks/
├── data/
├── chroma_db/
├── database/
├── exports/
├── .env
├── requirements.txt
└── README.md

---

## ⚡ Quick Start

git clone <repo>
cd project

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook

---

## ⚙️ Configuration

GROQ_API_KEY=your_api_key_here

---

## 🐛 Troubleshooting

- Check .env file
- Reinstall dependencies
- Clear chroma_db if needed

---

## 🧭 Roadmap

- Multi-agent systems
- Tool calling agents
- FastAPI deployment
- LangSmith observability

---

## 📄 License

Educational use only.
