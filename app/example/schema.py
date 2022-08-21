import strawberry

from core.mixin.schema import TypeMixin


@strawberry.type
class ExampleType(TypeMixin):
    name: str


@strawberry.input
class ExampleInput:
    name: str
