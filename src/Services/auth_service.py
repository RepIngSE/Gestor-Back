from sqlalchemy.orm import Session
from Models.user_model import User
from Schemas.auth_schema import LoginRequest, TokenResponse
from Auth.auth_utils import verify_password, create_access_token
from fastapi import HTTPException, status

def login_user(db: Session, login_data: LoginRequest) -> TokenResponse:
    user = db.query(User).filter(User.EMAIL == login_data.EMAIL).first()

    if not user or not verify_password(login_data.PASSWORD, user.PASSWORD):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas"
        )

    token_data = {
        "sub": user.EMAIL,
        "role": user.ID_ROL,
        "document": user.DOCUMENT
    }

    access_token = create_access_token(data=token_data)
    return TokenResponse(access_token=access_token, token_type="bearer", role=user.ID_ROL, document=user.DOCUMENT)
