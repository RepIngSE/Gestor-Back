# auth/utils.py
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configuración básica
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#Funcion para verificar la contraseña encriptada
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

#Función para encriptar la contraseña
def get_password_hash(password):
    return pwd_context.hash(password)

#Create token 
def create_access_token(data: dict, expires_delta: timedelta = None):
    #Create a copy to work with the dates
    to_encode = data.copy()
    #calculates token expiration date and time from current UTC time
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    # Adds the key “exp” (expiration) to the dictionary to be coded
    to_encode.update({"exp": expire})
    # Encrypts the token using the secret key and the defined algorithm (HS256)
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

