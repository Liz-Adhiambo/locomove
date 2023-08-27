from uuid import uuid4
from typing import Optional
from typing_extensions import Annotated
from pydantic import BaseModel, Field, UUID4

class Mover(BaseModel):
    id: Annotated[str, UUID4] = Field(default_factory=uuid4)
    user_id: Annotated[str, UUID4]
    rating: int
