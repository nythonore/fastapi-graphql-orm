from typing import List

import strawberry

from app.example.crud import example_crud
from app.example.schema import ExampleInput, ExampleType


@strawberry.type
class ExampleQuery:
    @strawberry.field
    async def list_examples(self) -> List[ExampleType]:
        return await example_crud.all()


@strawberry.type
class ExampleMutation:
    @strawberry.mutation
    async def create_example(self, payload: ExampleInput) -> ExampleType:
        return await example_crud.create(**payload.__dict__)

    @strawberry.mutation
    async def update_example(self, id: str, payload: ExampleInput) -> ExampleType:
        obj = await example_crud.get(id)

        if obj:
            return await example_crud.update(obj, **payload.__dict__)
        raise Exception("Example not found")
