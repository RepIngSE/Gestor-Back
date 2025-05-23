from sqlalchemy.orm import Session
from Models.document_type_model import Document_type
from Schemas.document_type_schema import DocumentTypeCreate 

#Función para crear un tipo de documento
def create_Document_type(db: Session, document_data: DocumentTypeCreate):
    document = Document_type(NAME=document_data.NAME, ABR = document_data.ABR)
    db.add(document)
    db.commit()
    db.refresh(document)
    return document

def get_all_Documents(db: Session):
    return db.query(Document_type).all()