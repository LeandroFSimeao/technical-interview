# technical-interview

Chat API built with FastAPI and a LangChain agent. The agent answers questions about BEON.tech using documents indexed in memory.

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)

## Setup

```bash
uv sync
```

Create a `.env` file in the project root:

```bash
GOOGLE_API_KEY=...
ANTHROPIC_API_KEY=...
```

`GOOGLE_API_KEY` is used by the `gemini-embedding-2` embedding model. `ANTHROPIC_API_KEY` is used by `claude-haiku-4-5`.

## Start the server

```bash
uv run fastapi dev
```

The API is available at http://localhost:8000. Interactive docs are at http://localhost:8000/docs.

## Endpoint

`POST /chat`

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"What does BEON.tech do?\"}"
```

Response:

```json
{"message": "..."}
```

## Structure

- `main.py` — FastAPI application, agent, and document search
- `pyproject.toml` — project dependencies
