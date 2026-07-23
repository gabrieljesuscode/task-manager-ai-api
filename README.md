# Task Manager AI - API

API do Task Manager AI. CRUD de tarefas desenvolvido com FastAPI e PostgreSQL.

Deploy da aplicação com Vercel e Supabase: [https://task-manager-ai-web.vercel.app/](url)

<img width="1707" height="545" alt="Task Manager AI API" src="https://github.com/user-attachments/assets/5229cf2a-0abd-477f-93a0-8e7ebbc7096e" />

## Stack

- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Pytest

## Funcionalidades

- CRUD completo de tarefas
- Migrations com Alembic
- Testes automatizados
- Documentação automática com Swagger

## Rodando localmente

```bash
git clone https://github.com/gabrieljesuscode/task-manager-ai-api.git

cd task-manager-ai-api
```

python -m venv .venv

### Linux/macOS
source .venv/bin/activate

### Windows
.venv\Scripts\activate

pip install -r requirements.txt

### Configure o arquivo .env com a DATABASE_URL

alembic upgrade head

uvicorn app.main:app --reload


## Documentação

API Publicada:

https://task-manager-ai-api.vercel.app/docs

Esta API está disponível publicamente apenas para fins de demonstração.

## Principais endpoints

| Método | Endpoint |
|---------|----------|
| GET | `/tasks` |
| GET | `/tasks/{id}` |
| POST | `/tasks` |
| PUT | `/tasks/{id}` |
| DELETE | `/tasks/{id}` |
| POST | `/ai/categorize` |

## Front-end

https://github.com/gabrieljesuscode/task-manager-ai-web

---

Gabriel da Silva de Jesus
