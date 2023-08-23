import uuid
from sqlalchemy import Column, String, ForeignKey, UUID, Integer

from locomove.db import Base


class Vehicle(Base):
    __tablename__ = 'vehicles'

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    mover_id = Column(
            UUID(as_uuid=True),
            ForeignKey('movers.id'))

    driver_id = Column(
            UUID(as_uuid=True),
            ForeignKey('drivers.id'),
            nullable=False
    )

    model = Column(
        String(255),
        nullable=False
    )

    plate = Column(
        String(255),
        nullable=False
    )

    description = Column(
        String(255),
        nullable=False
    )

    location = Column(
        String(255),
        nullable=False
    )
