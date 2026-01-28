'''
Purpose: Define the shapes of data FastAPI expects/returns at the API layer. 
These are not DB models.

Flow:
- Incoming JSON bodies from client are validated against TaskCreate / TaskUpdate / TagCreate.
- Outgoing responses are serialized using Task / Tag schemas.

'''
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from models import TaskStatus

#------ Tag schemas ---------

class TagBase(BaseModel):
    '''Common properties shared by Tag-related schemas'''
    name: str

class TagCreate(TagBase):
    '''Schema for creating a new Tag (request body)'''
    pass

class Tag(TagBase):
    '''Schema representing a Tag returned from the API (response body)'''
    id: int

    class Config:
        # Allow Pytdantic to read data from SQLAlchemy model attributes
        from_attributes = True

#------ Task schemas ---------

class TaskBase(BaseModel):
    '''Common properties shared by Task-related schemas.'''
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.pending
    due_date: Optional[datetime] = None

class TaskCreate(TaskBase):
    '''
    Schema for creating a Task via API.

    Client sends this as JSON body to POST /api/tasks.
    '''
    tag_ids: List[int] = []

class TaskUpdate(BaseModel):
    '''
    Schema for partially updating a task via API.

    All fields are optional so client can send only the field to be updated.
    '''
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    due_date: Optional[datetime] = None
    tag_ids: Optional[List[int]] = None

class Task(TaskBase):
    '''
    Schema for a Task returned from the API (response body).
    '''
    id: int
    created_at: datetime
    tags: List[Tag] = []

    class Config:
        from_attributes = True

