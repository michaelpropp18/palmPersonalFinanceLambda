from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.event_handler.api_gateway import Router
from aws_lambda_powertools.utilities.typing import LambdaContext

from health import router as health_router
from expenses import router as expenses_router
from incomes import router as incomes_router
from cashflow import router as cashflow_router


app = APIGatewayRestResolver(enable_validation=True)

app.include_router(health_router)
app.include_router(expenses_router)
app.include_router(incomes_router)
app.include_router(cashflow_router)

def lambda_handler(event: dict, context: LambdaContext):
    '''
    This fixes a bug in aws-powertools where it expects at least one query string is provided
    when parameters are present in the routing function header, even if these are all optional
    
    e.g. get_expenses has all optional query parameters, but will fail if the request has no
    query parameters passed in as aws-powertools does a get() on None. 

    Replacing None with {} allows the check to work properly.
    '''
    if event['queryStringParameters'] is None:
        event['queryStringParameters'] = {}
    if event['multiValueQueryStringParameters'] is None:
        event['multiValueQueryStringParameters'] = {}

    print('Received event: ', event)
    print('Received context: ', context)
    return app.resolve(event, context)