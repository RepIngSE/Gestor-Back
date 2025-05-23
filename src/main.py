from fastapi import FastAPI
from Models import *
from Routers.main_router import incluide_in_app
from Observers.observer import event_manager
from Notifiers.email_notifier import EmailNotifier
from Notifiers.whatsApp_notifier import WhatsappNotifier
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

#Cors para autorizar el frontend
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],  
   # Encabezados permitidos
    allow_headers=["*"],
)

#Make routes visible, accessible and grouped.
incluide_in_app(app)

# Suscribir observadores
event_manager.subscribe(EmailNotifier())
event_manager.subscribe(WhatsappNotifier())