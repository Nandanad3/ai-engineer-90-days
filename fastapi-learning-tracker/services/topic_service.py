
import models
from sqlalchemy.orm import Session


# Create a topic
def create_topic(db: Session, topic,user_id: int):

    new_topic = models.TopicModel(
        title=topic.title,
        day=topic.day,
        completed=topic.completed,
        user_id=user_id
    )

    db.add(new_topic)
    db.commit()
    db.refresh(new_topic)

    return new_topic


# Get all topics
def get_all_topics(db: Session, user_id: int):
    return db.query(models.TopicModel).filter(
        models.TopicModel.user_id == user_id
    ).all()

# Get topic by ID
def get_topic_by_id(db: Session, topic_id: int, user_id: int):
    return db.query(models.TopicModel).filter(
        models.TopicModel.id == topic_id,
        models.TopicModel.user_id == user_id
    ).first()


# Delete a topic
def delete_topic(db: Session, topic):

    db.delete(topic)
    db.commit()

    return True

def get_progress(db: Session, user_id: int):
    total = db.query(models.TopicModel).filter(
        models.TopicModel.user_id == user_id
    ).count()

    completed = db.query(models.TopicModel).filter(
        models.TopicModel.user_id == user_id,
        models.TopicModel.completed == True
    ).count()

    pending = total - completed

    percentage = round((completed / total) * 100, 2) if total else 0

    return {
        "total_topics": total,
        "completed_topics": completed,
        "pending_topics": pending,
        "completion_percentage": percentage
    }