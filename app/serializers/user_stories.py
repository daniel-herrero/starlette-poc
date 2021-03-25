from typing import List, Optional

from pydantic import BaseModel

from pydantic.schema import datetime, Optional


# Shared properties
from app.serializers.attachment import Attachment
from app.serializers.epic import Epic
from app.serializers.project import Project
from app.serializers.task import Task
from app.serializers.user import UserPartial


class UserStoryBase(BaseModel):
    finish_date: Optional[datetime]
    epics: Optional[List[Epic]]
    tasks: Optional[List[Task]]
    attachments: Optional[List[Attachment]]
    external_reference: Optional[str]
    tribe_gig: Optional[str]
    due_date: Optional[str]
    due_date_reason: Optional[str]
    generated_from_task_id: Optional[int]
    from_task_ref: Optional[str]
    swimlane_id: Optional[int]
    assigned_to: Optional[UserPartial]
    generated_from_issue_id: Optional[int]
    milestone_id: Optional[int]


# Properties to receive on task creation
class UserStoryCreate(UserStoryBase):
    tags: List[str]
    is_blocked: bool
    blocked_note: str
    ref: int
    is_closed: bool
    backlog_order: str
    description: str
    client_requirement: bool
    team_requirement: bool
    status_id: int
    sprint_order: int
    kanban_order: int
    version: int
    created_date: datetime
    modified_date: datetime
    subject: str
    owner: UserPartial
    project: Project

    class Config:
        orm_mode = True


# Properties to receive on task update
class UserStoryUpdate(UserStoryBase):
    id: int

    class Config:
        orm_mode = True


# Properties shared by models stored in DB
class UserStoryInDBBase(UserStoryBase):
    id: int

    tags: List[str]
    is_blocked: bool
    blocked_note: str
    ref: int
    is_closed: bool
    backlog_order: str
    description: str
    client_requirement: bool
    team_requirement: bool
    status_id: int
    sprint_order: int
    kanban_order: int
    version: int
    created_date: datetime
    modified_date: datetime
    subject: str
    owner: UserPartial
    project: Project

    class Config:
        orm_mode = True


# Properties to return to client
class UserStory(UserStoryInDBBase):
    pass

    class Config:
        orm_mode = True


# Properties properties stored in DB
class UserStoryInDB(UserStoryInDBBase):
    pass
