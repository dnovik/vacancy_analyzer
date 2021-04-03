from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel
from datetime import datetime
from typing import List



class Specialization(BaseModel):
    profarea_name: str


class Employer(BaseModel):
    id: str
    name: str


class Salary(BaseModel):
    currency: str = None
    __from__: int = None
    to: int = None
    gross: bool = None


class Skills(BaseModel):
    name: str


class Vacancy(BaseModel):
    id: str
    name: str
    published_at: datetime
    alternate_url: str
    key_skills: List[Skills]
    salary: Salary
    employer: Employer
    specializations: List[Specialization]


