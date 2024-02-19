from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.event_handler.api_gateway import Router
import json

import client
import health
import expenses
import incomes

METHOD_NOT_ALLOWED_RESPONSE = {
    'statusCode': 405,
    'body': json.dumps('Method not allowed')
}

app = APIGatewayRestResolver()
db_client = client.initiate_client()
router = Router()

@router.get("/health")
def get_health():
    return health.get_health()

app.include_router(router)

def lambda_handler(event, context):
    return app.resolve(event, context)

'''
    print('Received event: ', event)
    print('Received context: ', context)
    
    event_path = event['path']
    event_http_method = event['httpMethod']
    
    if event_path == '/health':
        return health.get_health()
    elif event_path.startswith('/expenses'):
        if event_http_method == 'GET':
            return expenses.get_expenses(db_client)
        elif event_http_method == 'PUT':
            return exepnses.put_expenses(db_client, event)
        elif event_http_method == 'DELETE':
            return expenses.delete_expenses(db_client)
        else:
            return METHOD_NOT_ALLOWED_RESPONSE
    elif event_path.startswith('/incomes'):
        if event_http_method == 'GET':
            return incomes.get_incomes(db_client)
        else:
            return METHOD_NOT_ALLOWED_RESPONSE
    else:  
        return METHOD_NOT_ALLOWED_RESPONSE
'''