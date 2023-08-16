import uuid
from sqlalchemy import Column, String, ForeignKey, UUID
from locomove.db import Base

class Vehicle(Base):
    __tablename__ = 'vehicles'

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    owner_id = Column(
        UUID(as_uuid=True),
        ForeignKey('movers.id'),
        nullable=False
    )

    driver_id = Column(
        UUID(as_uuid=True),
        ForeignKey('drivers.id'),
        nullable=False
    )

    model = Column(
        String(50),
        nullable=False
    )

    plate = Column(
        String(50),
        nullable=False
    )

    description = Column(
        String(50),
        nullable=False
    )

    location = Column(
        String(50),
        nullable=False
    )

