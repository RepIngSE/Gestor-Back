from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from Schemas.auth_schema import LoginRequest, TokenResponse
from Services.auth_service import login_user

router = APIRouter()

@router.post("/", response_model=TokenResponse)
def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    return login_user(db, login_data)
