from sqlalchemy import Column, Integer, String, ForeignKey

from locomove.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(
        String(50),
        Unique=True,
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