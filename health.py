import json
from aws_lambda_powertools.event_handler.api_gateway import Router

router = Router()

@router.get("/health")
def get_health():
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from health router! Palm Personal Finance API is Healthy!')
    }

'''
def get_health():
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from powertools branch! Palm Personal Finance API is Healthy!')
    }
'''