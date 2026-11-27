
from fastapi import FastAPI

import models
from database import engine
from routers import topics

app = FastAPI(
    title="AI Engineer Learning Tracker",
    description="API to manage and track AI Engineer learning progress",
    version="1.0.0"
)

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Register topic routes
app.include_router(topics.router)


@app.get("/")
def home():
    return {
        "message": "AI Learning Tracker API is running"
    }
