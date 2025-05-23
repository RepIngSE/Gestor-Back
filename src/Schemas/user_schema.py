from pydantic import BaseModel, EmailStr
from typing import Optional

#Crear un usuario.
class UserCreate(BaseModel):
    NAME: str
    LAST_NAME: str
    DOCUMENT: str
    EMAIL: EmailStr
    PHONE: str 
    PASSWORD: str
    ID_COMPANY: int
    ID_STATUS: int
    ID_TYPE_DOCUMENT: int
    ID_ROL: int
    ID_AREA: int

#Se devuelve al leer un usuario.
class UserOut(BaseModel):
    ID: int
    NAME: str
    EMAIL: EmailStr
    LAST_NAME: str
    DOCUMENT: str
    PHONE: str 
    PASSWORD: str
    ID_COMPANY: int
    ID_STATUS: int
    ID_TYPE_DOCUMENT: int
    ID_ROL: int
    ID_AREA: int

    #Pydantic sabe cómo convertir los modelos de SQLAlchemy en diccionarios.
    class Config:
        from_attributes = True

# Actualizar usuario
class UserUpdate(BaseModel):
    NAME: Optional[str] = None
    EMAIL: Optional[EmailStr] = None
    LAST_NAME: Optional[str] = None
    PHONE: Optional[str] = None 
    PASSWORD: Optional[str] = None
    ID_COMPANY: Optional[int] = None
    ID_STATUS: Optional[int] = None
    ID_TYPE_DOCUMENT: Optional[int] = None
    ID_ROL: Optional[int] = None
    ID_AREA: Optional[int] = None


class UserInfo(BaseModel):
    ID: int
    DOCUMENT: str
    NAME: str
    LAST_NAME: str
    EMAIL: EmailStr
    PHONE: str
    AREA: str
    ROL: str

    class Config:
        from_attributes = True
