import re

from fastapi import HTTPException
from locomove.models.user import User
from locomove.db import get_db
from jose import jwt
from datetime import datetime, timedelta
from typing import Optional, Union, Any

from passlib.context import CryptContext

from locomove.settings import (
    JWT_SECRET_KEY,
    JWT_REFRESH_SECRET_KEY,
    ALGORITHM,
    EXPIRES_IN,
    REFRESH_TOKEN_EXPIRE_MINUTES
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def check_is_valid_email(email: str) -> bool:
    if not email:
        return True
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(email_regex, email):
        #check is email already exists
        db = next(get_db())
        user = db.query(User).filter(User.email == email).first()
        if user:
            raise HTTPException(status_code=400, detail="A user with that email already exists")
        return True
    else:
        raise HTTPException(status_code=400, detail="The email is invalid")


def check_is_valid_phone(phone: str) -> bool:
    #phone is 0112111111
    phone_regex = r"^(?:254|\+254|0)?(7(?:(?:[129][0–9])|(?:0[0–8])|(4[0–1]))[0–9]{6})$"
    if re.match(phone_regex, phone):
        #check is phone already exists
        db = next(get_db())
        user = db.query(User).filter(User.phone == phone).first()
        if user:
            raise HTTPException(status_code=400, detail="A user with that phone number already exists")
        return True
    else:
        raise HTTPException(status_code=400, detail="The phone number is invalid")

def check_is_valid_username(username: str) -> bool:
    # 6 characters long and starts with letter or underscore
    username_regex = r"^[a-zA-Z_][a-zA-Z0-9_]{5,}$"
    if re.match(username_regex, username):
        #check is username already exists
        db = next(get_db())
        user = db.query(User).filter(User.username == username).first()
        if user:
            raise HTTPException(status_code=400, detail="A user with that username already exists")
        return True
    else:
        raise HTTPException(status_code=400, detail="Username must be 6 characters long and starts with letter or underscore")



def create_access_token(subject: Union[str, Any], expires_delta: Optional[int] = None) -> str:
    if expires_delta:
        expires_delta_ = datetime.utcnow() + timedelta(seconds=expires_delta)
    else:
        expires_delta_ = datetime.utcnow() + timedelta(seconds=int(EXPIRES_IN))

    to_encode = {"exp": expires_delta_, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt


def create_refresh_token(subject: Union[str, Any], expires_delta: Optional[int] = None) -> str:
    if expires_delta is not None:
        expires_delta_ = datetime.utcnow() + timedelta(minutes=expires_delta)
    else:
        expires_delta_ = datetime.utcnow() + timedelta(minutes=int(REFRESH_TOKEN_EXPIRE_MINUTES))

    to_encode = {"exp": expires_delta_, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt
