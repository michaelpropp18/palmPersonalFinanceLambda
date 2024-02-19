import json

def get_health():
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from powertools branch! Palm Personal Finance API is Healthy!')
    }