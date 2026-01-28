'''
Purpose: Encapsulate direct DB operations (so routes stay thin).

CRUD helper funtions that operate on SQLAlchemy ORM models.

Flow:
- Start point: API route calls crud.* with a Session and a Pydantic schema object (for create/update).
- End state: Database rows are created/updated/deleted as needed, and ORM objects are returned to the route.

'''
from sqlalchemy.orm import Session
from models import Task, Tag
from schemas import TaskCreate, TaskUpdate, TagCreate

# ----- Tag oprerations -----

def get_tags(db: Session):
    '''Return all tags from database.'''
    return db.query(Tag).all()

def get_tag(db: Session, tag_id: int):
    ''' Return a single tag by its ID, or None if not found.'''
    return db.query(Tag).filter(Tag.id == tag_id).first()

def create_tag(db: Session, tag: TagCreate):
    '''
    Insert a new Tag into the database and return the created Tag object.
    
    Start: receives validated TagCreate object from route.
    End: db_tag is committed to DB and refreshed with generated ID.

    '''
    db_tag = Tag(name=tag.name)
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

# ----- Task operations -----

def get_tasks(db: Session, status: str = None, tag_id: int = None):
    '''
    Return tasks, optionally filtered by status and/or tag_id.
    '''
    query = db.query(Task)

    if status:
        query = query.filter(Task.status == status)
    if tag_id:
        query = query.join(Task.tags).filter(Tag.id == tag_id)
    return query.all()

def get_task(db: Session, task_id: int):
    ''' Return a single task by ID, or None if not found.'''
    return db.query(Task).filter(Task.id == task_id).first()

def create_task(db: Session, task: TaskCreate):
    '''
    Create a new Task and associate tags, then return the created Task object.
    '''
    db_task = Task(
        title=task.title,
        description=task.description,
        status=task.status,
        due_date=task.due_date
    )
    # Attach tags by IDs if provided
    if task.tag_ids:
        tags = db.query(Tag).filter(Tag.id.in_(task.tag_ids)).all()
        db_task.tags = tags
    
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, task_update: TaskUpdate):
    ''' Update an existing Task and its tags, then return the updated Task object.'''
    db_task = get_task(db, task_id)
    if not db_task:
        return None
    
    update_data = task_update.model_dump(exclude_unset=True)
    tag_ids = update_data.pop("tag_ids", None)
    
    # Set each attribute on the ORM object
    for key, value in update_data.items():
        setattr(db_task, key, value)
    
    if tag_ids is not None:
        tags = db.query(Tag).filter(Tag.id.in_(tag_ids)).all()
        db_task.tags = tags
    
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int):
    ''' Delete a task by ID. Return True if deleted, False if not found.'''
    db_task = get_task(db, task_id)
    if db_task:
        db.delete(db_task)
        db.commit()
        return True
    return False