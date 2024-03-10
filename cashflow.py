from aws_lambda_powertools.event_handler.api_gateway import Router

from typing import List, Optional
from datetime import datetime

import database
from models.expense import Expense
from models.income import Income


router = Router()

@router.get("/cashflow")
def get_cashflow_summary(
    start: Optional[datetime] = None, 
    end: Optional[datetime] = None
) -> float:
    incomes: List[Income] = database.get_incomes(start, end)
    expenses: List[Expense] = database.get_expenses(start, end)

    income = sum([i['amount'] for i in incomes])
    expenses = sum([i['amount'] for i in expenses])
    cashflow = income - expenses

    return {
        'income': income,
        'expenses': expenses,
        'cashflow': cashflow
    }