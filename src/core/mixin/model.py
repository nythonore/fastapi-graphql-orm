from datetime import datetime
from typing import List, TypeVar

import shortuuid
from fastapi.encoders import jsonable_encoder
from fastapi_async_sqlalchemy import db
from sqlmodel import Field, SQLModel, select

ModelType = TypeVar("ModelType", bound=SQLModel)


class UUIDMixin(SQLModel):
    id: str = Field(
        default_factory=shortuuid.uuid, primary_key=True, index=True, nullable=False
    )


class TimeStampMixin(SQLModel):
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)


class ModelMixin(TimeStampMixin, UUIDMixin):
    @classmethod
    async def all(cls) -> List[ModelType]:
        query = select(cls)
        result = await db.session.execute(query)

        return result.scalars().all()

    @classmethod
    async def get(cls, pk: str) -> ModelType:
        query = select(cls).where(cls.id == pk)
        result = await db.session.execute(query)

        return result.scalar_one_or_none()

    async def save(self) -> ModelType:
        db.session.add(self)
        await db.session.commit()
        await db.session.refresh(self)

        return self

    @classmethod
    async def create(cls, **kwargs) -> ModelType:
        obj = cls(**jsonable_encoder(kwargs))

        db.session.add(obj)
        await db.session.commit()
        await db.session.refresh(obj)

        return obj

    async def update(self, **kwargs) -> ModelType:
        for field in jsonable_encoder(self):
            if field in kwargs:
                setattr(self, field, kwargs[field])

        if hasattr(self, "updated_at"):
            setattr(self, "updated_at", datetime.utcnow())

        return await self.save()

    async def delete(self) -> None:
        await db.session.delete(self)
        await db.session.commit()
