from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, Text
from sqlalchemy.orm import relationship

from app.database.database import Base

if TYPE_CHECKING:
    from .user import User
    from .user_story import UserStory
    from .project import Project


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