from sqlalchemy import Column, Integer, String
from database import Base

#Modelo que representa la tabla rols.
class Roles(Base):
    __tablename__ = "Roles"

    ID = Column(Integer, primary_key=True, index=True)
    ROL = Column(String, nullable=False)
    