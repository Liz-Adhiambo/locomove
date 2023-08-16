from uuid import uuid4
from typing import Annotated
from pydantic import BaseModel, Field, UUID4
from locomove.schemas.vehicle import Vehicle
from locomove.schemas.user import User

class Driver(BaseModel):
    id: Annotated[str, UUID4] = Field(default_factory=uuid4)
    user: User
    vehicle: Vehicle

    class Config:
        orm_mode = True
