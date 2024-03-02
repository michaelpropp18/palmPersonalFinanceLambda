from aws_lambda_powertools.event_handler.api_gateway import Router
from typing import List, Optional

import database
from models.expense import Expense


router = Router()

@router.get("/expenses")
def get_expenses(completed: Optional[str] = None) -> List[Expense]:
    print(completed)
    return database.get_expenses()

@router.get("/expenses/<expense_id>")
def get_expense(expense_id: str) -> Expense:
    return database.get_expense(expense_id)

@router.post("/expenses")
def post_expense(expense: Expense) -> Expense:
    return database.post_expense(expense)

@router.put("/expenses")
def put_expense(expense: Expense) -> Expense:
    return database.put_expense(expense)

@router.delete("/expenses/<expense_id>")
def delete_expenses(expense_id: str) -> Expense:
    return database.delete_expense(expense_id)