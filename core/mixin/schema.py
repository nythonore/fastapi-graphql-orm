import strawberry, uuid, datetime

@strawberry.type
class TypeMixin:
  id: uuid.UUID
  created_at: datetime.datetime
  updated_at: datetime.datetime
