'''
Purpose: Define REST endpoints under /api/tasks
Each route calls corresponding functions in crud.py to perform DB operations.
Routes handle:
- Input validation (via Pydantic schemas)
- Dependency injection (DB session)
- HTTP response codes and error handling

'''

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
import schemas
import crud
from database import get_db

# APIRouter groups endpoints under a common prefix and tags
router = APIRouter(
    prefix="/api/tasks", 
    tags=["tasks"],
    )

@router.get("/", response_model=List[schemas.Task])
def read_tasks(
    status: Optional[str] = None, 
    tag_id: Optional[int] = None, 
    db: Session = Depends(get_db)
    ):
    '''
    GET /api/tasks

    Optional query parameters:
    - status: filter tasks by status
    - tag_id: filter tasks associated with a specific tag ID
    '''
    return crud.get_tasks(db, status=status, tag_id=tag_id)

@router.get("/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    '''
    GET /api/tasks/{task_id}
    '''
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.post("/", response_model=schemas.Task, status_code=201)
def create_task(task: schemas.TaskCreate, db:
     Session = Depends(get_db)):
    '''
    POST /api/tasks

    Body: TaskCreate JSON
    '''
    return crud.create_task(db, task)

@router.put("/{task_id}", response_model=schemas.Task)
def update_task(
    task_id: int, 
    task: schemas.TaskUpdate, 
    db: Session = Depends(get_db)
    ):
    '''
    PUT /api/tasks/{task_id}

    Body: TaskUpdate JSON (partial fields update)
    '''
    updated = crud.update_task(db, task_id, task)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated

@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    '''
    DELETE /api/tasks/{task_id}
    '''
    success = crud.delete_task(db, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")