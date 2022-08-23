from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_async_sqlalchemy import SQLAlchemyMiddleware

from .config.database import DATABASE_URL
from .config.graphql import graphql
from .config.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    docs_url=None,
    redoc_url="/docs" if settings.APP_DEBUG else None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(SQLAlchemyMiddleware, db_url=DATABASE_URL)


app.include_router(graphql, prefix="/graphql")
app.add_websocket_route("/graphql", graphql)
