from sqlalchemy import ARRAY, Boolean, Column, DateTime, ForeignKey, Float, Integer, String, Date, TIMESTAMP, Text, JSON
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
    owner_id = Column(ForeignKey('users_user.id'))
    creation_template_id = Column(Integer)
    default_issue_status_id = Column(Integer)
    default_issue_type_id = Column(Integer)
    default_points_id = Column(Integer)
    default_priority_id = Column(Integer)
    default_severity_id = Column(Integer)
    default_task_status_id = Column(Integer)
    default_us_status_id = Column(Integer)
    issues_csv_uuid = Column(String)
    tasks_csv_uuid = Column(String)
    userstories_csv_uuid = Column(String)
    is_featured = Column(Boolean)
    is_looking_for_people = Column(Boolean)
    total_activity = Column(Integer)
    total_activity_last_month = Column(Integer)
    total_activity_last_week = Column(Integer)
    total_activity_last_year = Column(Integer)
    total_fans = Column(Integer)
    total_fans_last_month = Column(Integer)
    total_fans_last_week = Column(Integer)
    total_fans_last_year = Column(Integer)
    totals_updated_datetime = Column(TIMESTAMP)
    logo = Column(String)
    looking_for_people_note = Column(String)
    blocked_code = Column(String)
    transfer_token = Column(String)
    is_epics_activated = Column(Boolean)
    default_epic_status_id = Column(Integer)
    epics_csv_uuid = Column(String)
    is_contact_activated = Column(Boolean)
    default_swimlane_id = Column(Integer)

    owner = relationship("User", foreign_keys=[owner_id])


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
    generated_from_issue_id = Column(Integer)
    milestone_id = Column(Integer)
    project_id = Column(Integer, ForeignKey('projects_project.id'))
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

    __mapper_args__ = {
        # https://docs.sqlalchemy.org/en/14/orm/versioning.html?highlight=concurrency
        'version_id_col': version,
        # 'version_id_generator': lambda version: version+1
        # it automatically increases the version on any update/delete operation
    }
