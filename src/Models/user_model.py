from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

#Modelo que representa la tabla users.
class User(Base):
    __tablename__ = "Users"

    ID = Column(Integer, primary_key=True, index=True)
    NAME = Column(String, nullable=False)
    LAST_NAME = Column(String)
    DOCUMENT = Column(String, unique=True, nullable=False)
    EMAIL = Column(String, unique=True, nullable=False)
    PHONE = Column(String)
    PASSWORD = Column(String, nullable=False)
    ID_COMPANY = Column(Integer, ForeignKey('Enterprise.ID'))
    ID_STATUS = Column(Integer, ForeignKey('Status.ID'))
    ID_TYPE_DOCUMENT = Column(Integer, ForeignKey('Document_type.ID'))
    ID_ROL = Column(Integer, ForeignKey('Roles.ID'))
    ID_AREA = Column(Integer, ForeignKey('Area.ID'))
