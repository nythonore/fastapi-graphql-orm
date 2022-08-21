from core.mixin.model import UUIdMixin, TimeStampMixin

class Example(UUIdMixin, TimeStampMixin, table=True):
  name: str
