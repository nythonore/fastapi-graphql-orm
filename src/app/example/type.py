from typing import List

import strawberry

from .model import Example
from .schema import ExampleInput, ExampleType


@strawberry.type
class ExampleQuery:
    @strawberry.field
    async def list_examples(self) -> List[ExampleType]:
        return await Example.all()


@strawberry.type
class ExampleMutation:
    @strawberry.mutation
    async def create_example(self, payload: ExampleInput) -> ExampleType:
        return await Example.create(**payload.__dict__)

    @strawberry.mutation
    async def update_example(self, id: str, payload: ExampleInput) -> ExampleType:
        obj = await Example.get(id)

        if obj:
            return await obj.update(**payload.__dict__)
        raise Exception("Example not found")
