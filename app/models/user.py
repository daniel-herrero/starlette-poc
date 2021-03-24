from sqlalchemy import Boolean, Column, Integer, String, TIMESTAMP
from app.database.database import Base


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
