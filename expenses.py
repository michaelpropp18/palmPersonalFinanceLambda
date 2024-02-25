import json
from aws_lambda_powertools.event_handler.api_gateway import Router
from pydantic import BaseModel, Field
from datetime import datetime, timezone
from uuid import uuid4
from typing import Optional

import client

router = Router()
db_client = client.initiate_client()

class Expense(BaseModel): 
    amount: float 
    id_: int = Field(alias="id", default_factory=lambda: uuid4().int) 
    name: str
    datetime_: datetime = Field(alias="datetime", default_factory=lambda: datetime.now(timezone.utc))

@router.get("/expenses")
def get_expenses():
    res = db_client.scan(TableName="Expenses")["Items"]
    return {
        'statusCode': 200,
        'body': json.dumps(res)
    }

@router.post("/expenses")
def put_expense(expense: Expense) -> Expense:
    print(expense.dict(by_alias=True))
    res = db_client.put_item(
        TableName="Expenses",
        Item=expense_data
    )
    print(res)
    return expense

@router.delete("/expenses")
def delete_expenses():
    return {
        'statusCode': 200,
        'body': json.dumps('FIXME')
    }