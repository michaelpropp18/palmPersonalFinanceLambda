from aws_lambda_powertools.event_handler.api_gateway import Router
from aws_lambda_powertools.shared.types import Annotated  
from aws_lambda_powertools.event_handler.openapi.params import Query  

from typing import List, Optional
from datetime import datetime

import database
from models.income import Income


router = Router()

@router.get("/incomes")
def get_incomes( 
    start: Optional[datetime] = None, 
    end: Optional[datetime] = None, 
    limit: Annotated[Optional[int], Query(gt=0)] = None,
    exclusive_start_id: Optional[str] = None
) -> List[Income]:
    return database.get_incomes(start, end, limit, exclusive_start_id)

@router.get("/incomes/<income_id>")
def get_income(income_id: str) -> Income:
    return database.get_income(income_id)

@router.post("/incomes")
def post_income(income: Income) -> Income:
    return database.post_income(income)

@router.put("/incomes")
def put_income(income: Income) -> Income:
    return database.put_income(income)

@router.delete("/incomes/<income_id>")
def delete_incomes(income_id: str) -> Income:
    return database.delete_income(income_id)