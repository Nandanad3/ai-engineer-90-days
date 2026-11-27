
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

import models
from database import get_db
from schemas import Topic, TopicResponse
from services import topic_service
from dependencies import get_current_user
router = APIRouter(
    prefix="/topics",
    tags=["Topics"],
    dependencies=[Depends(get_current_user)]
)


# GET all topics
@router.get("/", response_model=list[TopicResponse])
def get_topics(db: Session = Depends(get_db),current_user: models.UserModel = Depends(get_current_user)):

    return topic_service.get_all_topics(db, current_user.id)


# POST - Create a topic
@router.post("/", response_model=TopicResponse)
def add_topic(
    topic: Topic,
    db: Session = Depends(get_db),
    current_user: models.UserModel = Depends(get_current_user)
):
    return topic_service.create_topic(db, topic, current_user.id)

# GET - Search topics
@router.get("/search", response_model=list[TopicResponse])
def search_topics(keyword: str, db: Session = Depends(get_db),current_user: models.UserModel = Depends(get_current_user)):

    return db.query(models.TopicModel).filter(
         models.TopicModel.user_id == current_user.id,
        models.TopicModel.title.ilike(f"%{keyword}%")
    ).all()


# GET - Filter topics
@router.get("/filter", response_model=list[TopicResponse])
def filter_topics(completed: bool, db: Session = Depends(get_db),current_user: models.UserModel = Depends(get_current_user)):

    return db.query(models.TopicModel).filter(
         models.TopicModel.user_id == current_user.id,
        models.TopicModel.completed == completed
    ).all()


# GET - Pagination
@router.get("/page", response_model=list[TopicResponse])
def get_topics_page(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=5, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: models.UserModel = Depends(get_current_user)
):

    return db.query(models.TopicModel).filter(
         models.TopicModel.user_id == current_user.id,
    ).limit(limit).all()


# PUT - Update a topic
@router.put("/{topic_id}", response_model=TopicResponse)
def update_topic(
    topic_id: int,
    updated_topic: Topic,
    db: Session = Depends(get_db),
    current_user: models.UserModel = Depends(get_current_user)
):
    topic = topic_service.get_topic_by_id(db, topic_id, current_user.id)

    if topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")

    topic.title = updated_topic.title
    topic.day = updated_topic.day
    topic.completed = updated_topic.completed

    db.commit()
    db.refresh(topic)

    return topic


# DELETE - Delete a topic
@router.delete("/{topic_id}")
def delete_topic(
    topic_id: int,
    db: Session = Depends(get_db),
    current_user: models.UserModel = Depends(get_current_user)
):
    topic = topic_service.get_topic_by_id(db, topic_id, current_user.id)

    if topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")

    topic_service.delete_topic(db, topic)

    return {"message": "Topic deleted successfully"}

@router.get("/progress")
def progress_summary(
    db: Session = Depends(get_db),
    current_user: models.UserModel = Depends(get_current_user)
):
    return topic_service.get_progress(db, current_user.id)

# GET - Retrieve one topic
@router.get("/{topic_id}", response_model=TopicResponse)
def get_topic(
    topic_id: int,
    db: Session = Depends(get_db),
    current_user: models.UserModel = Depends(get_current_user)
):
    topic = topic_service.get_topic_by_id(db, topic_id, current_user.id)

    if topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")

    return topic
