from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, Boolean, Column, ForeignKey, Integer, Date, TIMESTAMP, Text, JSON
from sqlalchemy.orm import relationship

from app.core.database import Base

# from .user_story import UserStory
# from .user import User
# from .project import Project


class Task(Base):
    __tablename__ = 'tasks_task'

    id = Column(Integer, primary_key=True)
    tags = Column(JSON)
    version = Column(Integer)
    is_blocked = Column(Boolean)
    blocked_note = Column(Text)
    ref = Column(BigInteger)
    created_date = Column(TIMESTAMP)
    modified_date = Column(TIMESTAMP)
    finished_date = Column(TIMESTAMP)
    subject = Column(Text)
    description = Column(Text)
    is_iocaine = Column(Boolean)
    assigned_to_id = Column(ForeignKey('users_user.id', deferrable=True, initially='DEFERRED'), index=True)
    milestone_id = Column(Integer)
    owner_id = Column(Integer, ForeignKey('users_user.id', deferrable=True, initially='DEFERRED'), index=True)
    project_id = Column(ForeignKey('projects_project.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    status_id = Column(Integer)
    user_story_id = Column(ForeignKey('userstories_userstory.id', deferrable=True, initially='DEFERRED'), index=True)
    taskboard_order = Column(BigInteger)
    us_order = Column(BigInteger)
    external_reference = Column(JSON)
    due_date = Column(Date)
    due_date_reason = Column(Text)

    assigned_to = relationship('User', foreign_keys=[assigned_to_id])
    owner = relationship('User', foreign_keys=[owner_id])
    project = relationship('Project', foreign_keys=[project_id])
    user_story = relationship('UserStory', foreign_keys=[user_story_id])