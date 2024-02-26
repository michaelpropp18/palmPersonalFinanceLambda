import json
from aws_lambda_powertools.event_handler.api_gateway import Router
from aws_lambda_powertools.shared.types import Annotated  
from aws_lambda_powertools.event_handler.openapi.params import Path
from typing import List

import database
from models.expense import Expense


router = Router()

@router.get("/expenses")
def get_expenses() -> List[Expense]:
    return database.get_expenses()

@router.post("/expenses")
def put_expense(expense: Expense) -> Expense:
    return database.put_expense(expense)

@router.delete("/expenses/<expense_id>")
def delete_expenses(expense_id):
    database.delete_expense(expense_id)