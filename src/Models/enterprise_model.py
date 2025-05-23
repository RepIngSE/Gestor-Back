from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger
from database import Base

#Modelo que representa la tabla enterprise.
class Enterprise(Base):
    __tablename__ = "Enterprise"

    ID = Column(Integer, primary_key=True, index=True)
    NAME = Column(String, nullable=False)
    NIT = Column(BigInteger, nullable=False)
    EMAIL = Column(String, unique=True, nullable=False)
    PHONE = Column(String)
    ID_STATUS = Column(Integer, ForeignKey('Status.ID'))
    ID_TYPE = Column(Integer, ForeignKey('Enterprise_type.ID'))
    