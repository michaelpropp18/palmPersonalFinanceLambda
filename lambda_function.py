from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.event_handler.api_gateway import Router
from aws_lambda_powertools.utilities.typing import LambdaContext

import json

import health
import expenses
import incomes

app = APIGatewayRestResolver()

app.include_router(health.router)
app.include_router(expenses.router)
app.include_router(incomes.router)

def lambda_handler(event: dict, context: LambdaContext):
    print('Received event: ', event)
    print('Received context: ', context)
    return app.resolve(event, context)