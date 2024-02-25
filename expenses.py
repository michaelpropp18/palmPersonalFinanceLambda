import json
from aws_lambda_powertools.event_handler.api_gateway import Router
from typing import List

import database
from models.expense import Expense


router = Router()

@router.get("/expenses")
def get_expenses() -> List[Expense]:
    return database.get_expenses()

@router.post("/expenses")
def put_expense(expense: Expense) -> str:
    res = database.put_expense(expense)
    if (res == 200 or res == 201):
        return expense.id_
    else:
        return "error"

@router.delete("/expenses")
def delete_expenses():
    return {
        'statusCode': 200,
        'body': json.dumps('FIXME')
    }