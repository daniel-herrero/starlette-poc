from typing import List

from pydantic import BaseModel
from pydantic.schema import datetime, Optional, Dict, Any


class Config:
    arbitrary_types_allowed = True


class UserBase(BaseModel):
    id: int
    password: str
    last_login: Optional[datetime] = None
    is_superuser: bool
    username: str
    email: str
    is_active: bool
    full_name: str
    color: str
    bio: str
    photo: str
    date_joined: datetime
    lang: str
    timezone: str
    colorize_tags: bool
    token:  Optional[str]
    email_token:  Optional[str]
    new_email:  Optional[str]
    is_system: bool
    theme: str
    max_private_projects:  Optional[int]
    max_public_projects:  Optional[int]
    max_memberships_private_projec:  Optional[int]
    max_memberships_public_projects:  Optional[int]
    uuid: str
    accepted_terms: bool
    read_new_terms: bool
    verified_email: bool
    is_staff: bool

    class Config:
        orm_mode = True


class UserStoryBase(BaseModel):
    id: int
    version: int
    tags: List[str]
    id: int
    is_blocked: bool
    blocked_note: str
    ref: int
    is_closed: bool
    backlog_order: str
    created_date: datetime
    modified_date: datetime
    finish_date: Optional[datetime]
    subject: str
    description: str
    client_requirement: bool
    team_requirement: bool
    assigned_to: Optional[UserBase]
    owner: UserBase
    generated_from_issue_id: Optional[int]
    milestone_id: Optional[int]
    project_id: int
    status_id: int
    sprint_order: int
    kanban_order: int
    external_reference: Optional[str]
    tribe_gig: Optional[str]
    due_date: Optional[str]
    due_date_reason: Optional[str]
    generated_from_task_id: Optional[int]
    from_task_ref: Optional[str]
    swimlane_id: Optional[int]

    class Config:
        orm_mode = True