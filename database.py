import json
import boto3
from boto3.dynamodb.conditions import Key
from boto3.dynamodb.types import TypeDeserializer, TypeSerializer

from typing import List
from datetime import datetime
from decimal import Decimal

from models.expense import Expense

EXPENSES_TABLE_NAME = "Expenses"
REGION_NAME = "us-east-1"

dynamodb = boto3.resource('dynamodb', region_name=REGION_NAME)

def get_expenses() -> List[Expense]:
    table = dynamodb.Table(EXPENSES_TABLE_NAME)
    res = table.scan()
    return res['Items']

def put_expense(expense: Expense) -> int:
    table = dynamodb.Table(EXPENSES_TABLE_NAME)
    expense_dict = expense.dict(by_alias=True)
    res = table.put_item(Item=_prepare_dynamodb_dict(expense_dict), ReturnValues='ALL_NEW')
    print(res)
    return res['ResponseMetadata']['HTTPStatusCode']

# remove values that DynamoDB doesn't like
def _prepare_dynamodb_dict(d):
    for k,v in d.items():
        if isinstance(v, float):
            d[k] = Decimal(str(v))
        if isinstance(v, datetime):
            d[k] = str(v)
    return d