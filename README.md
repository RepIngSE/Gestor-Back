#Back-end 

##Instalation

First install python from the main page with its path in the environment variable:  
```
https://www.python.org/
```

Install dependencies using: 

```
pip install fastapi[all]
pip install sqlalchemy asyncpg python-dotenv psycopg2-binary
pip install twilio
pip install python-jose[cryptography] passlib[bcrypt]
```

to execute the project: 
```
uvicorn main:app --reload
```

El manejo del proyecto es el siguiente: 
    -Se tiene una conexión a la db en el archivo database.py, allí esta singleton
    -El main tiene el manejo de los CORS y donde llama para que se inice el proyecto 
    -Folder Models:
        * Tiene todos los modelos de las tablas de la db, se realiza esto para que saber que datos estan en la db, seria un comparatibo. 
    -Folder Schemas: 
        *Se realiza los esquemas para realizar validacion de datos, que sean los que se aceptan en la DB 
    -Folder Routers:
        *Se realizan las apis como tal que es lo que se le va a pasar al front por la url
        *Main Router es para agruparlas, solo se debe incluir un breve prefijo y ya se unen
    -Folder Services: 
        *Aqui va la logica, de la DB a las APIS, se puede modificar todo lo que hace falta
    -Folder Auth: 
        *Estan los archivos para el login y toda la validación del token
    -Folder Notifiers: 
        *Si es necesario agregar otro metodo de notificacion colocarlo allí 
    -Folder Observer: 
        *Aquí tenemos el observer que se dispara cada que lo veamos necesario con la linea en el service