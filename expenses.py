import json
from aws_lambda_powertools.event_handler.api_gateway import Router
from pydantic import BaseModel, Field
from datetime import datetime, timezone
from uuid import uuid4
from typing import Optional

import client

import boto3
from boto3.dynamodb.conditions import Key

router = Router()
db_client = client.initiate_client()

class Expense(BaseModel): 
    amount: float 
    id_: int = Field(alias="id", default_factory=lambda: uuid4().int) 
    name: str
    datetime_: datetime = Field(alias="datetime", default_factory=lambda: datetime.now(timezone.utc))

@router.get("/expenses")
def get_expenses():
    dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
    table = dynamodb.Table("Expenses")
    res = table.scan()
    print(res)
    return {
        'statusCode': 200,
        'body': json.dumps(res)
    }
    '''
    res = db_client.scan(TableName="Expenses")["Items"]
    return {
        'statusCode': 200,
        'body': json.dumps(res)
    }
    '''

@router.post("/expenses")
def put_expense(expense: Expense) -> Expense:
    print(expense.dict(by_alias=True))
    print()
    res = db_client.put_item(
        TableName="Expenses",
        Item=expense.dict(by_alias=True)
    )
    print(res)
    return expense
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