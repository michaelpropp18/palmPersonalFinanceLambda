import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
from boto3.dynamodb.types import TypeDeserializer, TypeSerializer
from botocore.exceptions import ClientError

from typing import List, Optional
from datetime import datetime
from decimal import Decimal

from models.expense import Expense
from models.income import Income

EXPENSES_TABLE_NAME = "Expenses"
INCOMES_TABLE_NAME = "Incomes"
REGION_NAME = "us-east-1"

dynamodb = boto3.resource('dynamodb', region_name=REGION_NAME)

##############################################################
# Expenses
##############################################################
    
def get_expenses(
    start: Optional[datetime] = None, 
    end: Optional[datetime] = None, 
    limit: Optional[int] = None,
    exclusive_start_id: Optional[str] = None
) -> List[Expense]:
    params = {}
    filter_expression = _filter_expression_builder(start, end)
    if filter_expression:
        params['FilterExpression'] = filter_expression
    if limit:
        params['Limit'] = limit
    if exclusive_start_id:
        params['ExclusiveStartKey'] = exclusive_start_id
    table = dynamodb.Table(EXPENSES_TABLE_NAME)
    res = table.scan(**params)
    return res['Items']

def get_expense(expense_id: str) -> Expense:
    table = dynamodb.Table(EXPENSES_TABLE_NAME)
    res = table.get_item(Key={'id': expense_id})
    if 'Item' in res:
        return res['Item']

def post_expense(expense: Expense) -> Expense:
    table = dynamodb.Table(EXPENSES_TABLE_NAME)
    expense_dict = expense.dict(by_alias=True)
    res = table.put_item(Item=_prepare_dynamodb_dict(expense_dict))
    print(res)
    if res['ResponseMetadata']['HTTPStatusCode'] == 200:
        return expense

def put_expense(expense: Expense) -> Expense:
    table = dynamodb.Table(EXPENSES_TABLE_NAME)
    expense_dict = expense.dict(by_alias=True)
    try:
        res = table.put_item(
            Item=_prepare_dynamodb_dict(expense_dict),
            ConditionExpression=Attr('id').eq(expense.id_),
            ReturnValues='ALL_OLD'
        )
    except ClientError as e:
        print(e)
        return
    print(res)
    if res['ResponseMetadata']['HTTPStatusCode'] == 200 and 'Attributes' in res:
        return res['Attributes']
    

def delete_expense(expense_id: str) -> Expense:
    table = dynamodb.Table(EXPENSES_TABLE_NAME)
    res = table.delete_item(Key={'id': expense_id}, ReturnValues="ALL_OLD")
    print(res)
    if res['ResponseMetadata']['HTTPStatusCode'] == 200 and 'Attributes' in res:
        return res['Attributes']

##############################################################
# Incomes
##############################################################

def get_incomes() -> List[Income]:
    table = dynamodb.Table(INCOMES_TABLE_NAME)
    res = table.scan()
    return res['Items']

def get_income(income_id: str) -> Income:
    table = dynamodb.Table(INCOMES_TABLE_NAME)
    res = table.get_item(Key={'id': income_id})
    if 'Item' in res:
        return res['Item']

def post_income(income: Income) -> Income:
    table = dynamodb.Table(INCOMES_TABLE_NAME)
    income_dict = income.dict(by_alias=True)
    res = table.put_item(Item=_prepare_dynamodb_dict(income_dict))
    print(res)
    if res['ResponseMetadata']['HTTPStatusCode'] == 200:
        return income

def put_income(income: Income) -> Income:
    table = dynamodb.Table(INCOMES_TABLE_NAME)
    income_dict = income.dict(by_alias=True)
    try:
        res = table.put_item(
            Item=_prepare_dynamodb_dict(income_dict),
            ConditionExpression=Attr('id').eq(income.id_),
            ReturnValues='ALL_OLD'
        )
    except ClientError as e:
        print(e)
        return
    print(res)
    if res['ResponseMetadata']['HTTPStatusCode'] == 200 and 'Attributes' in res:
        return res['Attributes']
    

def delete_income(income_id: str) -> Income:
    table = dynamodb.Table(INCOMES_TABLE_NAME)
    res = table.delete_item(Key={'id': income_id}, ReturnValues="ALL_OLD")
    print(res)
    if res['ResponseMetadata']['HTTPStatusCode'] == 200 and 'Attributes' in res:
        return res['Attributes']

##############################################################
# Utilities
##############################################################

# remove values that DynamoDB doesn't like
def _prepare_dynamodb_dict(d):
    for k,v in d.items():
        if isinstance(v, float):
            d[k] = Decimal(str(v))
        if isinstance(v, datetime):
            d[k] = str(v)
    return d

# form a filter expression using args
def _filter_expression_builder(start: Optional[datetime] = None, end: Optional[datetime] = None):
    attrs = []
    if start is not None:
        attrs.append(Attr('datetime').gte(str(start)))
    if end is not None:
        attrs.append(Attr('datetime').lte(str(end)))
    filter_expression = None
    for a in attrs:
        if filter_expression is None:
            filter_expression = a
        else:
            filter_expression &= a
    print(filter_expression)
    return filter_expression