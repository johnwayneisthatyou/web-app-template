# SQLModel Models

from typing import Optional
from sqlmodel import SQLModel, Field


class Job(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    company: str
    location: str
