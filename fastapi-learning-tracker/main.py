
from fastapi import FastAPI
import auth
import models
from config import settings
from database import engine
from routers import topics

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="API to manage and track AI Engineer learning progress"
)

models.Base.metadata.create_all(bind=engine)

app.include_router(topics.router)
app.include_router(auth.router)


@app.get("/")
def home():
    return {
        "message": "AI Learning Tracker API is running"
    }