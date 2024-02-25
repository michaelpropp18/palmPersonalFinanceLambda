import boto3
from boto3.dynamodb.conditions import Key
from typing import List

import models.expense

dynamodb = boto3.resource('dynamodb', region_name="us-east-1")

EXPENSES_TABLE_NAME = "Expenses"

def get_expenses() -> List[Expense]:
    dynamodb =  dynamodb.Table(EXPENSES_TABLE_NAME)
    res = table.scan()
    return res['Items']