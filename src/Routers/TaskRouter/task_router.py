from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Schemas.task_schema import TaskCreate, TaskOut, TaskUpdate
from database import get_db
from Services.task_service import create_task, get_all_task, update_task, delete_task, get_task, get_tasks_by_user, get_task_status_summary_by_document, get_tasks_by_area, get_task_status_summary_by_Area
from typing import List
from Auth.token_dependencies import get_current_user

router = APIRouter()

#Crear tarea
@router.post("/create", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def createTask(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task)

#Ver todos las tareas 
@router.get("/view", response_model=List[TaskOut])
def list_task(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    # Validar si el usuario tiene rol 1
    if str(current_user["role"]) != "1":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos para ver esta información"
        )
    return get_all_task(db)

# Obtener tarea por ID
@router.get("/view/{task_id}", response_model=TaskOut)
def view_task(task_id: str, db: Session = Depends(get_db)):
    task = get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrado")
    return task

# Obtener las tareas por usuario
@router.get("/user/{user_id}", response_model=list[TaskOut])
def read_tasks_by_user(user_id: str, db: Session = Depends(get_db)):
    tasks = get_tasks_by_user(db, user_id)
    if not tasks:
        raise HTTPException(status_code=404, detail="No se encontraron tareas para este usuario")
    return tasks 

#Obtener todas las tareas de un usurio con contador
@router.get("/user/{user_id}/status-summary")
def task_status_summary(user_id: str, db: Session = Depends(get_db)):
    tasks = get_task_status_summary_by_document(db, user_id)
    if not tasks:
        raise HTTPException(status_code=404, detail="No se encontraron Sumarotirias de tareas para este usuario")
    return tasks 

#Obtener todas las tareas por area
@router.get("/user/{document}/area-tasks", response_model=list[TaskOut])
def read_tasks_by_user_area(document: str, db: Session = Depends(get_db)):
    task = get_tasks_by_area(db, document)
    if not task:
        raise HTTPException(status_code=404, detail="No se encontraron tareas para este usuario")
    return task

#Obtener todas las tareas por area con contador
@router.get("/user/{user_id}/area-tasks/status-summary")
def task_status_summary(user_id: str, db: Session = Depends(get_db)):
    tasks = get_task_status_summary_by_Area(db, user_id)
    if not tasks:
        raise HTTPException(status_code=404, detail="No se encontraron Sumarotirias de tareas para este usuario")
    return tasks 

# Actualizar tarea 
@router.put("/update/{task_id}", response_model=TaskOut)
def updateTask(task_id: str, task_update: TaskUpdate, db: Session = Depends(get_db)):
    task = update_task(db, task_id, task_update)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task

# Eliminar tarea
@router.delete("/delete/{task_id}", response_model=TaskOut)
def deleteTask(task_id: str, db: Session = Depends(get_db)):
    task = delete_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task