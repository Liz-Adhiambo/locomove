import uuid
from sqlalchemy import Column, String, ForeignKey, UUID, Integer
from sqlalchemy.orm import relationship

from locomove.db import Base


class Vehicle(Base):
    __tablename__ = 'vehicles'

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    mover_id = Column(Integer, ForeignKey('movers.id'))
    mover = relationship(
        'Mover',
        back_populates='vehicles'
    )

    driver = relationship(
        'Driver',
        back_populates='vehicles'
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
