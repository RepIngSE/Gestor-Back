from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Schemas.user_schema import UserCreate, UserOut, UserUpdate, UserInfo
from database import get_db
from Services.user_service import create_user, get_all_users, update_user, delete_user, get_user, get_users_by_area_and_role
from typing import List
from Auth.token_dependencies import get_current_user

router = APIRouter()

#Crear usuario
@router.post("/create", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def createUser(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

#Ver todos los usuarios
@router.get("/view", response_model=List[UserOut])
def list_users(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    # Validar si el usuario tiene rol 1
    if str(current_user["role"]) != "1":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos para ver esta información"
        )
    return get_all_users(db)

# Obtener usuario por ID
@router.get("/view/{user_id}", response_model=UserInfo)
def view_user(user_id: str, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

# Actualizar usuario
@router.put("/update/{user_id}", response_model=UserOut)
def updateUser(user_id: str, user_update: UserUpdate, db: Session = Depends(get_db)):
    user = update_user(db, user_id, user_update)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

# Eliminar usuario
@router.delete("/delete/{user_id}", response_model=UserOut)
def deleteUser(user_id: str, db: Session = Depends(get_db)):
    user = delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

#Ruta para taraer a todos los roles 4 del area necesaria 
@router.get("/area-role4/{document}", response_model=list[str])
def get_users_names_by_area_and_role(document: str, db: Session = Depends(get_db)):
    user = get_users_by_area_and_role(db, document)
    if not user: 
        raise HTTPException(status_code=404, detail="Sin usuarios para este area")
    return user