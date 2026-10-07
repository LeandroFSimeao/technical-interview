# technical-interview

API de chat com FastAPI e um agente LangChain. O agente responde perguntas sobre a BEON.tech usando documentos indexados em memória.

## Requisitos

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)

## Configuração

```bash
uv sync
```

Crie um arquivo `.env` na raiz do projeto:

```bash
GOOGLE_API_KEY=...
ANTHROPIC_API_KEY=...
```

`GOOGLE_API_KEY` é usada pelo modelo de embedding `gemini-embedding-2`. `ANTHROPIC_API_KEY` é usada pelo `claude-haiku-4-5`.

## Subir o servidor

```bash
uv run fastapi dev
```

A API fica em http://localhost:8000. A documentação interativa fica em http://localhost:8000/docs.

## Endpoint

`POST /chat`

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"What does BEON.tech do?\"}"
```

Resposta:

```json
{"message": "..."}
```

## Estrutura

- `main.py` — aplicação FastAPI, agente e busca nos documentos
- `pyproject.toml` — dependências do projeto
