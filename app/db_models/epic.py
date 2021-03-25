from sqlalchemy import BigInteger, Boolean, Column, ForeignKey, Float, Integer, String, TIMESTAMP, Text, JSON, \
    UniqueConstraint
from sqlalchemy.orm import relationship

from app.core.database import Base


class Epic(Base):
    __tablename__ = 'epics_epic'

    id = Column(Integer, primary_key=True)
    tags = Column(JSON)
    version = Column(Integer)
    is_blocked = Column(Boolean)
    blocked_note = Column(Text)
    ref = Column(BigInteger, index=True)
    epics_order = Column(BigInteger)
    created_date = Column(TIMESTAMP)
    modified_date = Column(TIMESTAMP)
    subject = Column(Text)
    description = Column(Text)
    client_requirement = Column(Boolean)
    team_requirement = Column(Boolean)
    assigned_to_id = Column(ForeignKey('users_user.id', deferrable=True, initially='DEFERRED'), index=True)
    owner_id = Column(ForeignKey('users_user.id', deferrable=True, initially='DEFERRED'), index=True)
    project_id = Column(ForeignKey('projects_project.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    color = Column(String)
    external_reference = Column(JSON)

    assigned_to = relationship('User', foreign_keys=[assigned_to_id])
    owner = relationship('User', foreign_keys=[owner_id])
    project = relationship('Project')
    user_stories = relationship("UserStory", secondary = 'epics_relateduserstory')


class EpicsRelateduserstory(Base):
    __tablename__ = 'epics_relateduserstory'
    __table_args__ = (
        UniqueConstraint('user_story_id', 'epic_id'),
    )

    id = Column(Integer, primary_key=True)
    order = Column(BigInteger)
    epic_id = Column(ForeignKey('epics_epic.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    user_story_id = Column(ForeignKey('userstories_userstory.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    epic = relationship('Epic', foreign_keys=[epic_id])
    user_story = relationship('UserStory',foreign_keys=[user_story_id])
