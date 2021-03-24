from pydantic import BaseModel

from pydantic.schema import datetime, Optional


# Shared properties
class DbActivityBase(BaseModel):
    obj_changes: Optional[dict]
    created_at: datetime
    event: str
    project_id: int
    obj_id: int
    obj_type: str


# Properties to receive on task creation
class DbActivityCreate(DbActivityBase):
    pass


# Properties to receive on task update
class DbActivityUpdate(DbActivityBase):
    pass


# Properties shared by models stored in DB
class DbActivityInDBBase(DbActivityBase):
    id: int
    created_at: datetime
    event: str
    project_id: int
    obj_id: int
    obj_type: str

    class Config:
        orm_mode = True


# Properties to return to client
class DbActivity(DbActivityInDBBase):
    pass

    class Config:
        orm_mode = True

# Properties properties stored in DB
class DbActivityInDB(DbActivityInDBBase):
    pass
