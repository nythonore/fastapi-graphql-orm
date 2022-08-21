from app.example.model import Example
from core.mixin.crud import CRUDMixin


class ExampleCrud(CRUDMixin[Example]):
    pass


example_crud = ExampleCrud(Example)
