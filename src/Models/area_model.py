from sqlalchemy import Column, Integer, String
from database import Base

#Modelo que representa la tabla Area.
class Area(Base):
    __tablename__ = "Area"

    ID = Column(Integer, primary_key=True, index=True)
    Name = Column(String, nullable=False)
    