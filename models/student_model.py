from pydantic import BaseModel, Field , validator
from datetime import datetime
from typing import Optional

class SocialsModel(BaseModel):
    instagram: Optional[str] = Field(None, max_length=100)
    linkedin: str = Field(None, max_length=100)
    github: str = Field(None, max_length=100)
    website: Optional[str] = Field(None, max_length=100)

class CodingModel(BaseModel):
    Leetcode: Optional[str] = Field(None, max_length=100)
    Hackerrank: Optional[str] = Field(None, max_length=100)
    Codechef: Optional[str] = Field(None, max_length=100)
    Codeforces: Optional[str] = Field(None, max_length=100)
    GFG: Optional[str] = Field(None, max_length=100)


class StudentModel(BaseModel):
    id: int = Field(None, alias='student_id')
    first_name: str = Field(None, max_length=20)
    last_name: str = Field(None, max_length=20)
    email: str = Field(None, max_length=100)
    @validator('email')
    def email_validator(cls, v):
        if '@student.nitw.ac.in' not in v:
            raise ValueError('Invalid email')
        return v
    personal_email: str = Field(None, max_length=100)
    @validator('personal_email')
    def personal_email_validator(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email')
        return v
    password: str = Field(None, min_length=6, max_length=20)
    socials: SocialsModel = Field(None)
    coding: CodingModel = Field(None)
    date_of_birth: datetime = Field(None)
    year: int = Field(None)
    created_at: datetime = Field(None)
    updated_at: datetime = Field(None)


class StudentModelSignIn(BaseModel):
    email: str = Field(None, max_length=100) 
    password: str = Field(None, min_length=6, max_length=20)
    class config:
        orm_mode = True

class StudentModelSignUp(BaseModel):
    first_name: str = Field(None, max_length=20)
    last_name: str = Field(None, max_length=20)
    email: str = Field(None, max_length=100)
    @validator('email')
    def email_validator(cls, v):
        if '@student.nitw.ac.in' not in v:
            raise ValueError('Invalid email')
        return v
    password: str = Field(None, min_length=6, max_length=20)
    year: int = Field(None)
    class config:
        orm_mode = True

class StudentModelUpdate(BaseModel):
    first_name: Optional[str] = Field(None, max_length=20)
    last_name: Optional[str] = Field(None, max_length=20)
    email: Optional[str] = Field(None, max_length=100)
    @validator('email')
    def email_validator(cls, v):
        if '@student.nitw.ac.in' not in v:
            raise ValueError('Invalid email')
        return v
    personal_email: Optional[str] = Field(None, max_length=100)
    @validator('personal_email')
    def personal_email_validator(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email')
        return v
    password: Optional[str] = Field(None, min_length=6, max_length=20)
    socials: Optional[SocialsModel] = Field(None)
    coding: Optional[CodingModel] = Field(None)
    date_of_birth: Optional[datetime] = Field(None)
    year: Optional[int] = Field(None)
    class config:
        orm_mode = True

class StudentModelUpdatePassword(BaseModel):
    password: str = Field(None, min_length=6, max_length=20)
    class config:
        orm_mode = True

class StudentModelUpdateSocials(BaseModel):
    socials: SocialsModel = Field(None)
    class config:
        orm_mode = True

class StudentModelUpdateCoding(BaseModel):
    coding: CodingModel = Field(None)
    class config:
        orm_mode = True






    


    


