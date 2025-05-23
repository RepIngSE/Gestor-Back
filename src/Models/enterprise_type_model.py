from sqlalchemy import Column, Integer, String
from database import Base

#Modelo que representa la tabla enterprise type.
class Enterprise_type(Base):
    __tablename__ = "Enterprise_type"

    ID = Column(Integer, primary_key=True, index=True)
    NAME = Column(String, nullable=False)
    