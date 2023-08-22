from uuid import uuid4
from typing import Annotated
from pydantic import BaseModel, Field, UUID4

#from locomove.schemas.owner import Owner
from locomove.schemas.driver import Driver


class Vehicle(BaseModel):
    id: Annotated[str, UUID4] = Field(default_factory=uuid4)
    # owner: Owner
    driver: Driver
    model: str
    plate: str
    description: str
    location: str

    class Config:
        orm_mode = True

