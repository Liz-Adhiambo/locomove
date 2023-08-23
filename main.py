from typing import List
from fastapi import FastAPI

from locomove.schemas.user import User as UserSchema, UserResponse, UserLogin
from locomove.crud.auth.signup import create_user
from locomove.crud.auth.login import check_user

app = FastAPI()

@app.post("/users/", response_model=dict, status_code=201)
def signup(user: UserSchema):
    return create_user(user)

@app.post("/users/login", response_model=dict, status_code=200)
def login(user: UserLogin):
    return check_user(user)


