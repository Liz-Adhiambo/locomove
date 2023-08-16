from uuid import uuid4
from typing import Annotated
from pydantic import BaseModel, Field, UUID4

from locomove.schemas.user import User


class Client(BaseModel):
    id: Annotated[str, UUID4] = Field(default_factory=uuid4)
    user_id: Annotated[str, UUID4]

    class Config:
        orm_mode = True
