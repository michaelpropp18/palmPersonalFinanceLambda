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
def put_expense(expense: Expense):
    res = database.put_expense(expense)
    return {
        'statusCode': 200,
        'body': 'yay'
    }

@router.delete("/expenses")
def delete_expenses():
    return {
        'statusCode': 200,
        'body': json.dumps('FIXME')
    }