from pydantic import BaseModel


# Shared properties
class AttachementBase(BaseModel):
    pass


# Properties to receive on task creation
class AttachementCreate(AttachementBase):
    attached_file: str


# Properties to receive on task update
class AttachementUpdate(AttachementBase):
    pass


# Properties shared by models stored in DB
class AttachementInDBBase(AttachementBase):
    id: int

    attached_file: str

    class Config:
        orm_mode = True


# Properties to return to client
class Attachement(AttachementInDBBase):
    pass


# Properties properties stored in DB
class AttachementInDB(AttachementInDBBase):
    pass
