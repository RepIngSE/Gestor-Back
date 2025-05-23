from pydantic import BaseModel
from typing import Optional
from datetime import date

#Crear un usuario.
class TaskCreate(BaseModel):
    NAME: str
    DESCRIPTION: str
    PRIORITY: int
    ID_USER: int
    ID_STATUS: int
    START_DATE: Optional[date]
    FINISH_DATE: Optional[date]
    AREA: int
    USER_IN_CHARGE: Optional[int]

#Se devuelve al leer un usuario.
class TaskOut(BaseModel):
    ID: int
    NAME: str
    DESCRIPTION: str
    PRIORITY: int
    ID_USER: int
    ID_STATUS: int
    START_DATE: Optional[date]
    FINISH_DATE: Optional[date]
    AREA: int
    USER_IN_CHARGE: Optional[int]

    #Pydantic sabe cómo convertir los modelos de SQLAlchemy en diccionarios.
    class Config:
        from_attributes = True

# Actualizar usuario
class TaskUpdate(BaseModel):
    NAME: Optional[str] = None
    DESCRIPTION: Optional[str] = None
    PRIORITY: Optional[int] = None 
    ID_USER: Optional[int] = None
    ID_STATUS: Optional[int] = None
    START_DATE: Optional[date] = None
    FINISH_DATE: Optional[date] = None
    AREA: Optional[int] = None
    USER_IN_CHARGE: Optional[int] = None