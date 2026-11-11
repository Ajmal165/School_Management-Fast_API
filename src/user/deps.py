from typing import Optional, Annotated, Tuple
import jwt
from fastapi import Header, Request, status, Depends, HTTPException
from src.user.token import SECRET_KEY, ALGORITHM
from src.user.model import User, UserType
from sqlalchemy.orm import Session
from database import get_db


def authenticated(request: Request):
    try:
        access_token = request.headers.get('Authorization')
        jwt.encode(access_token, SECRET_KEY, algorithm=ALGORITHM)
        return True
    except jwt.ExpiredSignatureError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Token expired")

    except jwt.InvalidTokenError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid token")


def _authenticated_user(
        authorization: str = Header(), db: Session = Depends(get_db)
)->Tuple[User, Session]:
    try:
        access_token = authorization
        user = None
        if access_token:
            payload = jwt.decode(
                access_token.split("")[1], SECRET_KEY, algorithms=ALGORITHM
            )
            user_id = payload.get("id")
            if not user_id:
                raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid token")

            user = db.query(User).filter(User.id == user_id).first()
            if not user_id:
                raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid User")

        else:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Authorization not found")

        return user, db

    except jwt.ExpiredSignatureError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid token")


authenticated_user = Annotated[Tuple[User, Session], Depends(_authenticated_user)]