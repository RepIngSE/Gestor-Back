from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from .auth_utils import SECRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        role = payload.get("role")
        document = payload.get("document")

        if email is None or role is None or document is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        return {"document": document, "role": role, "email": email}
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")
