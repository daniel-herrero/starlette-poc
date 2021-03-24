from typing import List, Optional

from pydantic import BaseModel

from pydantic.schema import datetime, Optional


# Shared properties
from app.schemas.user import User, UserBase


class ProjectBase(BaseModel):
    total_milestones: Optional[int]
    total_story_points: Optional[float]
    videoconferences: Optional[str]
    videoconferences_extra_data: Optional[str]
    creation_template_id: Optional[int]
    default_issue_status_id: Optional[int]
    default_issue_type_id: Optional[int]
    default_points_id: Optional[int]
    default_priority_id: Optional[int]
    default_severity_id: Optional[int]
    default_task_status_id: Optional[int]
    default_us_status_id: Optional[int]
    issues_csv_uuid: Optional[str]
    tasks_csv_uuid: Optional[str]
    userstories_csv_uuid: Optional[str]
    logo: Optional[str]
    blocked_code: Optional[str]
    transfer_token: Optional[str]
    default_epic_status_id: Optional[int]
    epics_csv_uuid: Optional[str]
    default_swimlane_id: Optional[int]


# Properties to receive on task creation
class ProjectCreate(ProjectBase):
    name: str
    slug: str
    tags: List[str]
    description: str
    created_date: datetime
    modified_date: datetime
    is_backlog_activated: bool
    is_kanban_activated: bool
    is_wiki_activated: bool
    is_issues_activated: bool
    anon_permissions: List[str]
    public_permissions: List[str]
    is_private: bool
    owner: Optional[User]
    is_featured: bool
    is_looking_for_people: bool
    total_activity: int
    total_activity_last_month: int
    total_activity_last_week: int
    total_activity_last_year: int
    total_fans: int
    total_fans_last_month: int
    total_fans_last_week: int
    total_fans_last_year: int
    totals_updated_datetime: datetime
    looking_for_people_note: str
    is_epics_activated: bool
    is_contact_activated: bool


# Properties to receive on task update
class ProjectUpdate(ProjectBase):
    pass


# Properties shared by models stored in DB
class ProjectInDBBase(ProjectBase):
    id: int

    name: str
    slug: str
    tags: List[str]
    description: str
    created_date: datetime
    modified_date: datetime
    is_backlog_activated: bool
    is_kanban_activated: bool
    is_wiki_activated: bool
    is_issues_activated: bool
    anon_permissions: List[str]
    public_permissions: List[str]
    is_private: bool
    owner: Optional[User]
    is_featured: bool
    is_looking_for_people: bool
    total_activity: int
    total_activity_last_month: int
    total_activity_last_week: int
    total_activity_last_year: int
    total_fans: int
    total_fans_last_month: int
    total_fans_last_week: int
    total_fans_last_year: int
    totals_updated_datetime: datetime
    looking_for_people_note: str
    is_epics_activated: bool
    is_contact_activated: bool

    class Config:
        orm_mode = True


# Properties to return to client
class Project(ProjectInDBBase):
    pass


# Properties properties stored in DB
class ProjectInDB(ProjectInDBBase):
    pass
