from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Schemas.document_type_schema import DocumentTypeCreate, DocumentTypeView
from database import get_db
from Services.document_type_service import create_Document_type, get_all_Documents
from typing import List

router = APIRouter()

@router.post("/create", response_model=DocumentTypeView)
def createDocument(document: DocumentTypeCreate, db: Session = Depends(get_db)):
    return create_Document_type(db, document)

@router.get("/view", response_model=List[DocumentTypeView])
def list_documents(db: Session = Depends(get_db)):
    return get_all_Documents(db)
