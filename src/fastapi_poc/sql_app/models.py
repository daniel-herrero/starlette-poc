from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, TIMESTAMP, Text, JSON
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = 'users_user'

    id = Column(Integer, primary_key=True)
    password = Column(String)
    last_login = Column(TIMESTAMP)
    is_superuser = Column(Boolean)
    username = Column(String)
    email = Column(String)
    is_active = Column(Boolean)
    full_name = Column(String)
    color = Column(String)
    bio = Column(String)
    photo = Column(String)
    date_joined = Column(TIMESTAMP)
    lang = Column(String)
    timezone = Column(String)
    colorize_tags = Column(Boolean)
    token = Column(String)
    email_token = Column(String)
    new_email = Column(String)
    is_system = Column(Boolean)
    theme = Column(String)
    max_private_projects = Column(Integer)
    max_public_projects = Column(Integer)
    max_memberships_private_projects = Column(Integer)
    max_memberships_public_projects = Column(Integer)
    uuid = Column(String)
    accepted_terms = Column(Boolean)
    read_new_terms = Column(Boolean)
    verified_email = Column(Boolean)
    is_staff = Column(Boolean)


class UserStory(Base):
    __tablename__ = 'userstories_userstory'

    id = Column(Integer, primary_key=True)
    tags = Column(JSON)
    version = Column(Integer, nullable=False)
    is_blocked = Column(Boolean)
    blocked_note = Column(String)
    ref = Column(Integer)
    is_closed = Column(Boolean)
    backlog_order = Column(String)
    created_date = Column(TIMESTAMP)
    modified_date = Column(TIMESTAMP)
    finish_date = Column(TIMESTAMP)
    subject = Column(String)
    description = Column(String)
    client_requirement = Column(Boolean)
    team_requirement = Column(Boolean)
    assigned_to_id = Column(Integer, ForeignKey('users_user.id'))
    owner_id = Column(Integer, ForeignKey('users_user.id'))
    assigned_to = relationship("User", foreign_keys=[assigned_to_id])
    owner = relationship("User", foreign_keys=[owner_id])
    generated_from_issue_id = Column(Integer)
    milestone_id = Column(Integer)
    project_id = Column(Integer)
    status_id = Column(Integer)
    sprint_order = Column(Integer)
    kanban_order = Column(Integer)
    external_reference = Column(String)
    tribe_gig = Column(String)
    due_date = Column(Date)
    due_date_reason = Column(Date)
    generated_from_task_id = Column(Integer)
    from_task_ref = Column(String)
    swimlane_id = Column(Integer)

    __mapper_args__ = {
        # https://docs.sqlalchemy.org/en/14/orm/versioning.html?highlight=concurrency
        'version_id_col': version,
        # 'version_id_generator': lambda version: version+1
        # it automatically increases the version on any update/delete operation
    }
