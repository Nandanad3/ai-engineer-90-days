

import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from fastapi.testclient import TestClient

from main import app
from database import Base, get_db

TEST_DATABASE_URL = "sqlite://"

test_engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=test_engine
)


@pytest.fixture
def client():
    Base.metadata.create_all(bind=test_engine)

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:

        # Register a test user
        test_client.post("/auth/register", json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123"
        })

        # Login and obtain JWT
        response = test_client.post("/auth/login", data={
            "username": "testuser",
            "password": "password123"
        })

        token = response.json()["access_token"]

        # Attach token to all subsequent requests
        test_client.headers.update({
            "Authorization": f"Bearer {token}"
        })

        yield test_client

    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=test_engine)
