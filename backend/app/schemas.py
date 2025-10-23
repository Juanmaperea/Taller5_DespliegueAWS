from pydantic import BaseModel
from typing import Optional

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    age: Optional[int] = None
    favorite_color: Optional[str] = None

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    age: Optional[int]
    favorite_color: Optional[str]

class StudentOut(StudentBase):
    id: int
    class Config:
        orm_mode = True
