from pydantic import BaseModel

from pydantic.schema import datetime, Optional


class UserPartial(BaseModel):
    """
    Minimum properties to serialize
    """
    id: int
    username: str
    full_name: str
    photo: Optional[str]
    email: str
    color: str
    is_system: bool
    theme: Optional[str]
    uuid: str

    class Config:
        orm_mode = True


class UserFull(UserPartial):
    """
    Complete properties list
    """
    is_active: bool
    is_superuser: bool
    bio: str
    date_joined: datetime
    lang: Optional[str]
    timezone: Optional[str]
    colorize_tags: bool
    accepted_terms: bool
    read_new_terms: bool
    verified_email: bool
    is_staff: bool

    last_login: Optional[datetime] = None
    token:  Optional[str]
    email_token:  Optional[str]
    new_email:  Optional[str]
    max_private_projects:  Optional[int]
    max_public_projects:  Optional[int]
    max_memberships_private_project:  Optional[int]
    max_memberships_public_projects:  Optional[int]


