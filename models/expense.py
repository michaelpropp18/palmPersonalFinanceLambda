from pydantic import BaseModel, Field
from datetime import datetime, timezone
from uuid import uuid4

class Expense(BaseModel): 
    amount: float 
    id_: str = Field(alias="id", default_factory=lambda: uuid4()) 
    name: str
    datetime_: datetime = Field(alias="datetime", default_factory=lambda: datetime.now(timezone.utc))