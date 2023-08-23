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

def create_user(user: UserSchema) -> dict:
    db = next(get_db())
    try:
        # check is valid email
        check_is_valid_email(user.email)

        #check_is_valid_phone(user.phone)

        check_is_valid_username(user.username)

        password_hash = get_password_hash(user.password)
        print(password_hash)

        #remove password from user object
        del user.password

        db_user = User(**user.dict(), password=password_hash)
        print(db_user.password,'user password')

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        del db_user.password

        access_token = create_access_token(str(db_user.id))
        refresh_token = create_refresh_token(str(db_user.id))

        return {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "exp": EXPIRES_IN,
                }

    except Exception as e:
        raise e





