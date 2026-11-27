# AI Engineer Learning Tracker API

A backend application built with **Python and FastAPI** to manage and track learning progress throughout a 90-day AI Engineer roadmap.

## Features

- User registration and login
- JWT-based authentication
- Secure password hashing using Argon2
- User-specific topic ownership
- Create, read, update and delete learning topics
- Search topics by title
- Filter topics by completion status
- Pagination
- Learning progress summary
- Pydantic request validation
- SQLite database with SQLAlchemy ORM
- Automated API testing using Pytest

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | REST API framework |
| Pydantic | Data validation |
| SQLAlchemy | ORM |
| SQLite | Database |
| JWT | Authentication |
| Argon2 | Password hashing |
| Pytest | Automated testing |

## Project Structure

```text
fastapi-learning-tracker/
├── main.py
├── config.py
├── database.py
├── models.py
├── schemas.py
├── security.py
├── dependencies.py
├── auth.py
├── routers/
│   └── topics.py
├── services/
│   └── topic_service.py
├── tests/
│   ├── conftest.py
│   └── test_main.py
├── .env.example
├── .gitignore
└── requirements.txt
```

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd ai-engineer-90-days/fastapi-learning-tracker
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create your `.env` file using `.env.example` as a template. Set your own secret key.

## Run the Application

```bash
uvicorn main:app --reload
```

Open the interactive API documentation:

http://127.0.0.1:8000/docs

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/register` | Register a user |
| POST | `/auth/login` | Login and obtain JWT |

### Topics

| Method | Endpoint | Description |
|---|---|---|
| GET | `/topics/` | Get user's topics |
| POST | `/topics/` | Create a topic |
| GET | `/topics/{id}` | Get a topic |
| PUT | `/topics/{id}` | Update a topic |
| DELETE | `/topics/{id}` | Delete a topic |
| GET | `/topics/search` | Search topics |
| GET | `/topics/filter` | Filter topics |
| GET | `/topics/page` | Paginated topics |
| GET | `/topics/progress` | View progress summary |

Topic endpoints require JWT authentication.

## Run Tests

```bash
python -m pytest -v
```

## Environment Variables

Configure these variables in `.env`:

- `DATABASE_URL`
- `SECRET_KEY`
- `APP_NAME`
- `APP_VERSION`

Never commit your actual `.env` file or secret key.

## Learning Outcomes

Through this project, I practised:

- Building REST APIs
- Working with JSON and HTTP methods
- Database integration using SQLAlchemy
- Authentication and authorization
- Password hashing and JWT
- Automated testing
- Modular backend architecture

## Future Improvements

- Docker containerization
- PostgreSQL integration
- API deployment
- Frontend dashboard
- Learning analytics and visualizations
