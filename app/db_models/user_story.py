from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, TIMESTAMP, JSON, Text
from sqlalchemy.orm import relationship

from app.core.database import Base


class UserStory(Base):
    __tablename__ = 'userstories_userstory'

    id = Column(Integer, primary_key=True)
    tags = Column(JSON)
    version = Column(Integer, nullable=False)
    is_blocked = Column(Boolean)
    blocked_note = Column(String)
    ref = Column(Integer, index=True)
    is_closed = Column(Boolean)
    backlog_order = Column(String)
    created_date = Column(TIMESTAMP)
    modified_date = Column(TIMESTAMP)
    finish_date = Column(TIMESTAMP)
    subject = Column(String)
    description = Column(String)
    client_requirement = Column(Boolean)
    team_requirement = Column(Boolean)
    assigned_to_id = Column(Integer, ForeignKey('users_user.id', deferrable=True, initially='DEFERRED'), index=True)
    owner_id = Column(Integer, ForeignKey('users_user.id', deferrable=True, initially='DEFERRED'), index=True)
    project_id = Column(Integer, ForeignKey('projects_project.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    generated_from_issue_id = Column(Integer)
    milestone_id = Column(Integer)
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

    assigned_to = relationship("User", foreign_keys=[assigned_to_id])
    owner = relationship("User", foreign_keys=[owner_id])
    project = relationship("Project", foreign_keys=[project_id])
    epics = relationship("Epic", secondary='epics_relateduserstory')
    tasks = relationship('Task', primaryjoin='Task.user_story_id == UserStory.id')
    attachments = relationship('Attachment', primaryjoin='Attachment.object_id == UserStory.id')

    __mapper_args__ = {
        # https://docs.sqlalchemy.org/en/14/orm/versioning.html?highlight=concurrency
        'version_id_col': version,
        # 'version_id_generator': lambda version: version+1
        # it automatically increases the version on any update/delete operation
    }


class Attachment(Base):
    __tablename__ = 'attachments_attachment'

    id = Column(Integer, primary_key=True)
    object_id = Column(ForeignKey('userstories_userstory.id', deferrable=True, initially='DEFERRED'), index=True)
    created_date = Column(TIMESTAMP)
    modified_date = Column(TIMESTAMP)
    attached_file = Column(String)
    is_deprecated = Column(Boolean)
    description = Column(Text)
    order = Column(Integer)
    content_type_id = Column(Integer)
    owner_id = Column(ForeignKey('users_user.id', deferrable=True, initially='DEFERRED'), index=True)
    project_id = Column(ForeignKey('projects_project.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    name = Column(String)
    size = Column(Integer)
    sha1 = Column(String)
    from_comment = Column(Boolean)

    owner = relationship('User', foreign_keys=[owner_id])
    project = relationship('Project', foreign_keys=[project_id])
    user_story = relationship('UserStory', foreign_keys=[object_id])
