from sqlalchemy import Column, Integer, String, ForeignKey, Date
from database import Base

#Modelo que representa la tabla task.
class Task(Base):
    __tablename__ = "Task"

    ID = Column(Integer, primary_key=True, index=True)
    START_DATE = Column(Date, nullable=False)
    FINISH_DATE = Column(Date, nullable=False)
    PRIORITY = Column(Integer, unique=True, nullable=False)
    NAME = Column(String, nullable=False)
    DESCRIPTION = Column(String, nullable=False)
    USER_IN_CHARGE = Column(Integer)
    AREA = Column(Integer, ForeignKey('Area.ID'))
    ID_USER = Column(Integer, ForeignKey('Users.ID'))
    ID_STATUS = Column(Integer, ForeignKey('Status.ID'))
    