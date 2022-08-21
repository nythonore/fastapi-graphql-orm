import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.tools import merge_types

from app.example.type import ExampleMutation, ExampleQuery
from config.settings import settings

Query = merge_types("Query", (ExampleQuery,))

Mutation = merge_types("Mutation", (ExampleMutation,))


schema = strawberry.federation.Schema(
    query=Query, mutation=Mutation, enable_federation_2=True
)

graphql = GraphQLRouter(schema, graphiql=settings.APP_DEBUG)
