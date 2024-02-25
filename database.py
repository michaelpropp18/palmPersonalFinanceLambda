import boto3
from boto3.dynamodb.conditions import Key
from typing import List

from models.expense import Expense

dynamodb = boto3.resource('dynamodb', region_name="us-east-1")

EXPENSES_TABLE_NAME = "Expenses"

def get_expenses() -> List[Expense]:
    table = dynamodb.Table(EXPENSES_TABLE_NAME)
    res = table.scan()
    return res['Items']

def python_to_dynamo(python_object: dict) -> dict:
    serializer = TypeSerializer()
    return {
        k: serializer.serialize(v)
        for k, v in python_object.items()
    }

def put_expense(expense: Expense):
    table = dynamodb.Table(EXPENSES_TABLE_NAME)
    expense_dict = expense.dict(by_alias=True)
    print(expense_dict)
    dynamo_dict = python_to_dynamo(expense_dict)
    print(dynamo_dict)
    res = table.put_item(Item=dynamo_dict)
    return res