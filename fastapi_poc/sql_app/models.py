from sqlalchemy import ARRAY, BigInteger, Boolean, CheckConstraint, Column, DateTime, ForeignKey, Float, Integer, String, Date, TIMESTAMP, Text, JSON, UniqueConstraint
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
    epics = relationship("Epic", secondary = 'epics_relateduserstory')
    tasks = relationship('Task', primaryjoin='Task.user_story_id == UserStory.id')
    attachments = relationship('Attachment', primaryjoin='Attachment.object_id == UserStory.id')

    __mapper_args__ = {
        # https://docs.sqlalchemy.org/en/14/orm/versioning.html?highlight=concurrency
        'version_id_col': version,
        # 'version_id_generator': lambda version: version+1
        # it automatically increases the version on any update/delete operation
    }


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
    owner_id = Column(ForeignKey('users_user.id', deferrable=True, initially='DEFERRED'), index=True)
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