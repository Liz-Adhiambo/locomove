import uuid
from sqlalchemy import Column, Integer, String, ForeignKey, UUID
from sqlalchemy.orm import relationship

from locomove.db import Base


class Mover(Base):
    __tablename__ = 'movers'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey('users.id'),
        nullable=False
    )

    vehicles = relationship("Vehicle", back_populates="mover")

    rating = Column(Integer, nullable=False)
