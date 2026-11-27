
from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class TopicModel(Base):

    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    day = Column(Integer, nullable=False)
    completed = Column(Boolean, default=False)
