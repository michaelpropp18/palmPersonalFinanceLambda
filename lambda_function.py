import json
import boto3

import client
import health
import expenses
import incomes

METHOD_NOT_ALLOWED_RESPONSE = {
    'statusCode': 405,
    'body': json.dumps('Method not allowed')
}

client = client.initiate_client()

def lambda_handler(event, context):
    print('Received event: ', event)
    print('Received context: ', context)
    
    event_path = event['path']
    event_http_method = event['httpMethod']
    
    if event_path == '/health':
        return health.get_health()
    elif event_path.startswith('/expenses'):
        if event_http_method == 'GET':
            return expenses.get_expenses(client)
        elif event_http_method == 'PUT':
            return exepnses.put_expenses(client, event)
        elif event_http_method == 'DELETE':
            return expenses.delete_expenses(client)
        else:
            return METHOD_NOT_ALLOWED_RESPONSE
    elif event_path.startswith('/incomes'):
        if event_http_method == 'GET':
            return incomes.get_incomes(client)
        else:
            return METHOD_NOT_ALLOWED_RESPONSE
    else:  
        return METHOD_NOT_ALLOWED_RESPONSE
