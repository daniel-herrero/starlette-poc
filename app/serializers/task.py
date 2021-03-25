from typing import List, Optional

from pydantic import BaseModel

from pydantic.schema import datetime, Optional

# Shared properties
from app.serializers.user import UserPartial


class TaskBase(BaseModel):
    ref: Optional[int]
    status_id: Optional[int]


# Properties to receive on task creation
class TaskCreate(TaskBase):
    is_blocked: bool
    is_iocaine: bool
    subject: str


# Properties to receive on task update
class TaskUpdate(TaskBase):
    pass


# Properties shared by models stored in DB
class TaskInDBBase(TaskBase):
    id: int
    is_blocked: bool
    is_iocaine: bool
    subject: str
    tags: Optional[List[str]]
    version: int
    blocked_note: str
    created_date: datetime
    modified_date: datetime
    finished_date: Optional[datetime]
    description: str
    assigned_to: Optional[UserPartial]
    milestone_id: Optional[int]
    owner: UserPartial
    # project: Project
    status_id: int
    # user_story: UserStory
    taskboard_order: int
    us_order: int
    external_reference: Optional[List[str]]
    due_date: Optional[datetime]
    due_date_reason: str

    class Config:
        orm_mode = True


# Properties to return to client
class Task(TaskInDBBase):
    pass


# Properties properties stored in DB
class TaskInDB(TaskInDBBase):
    pass
