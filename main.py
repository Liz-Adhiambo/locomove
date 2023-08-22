from typing import List
from fastapi import FastAPI
from locomove.models import *
from locomove.crud.user import (
    get_users,
    get_user,
    create_user,
    update_user,
    delete_user
)
from locomove.schemas.user import User

app = FastAPI()



@app.get("/")
def hello():
    return {"message": "Hello World"}


@app.get(
        "/users",
         response_model=List[User],
         )
def users():
    return get_users()

@app.get(
        "/users/{id}",
        response_model=User,
        )
def get_all_users(id: str):
    return get_user(id)

@app.post(
        "/users",
        response_model=User,
        )
def get_one_user(user: User):
    return create_user(user)

@app.put(
        "/users/{id}",
        response_model=User,
        )
def create_new_user(id: str, user: User):
    return update_user(id, user)

@app.delete(
        "/users/{id}",
        response_model=dict
        )
def delet_a_user(id: str):
    return delete_user(id)

####movers crud

###drivers crud

###vehicles crud
