from datetime import datetime

import shortuuid
from sqlmodel import Field, SQLModel


class UUIDMixin(SQLModel):
    id: str = Field(
        default_factory=shortuuid.uuid, primary_key=True, index=True, nullable=False
    )


class TimeStampMixin(SQLModel):
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
