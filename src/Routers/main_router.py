from fastapi import APIRouter
from Routers.UserRouter import user_router
from Routers import document_type_router
from Routers.LoginRouter import login_router
from Routers.TaskRouter import task_router


main_router = APIRouter() 

#Function to include the routes and have them grouped together.
def incluide_in_app(app):
    app.include_router(user_router.router, prefix = "/api/user")
    app.include_router(login_router.router, prefix = "/api/login")
    app.include_router(task_router.router, prefix = "/api/task")
    app.include_router(document_type_router.router, prefix = "/api/document")