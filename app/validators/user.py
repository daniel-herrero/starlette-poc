import json
from uuid import uuid4
from pydantic import BaseModel
from pydantic.class_validators import validator
from pydantic.schema import datetime, Optional

from app.api.common_responses import error_response


class UserCreateBaseVal(BaseModel):
    """
    Mandatory and explicit input parameters
    """
    password: str
    password2: str
    username: str
    full_name: str
    email: str

    @validator('username')
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'must be alphanumeric'
        return v

    @validator('full_name')
    def name_must_contain_space(cls, v):
        if ' ' not in v:
            raise ValueError('must contain a space')
        return v.title()

    @validator('password')
    def passwords_length(cls, v):
        if len(v) <= 6:
            raise ValueError('Passwords must have 6 chars')
        return v

    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('passwords do not match')
        return v


class UserCreateMandatoryVal(UserCreateBaseVal):
    """
    Optional input parameters with default values (mandatory in db)
    """
    is_superuser: bool = False
    is_active: bool = True
    color: str = "#FFFFFF"
    bio: str = ""
    date_joined: datetime = datetime.now()
    colorize_tags: bool = True
    is_system: bool = False
    uuid: str = uuid4().hex
    accepted_terms: bool = True
    read_new_terms: bool = True
    verified_email: bool = True
    is_staff: bool = False


class UserCreateVal(UserCreateMandatoryVal):
    """
    Optional input parameters (not mandatory in db)
    """
    theme: Optional[str]
    photo: Optional[str]


# Properties to receive on task update
class UserUpdateVal(BaseModel):
    password: Optional[str]
