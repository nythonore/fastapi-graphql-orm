from core.mixin.model import TimeStampMixin, UUIDMixin


class Example(TimeStampMixin, UUIDMixin, table=True):
    __tablename__ = "examples"

    name: str
