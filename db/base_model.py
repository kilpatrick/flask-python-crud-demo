from datetime import datetime
from pydantic import BaseModel
from uuid import UUID


class DBSharedCols(BaseModel):
    created_at: datetime
    deleted: bool
    deleted_at: datetime
    family_id: UUID
    school_id: UUID
    updated_at: datetime
    uuid: UUID
