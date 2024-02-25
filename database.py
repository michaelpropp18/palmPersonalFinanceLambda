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

def put_expense(expense: Expense):
    table = dynamodb.Table(EXPENSES_TABLE_NAME)
    res = table.put_item(item=expense.dict(by_alias=True))
    return res