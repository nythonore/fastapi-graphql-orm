import uuid1, UUID
from sqlmodel import SQLModel, Field

class UUIdMixin(SQLModel):
  id: UUID = Field(default=uuid1().hex, primary_key=True, nullable=False)

class TimeStampMixin(SQLModel):
  created_at: datetime.datetime = Field(default=datetime.datetime.utcnow, nullable=False)
  updated_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow, nullable=False)
