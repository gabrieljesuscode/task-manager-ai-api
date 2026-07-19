# Task Manager AI API

A **RESTful Task Manager API** built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.

This project was developed to explore the Python backend ecosystem while applying modern backend development practices such as ORM mapping, database migrations, dependency injection, automated testing, and API documentation.

<img width="1707" height="545" alt="Task Manager AI API" src="https://github.com/user-attachments/assets/5229cf2a-0abd-477f-93a0-8e7ebbc7096e" />

## Features

- Full CRUD operations for tasks
- PostgreSQL database integration
- SQLAlchemy ORM
- Database migrations with Alembic
- Automated testing with Pytest
- Interactive Swagger documentation
- Environment variables with `.env`

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic
- Pytest

## Getting Started

```bash
git clone https://github.com/gabrieljesuscode/task-manager-ai-api.git
cd task-manager-ai-api

python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate

pip install -r requirements.txt

# Create a .env file with your DATABASE_URL

alembic upgrade head

uvicorn app.main:app --reload
```

The API will be available at:

- http://localhost:8000
- http://localhost:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/tasks` | List all tasks |
| GET | `/tasks/{task_id}` | Get a task by ID |
| POST | `/tasks` | Create a task |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

## Future Improvements

- AI-powered task categorization
- Task priorities
- Search and filtering
- Authentication and user accounts

## License

This project was created for learning and portfolio purposes.