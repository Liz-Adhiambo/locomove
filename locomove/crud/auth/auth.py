from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from jose import jwt, exceptions

from locomove.crud.user import get_user
from locomove.settings import JWT_SECRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, ALGORITHM)
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        user = get_user(user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except exceptions.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Signature has expired")
    except exceptions.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail="Could not validate credentials")
