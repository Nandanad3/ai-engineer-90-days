
from pydantic import BaseModel, Field, ConfigDict, EmailStr


class Topic(BaseModel):
    title: str = Field(min_length=3, max_length=50)
    day: int = Field(gt=0, le=90)
    completed: bool = False


class TopicResponse(BaseModel):
    id: int
    title: str
    day: int
    completed: bool

    model_config = ConfigDict(from_attributes=True)
class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=30)
    email: EmailStr
    password: str = Field(min_length=8)


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)
class UserLogin(BaseModel):
    username: str
    password: str