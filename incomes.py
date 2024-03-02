from aws_lambda_powertools.event_handler.api_gateway import Router
from typing import List

import database
from models.income import Income


router = Router()

@router.get("/incomes")
def get_incomes() -> List[Income]:
    return database.get_expenses()