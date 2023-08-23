from uuid import uuid4
from typing_extensions import Annotated
from pydantic import BaseModel, Field, UUID4


class Vehicle(BaseModel):
    id: Annotated[str, UUID4] = Field(default_factory=uuid4)
    owner_id: Annotated[str, UUID4]
    driver_id: Annotated[str, UUID4]
    model: str
    plate: str
    description: str
    location: str

    class Config:
        orm_mode = True

