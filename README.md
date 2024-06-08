# se-technical-assessment

## Project setup

Create a `.env` file. Please look at the `.env.example` and adjust the connection settings for the database.

The `DATABASE_URL` should look like:

```
DATABASE_URL=postgresql+asyncpg://{user}:{password}@db/{databasename}
```

### Build and run the app with Docker Compose

```
docker compose build
docker compose up -d
```

### Build app without Docker

```
pip install --no-cache-dir -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## Project structure

Here's the structure of the project.

```
├── alembic
├── alembic.ini
└── app
    ├── __init__.py
    ├── config.py
    ├── main.py
    ├── api
    │   ├── __init__.py
    │   └── feedbacks.py
    ├── db
    │   ├── __init__.py
    │   ├── base.py
    │   ├── models.py
    │   └── session.py
    ├── models
    │   ├── __init__.py
    │   └── feedback.py
    └── repositories
        ├── __init__.py
        └── feedback.py
```

`/alembic/` and `alembic.ini` was built using the `async` template. The app's core is located inside `/app/`.

* `config.py` reads the `.env` file to be reused by other parts of the app.
* `main.py` is the entrypoint of the app.
* `/api/` contains endpoint definitions.
* `/db/` consists of files for SQLAlchemy to work.
* `/models/` consists of Pydantic models.
* `/repositories/` handles the database operations. 


## Endpoint

There are two endpoints:

```
GET     /api/feedbacks/
POST    /api/feedbacks/
```

More detailed information is available on the built-in Swagger documentation in `/docs` (ex: `http://localhost:8000/docs`).
