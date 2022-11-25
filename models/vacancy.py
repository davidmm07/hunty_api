from typing import Optional
from pydantic import BaseModel
from models.skill import Skill


class Vacancy(BaseModel):
    PositionName: str
    CompanyName: str
    Salary: int
    Currency: str
    VacancyLink: str
    RequiredSkills: list[Skill]

class UpdateVacancy(BaseModel):
    PositionName: Optional[str]
    CompanyName: Optional[str]
    Salary: Optional[int]
    Currency: Optional[str]
    VacancyLink: Optional[str]
    RequiredSkills: Optional[list[Skill]]

class VacancyResponse(Vacancy):
    VacancyId: str