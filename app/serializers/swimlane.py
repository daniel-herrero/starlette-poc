from pydantic import BaseModel

from app.serializers.project import Project


# Shared properties
class SwimlaneBase(BaseModel):
    pass


# Properties to receive on task creation
class SwimlaneCreate(SwimlaneBase):
    name: str
    order: int
    project: Project

# Properties to receive on task update
class SwimlaneUpdate(SwimlaneBase):
    pass


# Properties shared by models stored in DB
class SwimlaneInDBBase(SwimlaneBase):
    id: int

    name: str
    order: int
    project: Project

    class Config:
        orm_mode = True


# Properties to return to client
class Swimlane(SwimlaneInDBBase):
    pass


# Properties properties stored in DB
class SwimlaneInDB(SwimlaneInDBBase):
    pass
