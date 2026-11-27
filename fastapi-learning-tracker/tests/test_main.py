
from fastapi.testclient import TestClient
from main import app





def test_home(client):
    response = client.get("/")

    assert response.status_code == 200


def test_get_topics(client):
    response = client.get("/topics/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_topic(client):

    topic_data = {
        "title": "Learn Deep Learning",
        "day": 35,
        "completed": False
    }

    response = client.post("/topics/", json=topic_data)

    assert response.status_code == 200
    assert response.json()["title"] == "Learn Deep Learning"


def test_update_topic(client):

    topic_data = {
        "title": "Learn Advanced Python",
        "day": 5,
        "completed": True
    }

    created = client.post("/topics/", json={
        "title": "Python Basics",
        "day": 1,
        "completed": False
    })

    topic_id = created.json()["id"]

    response = client.put(
        f"/topics/{topic_id}",
        json=topic_data
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Learn Advanced Python"


def test_delete_topic(client):

    created = client.post("/topics/", json={
        "title": "Temporary Topic",
        "day": 10,
        "completed": False
    })

    topic_id = created.json()["id"]

    response = client.delete(f"/topics/{topic_id}")

    assert response.status_code == 200
    assert response.json()["message"] == "Topic deleted successfully"
def test_invalid_topic(client):

    topic_data = {
        "title": "AI",
        "day": 100,
        "completed": False
    }

    response = client.post("/topics/", json=topic_data)

    assert response.status_code == 422
def test_missing_topic(client):
    response = client.get("/topics/9999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Topic not found"
def test_progress(client):
    # Add first topic (completed)
    client.post("/topics/", json={
        "title": "Python Basics",
        "day": 1,
        "completed": True
    })

    # Add second topic (pending)
    client.post("/topics/", json={
        "title": "Machine Learning",
        "day": 31,
        "completed": False
    })

    response = client.get("/topics/progress")

    assert response.status_code == 200

    data = response.json()

    assert data["total_topics"] == 2
    assert data["completed_topics"] == 1
    assert data["pending_topics"] == 1
    assert data["completion_percentage"] == 50.0
def test_search_topics(client):
    client.post("/topics/", json={
        "title": "Python Programming",
        "day": 1,
        "completed": False
    })

    response = client.get("/topics/search?keyword=Python")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["title"] == "Python Programming"
def test_filter_topics(client):
    client.post("/topics/", json={
        "title": "Python Basics",
        "day": 1,
        "completed": True
    })

    client.post("/topics/", json={
        "title": "Machine Learning",
        "day": 31,
        "completed": False
    })

    response = client.get("/topics/filter?completed=true")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["completed"] is True
def test_pagination(client):
    for day in range(1, 6):
        client.post("/topics/", json={
            "title": f"Topic Number {day}",
            "day": day,
            "completed": False
        })

    response = client.get("/topics/page?skip=0&limit=2")

    assert response.status_code == 200
    assert len(response.json()) == 2
def test_unauthorized_access(client):
    client.headers.pop("Authorization")

    response = client.get("/topics/")

    assert response.status_code == 401
def test_user_isolation(client):
    # User 1 creates a topic
    client.post("/topics/", json={
        "title": "Python Programming",
        "day": 1,
        "completed": False
    })

    # Register User 2
    client.post("/auth/register", json={
        "username": "seconduser",
        "email": "second@example.com",
        "password": "password123"
    })

    # Login as User 2
    login_response = client.post("/auth/login", data={
        "username": "seconduser",
        "password": "password123"
    })

    token = login_response.json()["access_token"]

    # Switch to User 2
    client.headers.update({
        "Authorization": f"Bearer {token}"
    })

    # User 2 should not see User 1's topic
    response = client.get("/topics/")

    assert response.status_code == 200
    assert response.json() == []