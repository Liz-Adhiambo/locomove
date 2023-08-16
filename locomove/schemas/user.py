from typing import Optional
from uuid import uuid4
from typing import Annotated
from pydantic import UUID4, BaseModel, Field

from locomove.enums import Role


class User(BaseModel):
    id: Annotated[UUID4, str] = Field(default_factory=uuid4)
    username: str
    password: str
    phone: str
    email: Optional[str] = None
    role: Annotated[Role, str] = Field(default=Role.CLIENT)

