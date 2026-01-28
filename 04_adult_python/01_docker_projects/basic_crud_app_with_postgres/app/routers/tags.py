'''
Purpose: Define endpoints under /api/tags for tag operations.
API routes for tag CRUD operations.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import schemas
import crud
from database import get_db

router = APIRouter(
    prefix="/api/tags", 
    tags=["tags"],
    )

@router.get("/", response_model=List[schemas.Tag])
def read_tags(db: Session = Depends(get_db)):
    ''' GET /api/tags/ - Return all tags. '''
    return crud.get_tags(db)

@router.post("/", response_model=schemas.Tag, status_code=201)
def create_tag(tag: schemas.TagCreate, db: Session = Depends(get_db)):
    ''' POST /api/tags/ - Create a new tag. '''
    return crud.create_tag(db, tag)