
import models
from sqlalchemy.orm import Session


# Create a topic
def create_topic(db: Session, topic):

    new_topic = models.TopicModel(
        title=topic.title,
        day=topic.day,
        completed=topic.completed
    )

    db.add(new_topic)
    db.commit()
    db.refresh(new_topic)

    return new_topic


# Get all topics
def get_all_topics(db: Session):

    return db.query(models.TopicModel).all()


# Get topic by ID
def get_topic_by_id(db: Session, topic_id: int):

    return db.query(models.TopicModel).filter(
        models.TopicModel.id == topic_id
    ).first()


# Delete a topic
def delete_topic(db: Session, topic):

    db.delete(topic)
    db.commit()

    return True

def get_progress(db: Session):

    total = db.query(models.TopicModel).count()

    completed = db.query(models.TopicModel).filter(
        models.TopicModel.completed == True
    ).count()

    pending = total - completed

    if total == 0:
        percentage = 0
    else:
        percentage = round((completed / total) * 100, 2)

    return {
        "total_topics": total,
        "completed_topics": completed,
        "pending_topics": pending,
        "completion_percentage": percentage
    }
