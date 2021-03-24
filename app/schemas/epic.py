from typing import List, Optional

from pydantic import BaseModel

from pydantic.schema import Optional


# Shared properties


# Shared properties
from app.schemas.project import Project


class EpicBase(BaseModel):
    ref: Optional[int]
    # user_stories: Optional[List[UserStory]]


# Properties to receive on task creation
class EpicCreate(EpicBase):
    color: str
    project: Project
    subject: str


# Properties to receive on task update
class EpicUpdate(EpicBase):
    pass


# Properties shared by models stored in DB
class EpicInDBBase(EpicBase):
    id: int
    color: str
    project: Project
    subject: str

    class Config:
        orm_mode = True


# Properties to return to client
class Epic(EpicInDBBase):
    pass


# Properties properties stored in DB
class EpicInDB(EpicInDBBase):
    pass
