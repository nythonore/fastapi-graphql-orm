import strawberry

from app.example.schema import ExampleInput, ExampleType


@strawberry.type
class ExampleQuery:
    @strawberry.field
    async def list_examples(self) -> ExampleType:
        return ExampleType(name="example")


@strawberry.type
class ExampleMutation:
    @strawberry.mutation
    async def create_example(self, payload: ExampleInput) -> ExampleType:
        return payload
