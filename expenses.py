import json
from aws_lambda_powertools.event_handler.api_gateway import Router
from pydantic import BaseModel, Field
from uuid import uuid4

import client

router = Router()
db_client = client.initiate_client()

class Expense(BaseModel): 
    amount: float
    id_: Optional[int] = Field(alias="id", default=None)
    title: str
    completed: bool

@router.get("/expenses")
def get_expenses():
    res = db_client.scan(TableName="Expenses")["Items"]
    return {
        'statusCode': 200,
        'body': json.dumps(res)
    }

@router.put("/expenses")
def put_expense():
    expense_data: dict = router.current_event.body  # deserialize json str to dict
    #body = json.loads(router.current_event['body'])
    print(expense_data)
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

@router.delete("/expenses")
def delete_expenses():
    return {
        'statusCode': 200,
        'body': json.dumps('FIXME')
    }