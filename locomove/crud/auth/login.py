
from locomove.models.user import User
from locomove.schemas.user import User as UserSchema, UserResponse
from locomove.db import get_db
from locomove.crud.auth.helpers import (
    EXPIRES_IN,
    check_is_valid_email,
    check_is_valid_phone,
    check_is_valid_username,
    create_access_token,
    create_refresh_token,
    get_password_hash,
    verify_password,
)
from fastapi import HTTPException




def check_user(user: UserSchema) -> dict:
    db = next(get_db())
    
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user is None or not verify_password(user.password, db_user.password):
        raise Exception("Invalid credentials")

    access_token = create_access_token(str(db_user.id))
    refresh_token = create_refresh_token(str(db_user.id))

    return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "exp": EXPIRES_IN,
                }
        

