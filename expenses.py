import json
from aws_lambda_powertools.event_handler.api_gateway import Router
from pydantic import BaseModel, Field
from datetime import datetime, timezone
from uuid import uuid4
from typing import List, Optional

import client
import database

import boto3
from boto3.dynamodb.conditions import Key

from models.expense import *

router = Router()
db_client = client.initiate_client()

@router.get("/expenses")
def get_expenses() -> List[Expense]:
    return database.get_expenses()

@router.post("/expenses")
def put_expense(expense: Expense) -> Expense:
    database.put_expense(expense)
    return {
        'statusCode': 200,
        'body': 'yay'
    }
    '''
    print(expense.dict(by_alias=True))
    print()
    res = db_client.put_item(
        TableName="Expenses",
        Item=expense.dict(by_alias=True)
    )
    print(res)
    return expense
    '''
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