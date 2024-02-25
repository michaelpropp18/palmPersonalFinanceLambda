import json
import boto3
from boto3.dynamodb.conditions import Key
from boto3.dynamodb.types import TypeDeserializer, TypeSerializer

from typing import List
from decimal import Decimal

from models.expense import Expense

dynamodb = boto3.resource('dynamodb', region_name="us-east-1")

EXPENSES_TABLE_NAME = "Expenses"

def get_expenses() -> List[Expense]:
    table = dynamodb.Table(EXPENSES_TABLE_NAME)
    res = table.scan()
    return res['Items']

def custom_serializer(my_dict):
    for k,v in my_dict.items():
        if isinstance(v, float):
            my_dict[k] = Decimal(str(v))
        if isinstance(v, datetime):
            my_dict[k] = str(v)
    serializer = boto3.dynamodb.types.TypeSerializer()
    return {k: serializer.serialize(v) for k,v in expense_dict.items()}



def put_expense(expense: Expense):
    table = dynamodb.Table(EXPENSES_TABLE_NAME)
    expense_dict = expense.dict(by_alias=True)
    print(expense_dict)
    p1 = json.dumps(expense_dict, default=str)
    print(p1)
    serializer = boto3.dynamodb.types.TypeSerializer()
    p2 = custom_serializer(expense_dict)
    print(p2)
    res = table.put_item(Item=p2)
    return res