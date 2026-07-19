# Task Manager AI API

A RESTful API for managing tasks, built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.

This project is the Python backend version of my original **Task Manager AI**, which was first developed with **Java Spring Boot**. The goal was to rebuild the same application while learning the Python backend ecosystem and its best practices.

<img width="1707" height="545" alt="image" src="https://github.com/user-attachments/assets/5229cf2a-0abd-477f-93a0-8e7ebbc7096e" />

## Features

- CRUD operations for tasks
- PostgreSQL database integration
- SQLAlchemy ORM
- Database versioning with Alembic
- Environment variable support with `.env`
- Interactive API documentation with Swagger UI (`/docs`)

## Tech Stack

- Python
- FastAPI
- SQLAlchemy 2.0
- PostgreSQL
- Alembic
- Pydantic
- Python-dotenv
- Uvicorn

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/task-manager-ai-api.git
cd task-manager-ai-api
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/taskdb
```

### 5. Run database migrations

```bash
alembic upgrade head
```

### 6. Start the server

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```
http://localhost:8000
```

Swagger documentation:

```
http://localhost:8000/docs
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/tasks` | List all tasks |
| GET | `/tasks/{task_id}` | Get a task by ID |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

## Project Structure

```text
app/
├── database/
├── models/
├── routers/
├── schemas/
└── main.py

alembic/
requirements.txt
```

## Future Improvements

- AI-powered task categorization
- Task priorities
- Search and filtering
- Authentication and user accounts

## License

This project was created for learning and portfolio purposes.
