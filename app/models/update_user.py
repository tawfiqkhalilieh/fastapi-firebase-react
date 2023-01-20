from pydantic import BaseModel,validator
from typing import Optional
from fastapi.exceptions import HTTPException
import re

class User(BaseModel):
    username: Optional[str]
    email: Optional[str]
    password: Optional[str]
    age: Optional[int]
    gender: Optional[str]
    birthday: Optional[str]

    @validator('username')
    def validate_username(cls, v):
        if ' ' in v or not v:
            raise HTTPException(status_code=422)
        return v
    
    @validator('email')
    def validate_email(cls, v):
        if len(v) < 7 or not re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", v):
            raise HTTPException(status_code=422)
        return v

    @validator("age")
    def validate_age(cls, v):
        if v <= 0:
            raise HTTPException(status_code=422)
        return v

    @validator("password")
    def validate_password(cls, v):
        if " " in v and len(v) < 5:
            raise HTTPException(status_code=422)
        return v

    @validator("birthday")
    def validate_birthday(cls, v):
        if not re.match("^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[012])/((19|20)\\d\\d)$", v):
            raise HTTPException(status_code=422)
        return v
    
    @validator("gender")
    def validate_gender(cls, v):
        if v not in ("male" , "female" , "prefer_not_to_say"):
            raise HTTPException(status_code=422)
        return v