from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordRequestForm
from locomove.crud.auth.auth import get_current_user

from locomove.schemas.user import UserCreate, UserLogin
from locomove.crud.auth.signup import create_user
from locomove.crud.auth.login import check_user

app = FastAPI()

@app.post("/users/", response_model=dict, status_code=201)
def signup(user: UserCreate):
    return create_user(user)

@app.post("/users/login", response_model=dict, status_code=200)
def login(user: OAuth2PasswordRequestForm = Depends()):
    user_ = UserLogin(username=user.username, password=user.password)
    return check_user(user_)



"""
An example of how to protect a route (check the request has a valid token)
By including _ = Depends(get_current_user) in the function parameters,
the get_current_user function will be called before the function is executed
and an HTTPException will be raised if the token is invalid
"""
@app.get("/protected", response_model=dict, status_code=200)
def protected(_ = Depends(get_current_user)):
    return {"message": "Hello World"}
