from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Crear la URL de conexión
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Patrón Singleton para la base de datos
class DB:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DB, cls).__new__(cls)
            try:
                # Crear motor y sesión
                cls._instance.engine = create_engine(DATABASE_URL)
                cls._instance.SessionLocal = sessionmaker(
                    autocommit=False,
                    autoflush=False,
                    bind=cls._instance.engine
                )
                print("✅ Conexión exitosa a PostgreSQL con SQLAlchemy.")
            except Exception as e:
                print(f"❌ Error al conectar con PostgreSQL: {e}")
                raise
        return cls._instance

# Base para los modelos
Base = declarative_base()

# Dependencia de FastAPI para obtener la sesión de base de datos
def get_db():
    db = DB().SessionLocal()
    try:
        yield db
    finally:
        db.close()
