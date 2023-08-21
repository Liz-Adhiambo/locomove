from typing import List
from fastapi import FastAPI

from locomove.schemas.user import User as UserSchema, UserResponse
from locomove.crud.auth.signup import create_user

app = FastAPI()

@app.post("/users/", response_model=dict, status_code=201)
def signup(user: UserSchema):
    return create_user(user)
