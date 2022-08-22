from datetime import datetime

import strawberry


@strawberry.type
class TypeMixin:
    id: str
    created_at: datetime
    updated_at: datetime
