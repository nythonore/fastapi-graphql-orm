from ...core.mixin.model import ModelMixin


class Example(ModelMixin, table=True):
    __tablename__ = "examples"

    name: str
