from aws_lambda_powertools.event_handler.api_gateway import Router
from aws_lambda_powertools.shared.types import Annotated  
from aws_lambda_powertools.event_handler.openapi.params import Query  

from typing import List, Optional
from datetime import datetime

import database


router = Router()

@router.get("/cashflow")
def get_expenses(
    start: Optional[datetime] = None, 
    end: Optional[datetime] = None
) -> str:
    expenses = database.get_expenses(start, end)
    incomes = database.get_incomes(start, end)
    return "GOT HERE"