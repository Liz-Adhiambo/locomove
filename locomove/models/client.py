import uuid
from sqlalchemy import Column, ForeignKey, UUID
from locomove.db import Base


class Client(Base):
    __tablename__ = 'clients'

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey('users.id'),
        nullable=False
    )
