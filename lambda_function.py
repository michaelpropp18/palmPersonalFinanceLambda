from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.event_handler.api_gateway import Router
from aws_lambda_powertools.utilities.typing import LambdaContext

from health import router as health_router
from expenses import router as expenses_router
from incomes import router as incomes_router


app = APIGatewayRestResolver()

app.include_router(health_router)
app.include_router(expenses_router)
app.include_router(incomes_router)

def lambda_handler(event: dict, context: LambdaContext):
    print('Received event: ', event)
    print('Received context: ', context)
    return app.resolve(event, context)