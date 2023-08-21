from uuid import uuid4
from typing import Annotated, Optional
from pydantic import BaseModel, Field, UUID4

class Mover(BaseModel):
    id: Annotated[str, UUID4] = Field(default_factory=uuid4)
    user_id: Annotated[str, UUID4]
    rating: int
