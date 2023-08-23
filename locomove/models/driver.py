import uuid

from sqlalchemy import Column, Integer, String, ForeignKey, UUID
from locomove.db import Base


class Driver(Base):
    __tablename__ = 'drivers'

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

    vehicle_id = Column(
        UUID(as_uuid=True),
        ForeignKey('vehicles.id'),
        nullable=True
    )

    rating = Column(Integer, nullable=False, default=0)
