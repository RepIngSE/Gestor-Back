from pydantic import BaseModel

#El cliente envía al crear tipo de documento
class DocumentTypeCreate(BaseModel):
    NAME: str
    ABR: str
    
class DocumentTypeView(BaseModel):
    ID: int
    NAME: str
    ABR: str