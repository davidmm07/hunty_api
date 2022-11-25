from typing import Optional
from pydantic import BaseModel
from models.skill import Skill


class User(BaseModel):
    FirstName: str
    LastName: str
    Email: str
    YearsPreviousExperience: int
    Skills: list[Skill]

class UpdateUser(BaseModel):
    FirstName: Optional[str]
    LastName: Optional[str]
    Email: Optional[str]
    YearsPreviousExperience: Optional[int]
    Skills: Optional[list[Skill]]

class UserResponse(User):
    UserId: str