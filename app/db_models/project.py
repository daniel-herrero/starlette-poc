from typing import TYPE_CHECKING

from sqlalchemy import ARRAY, BigInteger, Boolean, Column, ForeignKey, Float, Integer, String, TIMESTAMP, Text, JSON,\
    UniqueConstraint
from sqlalchemy.orm import relationship

from app.core.database import Base


if TYPE_CHECKING:
    from .user import User
    from .project import Project
    from .epic import Epic


class Project(Base):
    __tablename__ = 'projects_project'

    id = Column(Integer, primary_key=True)
    tags = Column(JSON)
    name = Column(String)
    slug = Column(String)
    description = Column(String)
    created_date = Column(TIMESTAMP)
    modified_date = Column(TIMESTAMP)
    total_milestones = Column(Integer)
    total_story_points = Column(Float)
    is_backlog_activated = Column(Boolean)
    is_kanban_activated = Column(Boolean)
    is_wiki_activated = Column(Boolean)
    is_issues_activated = Column(Boolean)
    videoconferences = Column(String)
    videoconferences_extra_data = Column(String)
    anon_permissions = Column(JSON)
    public_permissions = Column(JSON)
    is_private = Column(Boolean)
    tags_colors = Column(ARRAY(String))
    owner_id = Column(ForeignKey('users_user.id', deferrable=True, initially='DEFERRED'), index=True)
    creation_template_id = Column(Integer)
    default_issue_status_id = Column(Integer)
    default_issue_type_id = Column(Integer)
    default_points_id = Column(Integer)
    default_priority_id = Column(Integer)
    default_severity_id = Column(Integer)
    default_task_status_id = Column(Integer)
    default_us_status_id = Column(Integer)
    issues_csv_uuid = Column(String, index=True)
    tasks_csv_uuid = Column(String, index=True)
    userstories_csv_uuid = Column(String, index=True)
    is_featured = Column(Boolean)
    is_looking_for_people = Column(Boolean)
    total_activity = Column(Integer, index=True)
    total_activity_last_month = Column(Integer, index=True)
    total_activity_last_week = Column(Integer, index=True)
    total_activity_last_year = Column(Integer, index=True)
    total_fans = Column(Integer, index=True)
    total_fans_last_month = Column(Integer, index=True)
    total_fans_last_week = Column(Integer, index=True)
    total_fans_last_year = Column(Integer, index=True)
    totals_updated_datetime = Column(TIMESTAMP, index=True)
    logo = Column(String)
    looking_for_people_note = Column(String)
    blocked_code = Column(String)
    transfer_token = Column(String)
    is_epics_activated = Column(Boolean)
    default_epic_status_id = Column(Integer)
    epics_csv_uuid = Column(String, index=True)
    is_contact_activated = Column(Boolean)
    default_swimlane_id = Column(ForeignKey('projects_swimlane.id', deferrable=True, initially='DEFERRED'), unique=True)

    owner = relationship("User", foreign_keys=[owner_id])
    default_swimlane = relationship('ProjectsSwimlane', foreign_keys=[default_swimlane_id])


class ProjectsSwimlane(Base):
    __tablename__ = 'projects_swimlane'
    __table_args__ = (
        UniqueConstraint('project_id', 'name'),
    )

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    order = Column(BigInteger)
    project_id = Column(ForeignKey('projects_project.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    project = relationship('Project', foreign_keys=[project_id])
