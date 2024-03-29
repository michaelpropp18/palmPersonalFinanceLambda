from aws_lambda_powertools.event_handler.api_gateway import Router
from aws_lambda_powertools.shared.types import Annotated  
from aws_lambda_powertools.event_handler.openapi.params import Query  

from typing import List, Optional
from datetime import datetime

import database
from models.expense import Expense


router = Router()

@router.get("/expenses")
def get_expenses(
    start: Optional[datetime] = None, 
    end: Optional[datetime] = None, 
    limit: Annotated[Optional[int], Query(gt=0)] = None,
    exclusive_start_id: Optional[str] = None
) -> List[Expense]:
    return database.get_expenses(start, end, limit, exclusive_start_id)

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