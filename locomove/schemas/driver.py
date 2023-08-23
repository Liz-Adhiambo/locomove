from uuid import uuid4
from typing import Optional
from typing_extensions import Annotated
from pydantic import BaseModel, Field, UUID4

class Driver(BaseModel):
    id: Annotated[str, UUID4] = Field(default_factory=uuid4)
    user_id: Annotated[str, UUID4]
    vehicle_id: Optional[Annotated[str, UUID4]] = None

    class Config:
        orm_mode = True
