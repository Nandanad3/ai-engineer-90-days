
from pydantic import BaseModel, Field, ConfigDict


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
