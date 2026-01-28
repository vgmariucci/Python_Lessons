'''
SQLAlchemy ORM models for tasks, tags, and their relationships.
'''
from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, Table, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base
import enum

# Association (join) table for many-to-many Task <-> Tag relationship
task_tags = Table(
    'task_tags',
    Base.metadata,
    Column('task_id', Integer, ForeignKey('tasks.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True)
)

class TaskStatus(str, enum.Enum):
    '''
    Enum for allowed task statuses.

    Stored as string in the DB: 'pending', 'in_progress', 'done'
    '''
    pending = "pending"
    in_progress = "in_progress"
    done = "done"

class Task(Base):
    '''
    Represents a task row in the 'tasks' table.
    '''
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(Enum(TaskStatus), default=TaskStatus.pending, nullable=False)
    due_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.now, nullable=False)

    # Many-to-many relationship with Tag through task_tags association table
    tags = relationship(
        "Tag", 
        secondary=task_tags, 
        back_populates="tasks",
        )

class Tag(Base):
    '''
    Represents a tag row in the 'tags' table.
    '''
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)

    # Back-reference to tasks that have this tag
    tasks = relationship(
        "Task", 
        secondary=task_tags, 
        back_populates="tags",
        )