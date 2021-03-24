from sqlalchemy import Column, Integer, String, TIMESTAMP, JSON
from app.database.database import Base


class DbActivity(Base):
    __tablename__ = 'db_activity'

    id = Column(Integer, primary_key=True)
    created_at = Column(TIMESTAMP)
    event = Column(String)
    obj_id = Column(Integer)
    project_id = Column(Integer)
    obj_type = Column(String)
    obj_changes = Column(JSON, nullable=True)