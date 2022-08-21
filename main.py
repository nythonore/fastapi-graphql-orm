from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.graphql import graphql

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=['*'],
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*'],
)

app.include_router(graphql, prefix="/graphql")
app.add_websocket_route("/graphql", graphql)
