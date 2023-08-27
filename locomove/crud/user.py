from typing import List, Optional
from locomove.models.user import User
from locomove.schemas.client import User as UserSchema
from locomove.db import get_db
from sqlalchemy import or_

def get_users() -> List[UserSchema]:
    db = next(get_db())
    users = db.query(User).all()
    return users

def get_user(id: str) -> Optional[UserSchema]:
    try:
        db = next(get_db())
        user = db.query(User).filter(User.id == id).first()
        if user:
            return user
    except Exception as e:
        print(e)
        return None

def get_user_by_username_or_email(username: str) -> Optional[UserSchema]:
    try:
        db = next(get_db())
        return (
        db.query(User)
        .filter(
            or_(
                User.email == username,
                User.username == username,
                )
        )
        .first()
    )
    except Exception as e:
        print(e)
        return None

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


