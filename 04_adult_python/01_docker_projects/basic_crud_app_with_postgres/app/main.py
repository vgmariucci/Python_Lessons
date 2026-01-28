'''
Purpose:
    - Create FastAPI application instance.
    - Ensure database tables are created.
    - Mount static files and templates for web UI.
    - Include API routers for tasks and tags.
    - Define routes for rendering HTML pages using Jinja2 templates.

Flow:
    - Start point: Uvicorn imports main:app and runs the server.
    - End state: App instance is ready to handle both JSON API calls and HTML page requests.
'''

# Main entrypoint for the FastAPI application
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import engine, get_db
import models
from routers import tasks, tags

# ------ App startup: create tables if they don't exist ------

# This inspects all models inheriting from Base and creates the tables in the database
models.Base.metadata.create_all(bind=engine)

# ------ FastAPI application instance ------
app = FastAPI(title="Tasks & Tags CRUD")

# ------ Static files and templates setup ------

# Serve files from app/static/ under the URL path /static
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure Jinja2 templates directory
templates = Jinja2Templates(directory="templates")

# ------ Include API routers (/api/tasks and /api/tags) -----

app.include_router(tasks.router)
app.include_router(tags.router)

# --- HTML routes (server-rendered pages using Jinja2) ---

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    '''
    GET /

    Start: Browser requests root URL.
    End: Returns rendered index.html template.
    '''
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/tasks", response_class=HTMLResponse)
def tasks_page(request: Request, db: Session = Depends(get_db)):
    '''
    GET /tasks

    - Fetches all tasks and tags from the database.
    - Renders tasks.html template with the fetched data.
    '''

    import crud
    all_tasks = crud.get_tasks(db)
    all_tags = crud.get_tags(db)

    return templates.TemplateResponse(
        "tasks.html", 
        {
            "request": request, # required for Jinja2 templates in FastAPI
            "tasks": all_tasks,
            "tags": all_tags,
        },
    )

@app.get("/tags", response_class=HTMLResponse)
def tags_page(request: Request, db: Session = Depends(get_db)):
    '''
    GET /tags

    - Fetches all tags from the database.
    - Renders tags.html template with the fetched data.
    '''

    import crud
    all_tags = crud.get_tags(db)
    return templates.TemplateResponse(
        "tags.html", 
        {
            "request": request,
            "tags": all_tags,
        },
    )