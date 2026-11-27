
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database import Base



class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
class TopicModel(Base):

    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    day = Column(Integer, nullable=False)
    completed = Column(Boolean, default=False)
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True
    )
