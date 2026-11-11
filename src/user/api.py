from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from src.user import model, schemas
from src.user.helper.password import hash_password, verify_password
from src.user.token import create_access_token, create_refresh_token


Router = APIRouter(prefix="/user", tags=["User"])


@Router.post("/register")
def create_user(
    request: schemas.User,
    db: Session = Depends(get_db),
):
    existing_mail = (
        db.query(model.User)
        .filter(model.User.email == request.email)
        .first()
    )
    if existing_mail:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered",
        )

    existing_username = (
        db.query(model.User)
        .filter(model.User.username == request.username)
        .first()
    )
    if existing_username:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username already registered",
        )

    user = model.User(
        firstname=request.firstname,
        lastname=request.lastname,
        email=request.email,
        username=request.username,
        password=hash_password(request.password),
        birthdate=request.birthdate,
        user_type=request.user_type.value,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {"email": user.email, "User": user.username}


@Router.post("/login")
def verify_user(
    request: schemas.Login,
    db: Session = Depends(get_db),
):
    user = db.query(model.User).filter(
        model.User.email == request.email
    ).first()

    if not user or not verify_password(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )

    token_data = {
        "sub": user.username,
        "email": user.email,
        "username": user.username,
        "user_type": user.user_type,
    }

    return {
        "name": f"{user.firstname} {user.lastname}",
        "email": user.email,
        "access_token": create_access_token(token_data),
        "refresh_token": create_refresh_token(token_data),
        "token_type": "Bearer",
    }


@Router.post("/show/{id}", response_model=schemas.ShowUser)
def show_user(
    id: int,
    db: Session = Depends(get_db),
):
    user = db.query(model.User).filter(model.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This user is not exists",
        )

    return user
