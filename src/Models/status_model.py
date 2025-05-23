from sqlalchemy import Column, Integer, String
from database import Base

#Modelo que representa la tabla status.
class Status(Base):
    __tablename__ = "Status"

    ID = Column(Integer, primary_key=True, index=True)
    DESCRIPTION = Column(String, nullable=False)
    
