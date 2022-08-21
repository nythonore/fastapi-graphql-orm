from datetime import datetime
from typing import Generic, List, Type, TypeVar

from fastapi.encoders import jsonable_encoder
from fastapi_async_sqlalchemy import db
from sqlmodel import SQLModel, select

ModelType = TypeVar("ModelType", bound=SQLModel)


class CRUDMixin(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def all(self) -> List[ModelType]:
        query = select(self.model)
        result = await db.session.execute(query)

        return result.scalars().all()

    async def get(self, id: str) -> ModelType:
        query = select(self.model).where(self.model.id == id)
        result = await db.session.execute(query)

        return result.scalar_one_or_none()

    async def save(self, obj: ModelType) -> ModelType:
        db.session.add(obj)
        await db.session.commit()
        await db.session.refresh(obj)

        return obj

    async def create(self, **kwargs) -> ModelType:
        obj = self.model(**jsonable_encoder(kwargs))
        return await self.save(obj)

    async def update(self, obj: ModelType, **kwargs) -> ModelType:
        for field in jsonable_encoder(obj):
            if field in kwargs:
                setattr(obj, field, kwargs[field])

        if hasattr(obj, "updated_at"):
            setattr(obj, "updated_at", datetime.utcnow())

        return await self.save(obj)

    async def delete(self, obj: ModelType) -> None:
        await db.session.delete(obj)
        await db.session.commit()
