# Purpose: Central place to configure SQLAlchemy engine, session factory, and base class

''' 
Database configuration and session management for the application. 
'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Read DB URL from environment variable (.env via docker-compose)
DATABASE_URL = os.getenv("DATABASE_URL")

# Create SQLAlchemy engine: holds DB connection pool
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class: factory to create new DB session objects
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine,
    )

# Base class for ORM models to inherit from (Task, Tag, etc.)
Base = declarative_base()


# Dependency for routes
def get_db():
    '''
    FastAPI dependency that provides a database session to path operations.
    It ensures the session is properly closed after use.

    Usage in routess:
        def route(db: Session = Depends(get_db)):
            ...

    Start: Route handler is called.
    - get_db() creates a SessionLocal instance, yields it to the route.

    End: After the route finishes, the session is closed (finally block).
    '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()