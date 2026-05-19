"""
Centralized environment configuration.

Copy `.env.example` to `.env` in the project root and fill in your values.
Never commit `.env` — it is listed in `.gitignore`.
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

# Load variables from `.env` in the project root (parent of `src/`)
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(_PROJECT_ROOT / ".env")

# Groq API — required for all LLM cells in the notebook
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# PostgreSQL — optional; used in the persistence / hybrid-memory section
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB", "langchain_db")

# Hugging Face — optional; improves model download rate limits
HF_TOKEN = os.getenv("HF_TOKEN")


def require_groq_api_key() -> str:
    """Return the Groq API key or raise a clear configuration error."""
    if not GROQ_API_KEY:
        raise ValueError(
            "GROQ_API_KEY is not set. Copy .env.example to .env and add your key "
            "(https://console.groq.com/keys)."
        )
    return GROQ_API_KEY


def require_postgres_password() -> str:
    """Return the PostgreSQL password or raise a clear configuration error."""
    if not POSTGRES_PASSWORD:
        raise ValueError(
            "POSTGRES_PASSWORD is not set. Copy .env.example to .env and set your "
            "local PostgreSQL credentials."
        )
    return POSTGRES_PASSWORD
