from sqlalchemy import Column, Integer, String
from database import Base

#Modelo que representa la tabla document type.
class Document_type(Base):
    __tablename__ = "Document_type"

    ID = Column(Integer, primary_key=True, index=True)
    NAME = Column(String, nullable=False)
    ABR = Column(String)
    