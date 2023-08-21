from uuid import uuid4
from typing import Annotated, Optional
from pydantic import BaseModel, Field, UUID4

class Driver(BaseModel):
    id: Annotated[str, UUID4] = Field(default_factory=uuid4)
    user_id: Annotated[str, UUID4]
    vehicle_id: Optional[Annotated[str, UUID4]] = None

    class Config:
        orm_mode = True
