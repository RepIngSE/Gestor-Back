from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from Models.task_model import Task
from Models.user_model import User
from Schemas.task_schema import TaskCreate, TaskUpdate
from Observers.observer import event_manager

#Función para crear una tarea 
def create_task(db: Session, task_data: TaskCreate):
        db_task = Task(**task_data.model_dump())
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        event_manager.notify("task_created", {"name": db_task.NAME, "description": db_task.DESCRIPTION, "user": db_task.ID_USER})
        return db_task

#Función para ver todas las tareas
def get_all_task(db: Session):
    return db.query(Task).all()

#Función para ver una sola tarea
def get_task(db: Session, task_id: str):
    return db.query(Task).filter(Task.ID == task_id).first()

#Ver todas las tareas de un usuario
def get_tasks_by_user(db: Session, document: str):
    user = db.query(User).filter(User.DOCUMENT == document).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    tasks = db.query(Task).filter(Task.ID_USER == user.ID).all()
    return tasks

#Tener un conteo de las tareas
def get_task_status_summary_by_document(db: Session, document: str):
    user = db.query(User).filter(User.DOCUMENT == document).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    tasks = db.query(Task).filter(Task.ID_USER == user.ID).all()

    summary = {}
    for task in tasks:
        status = task.ID_STATUS
        if status not in summary:
            summary[status] = {
                "ID_STATUS": status,
                "cantidad": 0,
                "tasks": []
            }
        summary[status]["cantidad"] += 1
        summary[status]["tasks"].append(task.ID)

    return list(summary.values())

#Ver todas las tareas de este admin
def get_tasks_by_area(db: Session, document: str):
    user = db.query(User).filter(User.DOCUMENT == document).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    area_id = user.ID_AREA
    tasks = db.query(Task).filter(Task.AREA == area_id).all()

    if not tasks:
        raise HTTPException(status_code=404, detail=f"No hay tareas para el área: {area_id}")

    return tasks

#Tener un conteo de las tareas del area
def get_task_status_summary_by_Area(db: Session, document: str):
    user = db.query(User).filter(User.DOCUMENT == document).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    tasks = db.query(Task).filter(Task.AREA == user.ID_AREA).all()

    summary = {}
    for task in tasks:
        status = task.ID_STATUS
        if status not in summary:
            summary[status] = {
                "ID_STATUS": status,
                "cantidad": 0,
                "tasks": []
            }
        summary[status]["cantidad"] += 1
        summary[status]["tasks"].append(task.ID)

    return list(summary.values())


#Función de actualizar la tarea
def update_task(db: Session, task_id: str, task_data: TaskUpdate):
    task = db.query(Task).filter(Task.ID == task_id).first()
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarea con id {task_id} no encontrada"
        )

    for key, value in task_data.model_dump(exclude_unset=True):
        setattr(task, key, value)

    db.commit()
    db.refresh(task)
    event_manager.notify("task_created", {"name": task.NAME, "description": task.DESCRIPTION, "user": task.ID_USER})
    return task

#Función de eliminar una tarea
def delete_task(db: Session, task_id: str):
    task = db.query(Task).filter(Task.DOCUMENT== task_id).first()
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuario con cédula {task_id} no encontrado"
        )
    
    db.delete(task)
    db.commit()
    event_manager.notify("task_created", {"name": task.NAME, "description": task.DESCRIPTION, "user": task.ID_USER})
    return task