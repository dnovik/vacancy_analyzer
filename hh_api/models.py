from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class Vacancy(BaseModel):
    country: str
    city: str
    created: datetime
    published: datetime
    employer: str
    position: str
    salary_min: int
    salary_max: int
    gross: bool
    currency: str
    prof_areas: Optional[List]
    required_skills: Optional[List]
