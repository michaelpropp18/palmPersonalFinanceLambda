from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.event_handler.api_gateway import Router
import json

import client
import health
import expenses
import incomes

app = APIGatewayRestResolver()
db_client = client.initiate_client()
router = Router()

@router.get("/health")
def get_health():
    return health.get_health()

@router.get("/expenses")
def get_expenses():
    return expenses.get_expenses(db_client)

@router.put("/expenses")
def put_expenses():
    return expenses.put_expenses(db_client, router.current_event)

@router.delete("/expenses")
def delete_expenses():
    return expenses.delete_expenses(db_client)

@router.get("/incomes")
def get_incomes():
    return incomes.get_incomes(db_client)

app.include_router(router)

def lambda_handler(event: dict, context: LambdaContext):
    print('Received event: ', event)
    print('Received context: ', context)
    return app.resolve(event, context)