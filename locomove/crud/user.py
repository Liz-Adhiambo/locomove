from typing import List
from locomove.models.user import User
from locomove.schemas.client import User as UserSchema
from locomove.db import get_db

def get_users() -> List[UserSchema]:
    db = next(get_db())
    users = db.query(User).all()
    return users

def get_user(id: str) -> UserSchema:
    db = next(get_db())
    user = db.query(User).filter(User.id == id).first()
    return user

def create_user(user: UserSchema) -> UserSchema:
    db = next(get_db())
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(id: str, user: UserSchema) -> UserSchema:
    db = next(get_db())
    db_user = db.query(User).filter(User.id == id).first()
    for field, value in user:
        setattr(db_user, field, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(id: str) -> dict:
    db = next(get_db())
    db_user = db.query(User).filter(User.id == id).first()
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully."}


