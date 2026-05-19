"""Strip notebook outputs and replace hardcoded secrets with env-based config."""

import json
from pathlib import Path

NB_PATH = Path(__file__).resolve().parent.parent / "notebooks" / "week6_advanced_langgraph.ipynb"

ENV_CELL = """# Load secrets from .env (never commit .env — see .env.example)
from dotenv import load_dotenv
import os
import sys

# Allow importing shared config from project root
sys.path.insert(0, os.path.abspath(".."))

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY is not set. Copy .env.example to .env and add your key."
    )

# Confirm configuration without printing the secret
print("GROQ_API_KEY loaded successfully (value hidden).")"""

CHATGROQ_INIT = """from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.3-70b-versatile",  # Updated to a current Groq model
    temperature=0,
    groq_api_key=GROQ_API_KEY,
)

response = llm.invoke("Say hello in 1 sentence")
print(response.content)"""

STREAMING_CELL = """from langchain_groq import ChatGroq
from langchain_core.callbacks import StreamingStdOutCallbackHandler

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    streaming=True,
    groq_api_key=GROQ_API_KEY,
    callbacks=[StreamingStdOutCallbackHandler()],
)

response = llm.invoke("Explain LangGraph in simple words.")"""

PG_CONNECT = """import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

# PostgreSQL credentials from .env (see .env.example)
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_DB = os.getenv("POSTGRES_DB", "langchain_db")
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
if not POSTGRES_PASSWORD:
    raise ValueError(
        "POSTGRES_PASSWORD is not set. Copy .env.example to .env."
    )

conn = psycopg2.connect(
    host=POSTGRES_HOST,
    database=POSTGRES_DB,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
)

cursor = conn.cursor()"""

PG_CREATE_DB = """import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv

load_dotenv()

POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB", "langchain_db")
if not POSTGRES_PASSWORD:
    raise ValueError(
        "POSTGRES_PASSWORD is not set. Copy .env.example to .env."
    )

# Connect to the default postgres database first
conn = psycopg2.connect(
    host=POSTGRES_HOST,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
)

conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = conn.cursor()

try:
    cursor.execute(f"CREATE DATABASE {POSTGRES_DB};")
    print(f"database '{POSTGRES_DB}' created successfully!")
except psycopg2.errors.DuplicateDatabase:
    print(f"'{POSTGRES_DB}' already exists.")
finally:
    cursor.close()
    conn.close()"""


def to_source(text: str) -> list[str]:
    lines = text.split("\n")
    return [line + "\n" for line in lines[:-1]] + ([lines[-1]] if lines[-1] else [])


def main() -> None:
    nb = json.loads(NB_PATH.read_text(encoding="utf-8"))

    for cell in nb["cells"]:
        if cell.get("cell_type") != "code":
            continue
        src = "".join(cell.get("source", []))

        if 'print(os.getenv("GROQ_API_KEY"))' in src:
            cell["source"] = to_source(ENV_CELL)
        elif src.strip().startswith("from langchain_groq import ChatGroq") and "Say hello" in src:
            cell["source"] = to_source(CHATGROQ_INIT)
        elif "StreamingStdOutCallbackHandler" in src:
            cell["source"] = to_source(STREAMING_CELL)
        elif 'password="132311"' in src and "CREATE DATABASE" not in src:
            cell["source"] = to_source(PG_CONNECT)
        elif 'password="132311"' in src:
            cell["source"] = to_source(PG_CREATE_DB)

        cell["outputs"] = []
        cell["execution_count"] = None

    nb["metadata"].pop("widgets", None)
    NB_PATH.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Sanitized: {NB_PATH}")


if __name__ == "__main__":
    main()
