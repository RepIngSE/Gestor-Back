from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from Models.user_model import User
from Models.roles_model import Roles
from Models.area_model import Area
from Schemas.user_schema import UserCreate, UserUpdate
from Observers.observer import event_manager
from Auth.auth_utils import get_password_hash

#Función para crear un usuario
def create_user(db: Session, user_data: UserCreate):
        existing_user = db.query(User).filter(User.DOCUMENT == user_data.DOCUMENT).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El número de cédula ya está registrado"
            )
        
        # Validar si ya existe el email
        existing_user_by_email = db.query(User).filter(User.EMAIL == user_data.EMAIL).first()
        if existing_user_by_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El email ya está registrado"
            )
        
        # Hashear la contraseña antes de guardarla
        user_dict = user_data.model_dump()
        user_dict["PASSWORD"] = get_password_hash(user_dict["PASSWORD"])

        # Crear el usuario con la contraseña ya encriptada
        db_user = User(**user_dict)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        event_manager.notify("user_created", {"email": db_user.EMAIL, "name": db_user.NAME, "CC": db_user.DOCUMENT})
        return db_user

#Función para ver todos los ususrios
def get_all_users(db: Session):
    return db.query(User).all()

#Función para ver un solo usuario
def get_user(db: Session, user_id: str):
    user = db.query(User).filter(User.DOCUMENT == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    print(user.ID_AREA)
    role = db.query(Roles).filter(Roles.ID == user.ID_ROL).first()
    area = db.query(Area).filter(Area.ID == user.ID_AREA).first()
     
    print(area)
    return {
        "ID": user.ID,
        "DOCUMENT": user.DOCUMENT,
        "NAME": user.NAME,
        "LAST_NAME": user.LAST_NAME,
        "EMAIL": user.EMAIL,
        "PHONE": user.PHONE,
        "AREA": area.Name,  # relación con Area
        "ROL": role.ROL   # relación con Role
    }

#Función de actualizar un usuario
def update_user(db: Session, user_id: str, user_data: UserUpdate):
    user = db.query(User).filter(User.DOCUMENT == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuario con cédula {user_id} no encontrado"
        )
    
    update_fields = user_data.model_dump(exclude_unset=True)

    # Si el usuario está actualizando la contraseña, la encriptamos antes de guardar
    if "PASSWORD" in update_fields:
        update_fields["PASSWORD"] = get_password_hash(update_fields["PASSWORD"])

    for key, value in update_fields.items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    event_manager.notify("user_updated", {"email": user.EMAIL, "name": user.NAME, "CC": user.DOCUMENT})
    return user

#Función de eliminar un usuario
def delete_user(db: Session, user_id: str):
    user = db.query(User).filter(User.DOCUMENT== user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuario con cédula {user_id} no encontrado"
        )
    
    db.delete(user)
    db.commit()
    event_manager.notify("user_deleted", {"email": user.EMAIL, "name": user.NAME, "CC": user.DOCUMENT})
    return user

#Devolver nombres dependiendo del area con el rol 4 
def get_users_by_area_and_role(db: Session, document: str):
    user = db.query(User).filter(User.DOCUMENT == document).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    area = user.ID_AREA

    users = db.query(User).filter(User.ID_AREA == area, User.ID_ROL == 4).all()
    print(users)
    full_names = [f"{u.NAME} {u.LAST_NAME}" for u in users]

    return full_names