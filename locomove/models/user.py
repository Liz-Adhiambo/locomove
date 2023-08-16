import uuid
from sqlalchemy import Column, String, UUID

from locomove.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(
        String(50),
        unique=True,
        nullable=False
    )

    password = Column(
        String(50),
        nullable=False
    )

    phone = Column(
        String(50),
        nullable=False
    )

    email = Column(
        String(50),
        nullable=True
    )

    role = Column(
        String(50),
        nullable=False
    )



