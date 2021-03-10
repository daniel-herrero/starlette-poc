from sqlalchemy import Column, Integer, String, Table, MetaData, create_engine, TIMESTAMP, \
    Boolean, Date
from sqlalchemy.orm import sessionmaker
import databases

from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
DATABASE_URL = "postgresql://taiga:taiga@localhost:5432/taiga"
Engine = create_engine(DATABASE_URL, encoding='utf-8', echo=True)
Metadata = MetaData()
Session = sessionmaker(bind=Engine)

session = Session()

# Config for databases
Taiga_db = databases.Database(DATABASE_URL)

# Schema definition into SQLAlchemy
projects = Table(
    "projects_project",
    Metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("description", String),
)


# Using SerializerMixin to render as JSON its fields
class Userstory(Base, SerializerMixin):
    __tablename__ = 'userstories_userstory'

    id = Column(Integer, primary_key=True)
    tags = Column(String)
    version = Column(Integer)
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
    assigned_to_id = Column(Integer)
    generated_from_issue_id = Column(Integer)
    milestone_id = Column(Integer)
    owner_id = Column(Integer)
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


# SQLAlchemy queries
all_projects_query = projects.select()


def get_us_by_id(us_id: int):
    # return session.query(Userstory).filter_by(id=us_id).first()
    # return userstory.select().where(userstory.c.id == us_id)
    return session.query(Userstory).get(us_id)


def commit_changes():
    return session.commit()


# Plain SQLs
users_query = """SELECT * from users_user"""

