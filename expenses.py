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
    #amount: float
    #id_: int = Field(alias="id", default=uuid4().int)
    name: str
    #datetime_: datetime = Field(alies="datetime", default=datetime.now(timezone.utc))

@router.get("/expenses")
def get_expenses():
    res = db_client.scan(TableName="Expenses")["Items"]
    return {
        'statusCode': 200,
        'body': json.dumps(res)
    }

@router.post("/expenses")
def put_expense(expense: Expense) -> str:
    expense_data: dict = router.current_event.body  # deserialize json str to dict
    #body = json.loads(router.current_event['body'])
    print(expense_data)
    print(expense.dict(by_alias=True))
    return "1"
    '''
    if (expense_data and 'amount' in expense_data and 'id' in expense_data and 'name' in expense_data):
        res = db_client.put_item(
            TableName="Expenses",
            Item=expense_data
        )
        return {
            'statusCode': res['ResponseMetadata']['HTTPStatusCode'],
            'body': json.dumps(res)
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('amount, id, and name are all required fields')
        }
    '''

@router.delete("/expenses")
def delete_expenses():
    return {
        'statusCode': 200,
        'body': json.dumps('FIXME')
    }