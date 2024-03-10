from aws_lambda_powertools.event_handler.api_gateway import Router
from aws_lambda_powertools.shared.types import Annotated  
from aws_lambda_powertools.event_handler.openapi.params import Query  

from typing import List, Optional
from datetime import datetime

import database
from models.expense import Expense
from models.income import Income


router = Router()

@router.get("/cashflow")
def get_expenses(
    start: Optional[datetime] = None, 
    end: Optional[datetime] = None
) -> str:
    expenses: List[Expense] = database.get_expenses(start, end)
    incomes: List[Income] = database.get_incomes(start, end)
    cashflow = 0
    for e in expenses:
        cashflow -= e.amount
    for i in incomes:
        cashflow += i.amount
    return cashflow