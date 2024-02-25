from pydantic import BaseModel, Field
from datetime import datetime, timezone
from uuid import uuid4
from decimal import Decimal

class Expense(BaseModel): 
    amount: Decimal 
    id_: int = Field(alias="id", default_factory=lambda: uuid4().int) 
    name: str
    datetime_: datetime = Field(alias="datetime", default_factory=lambda: datetime.now(timezone.utc))