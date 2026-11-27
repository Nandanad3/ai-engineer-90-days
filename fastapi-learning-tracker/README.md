# AI Engineer Learning Tracker API

A REST API built using FastAPI to track progress through a 90-day AI Engineer roadmap.

## Technologies
- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication
- Pytest
- Docker

## Features
- User registration and login
- JWT authentication
- Create, read, update and delete learning topics
- Search and filter topics
- Pagination
- Learning progress summary
- User-specific topic access

## Run Locally

pip install -r requirements.txt

uvicorn main:app --reload

## Run with Docker

docker build -t ai-learning-tracker .

docker run --name ai-learning-tracker -p 8000:8000 --env-file .env ai-learning-tracker

## API Documentation

Visit http://localhost:8000/docs