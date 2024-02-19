import json

def get_health():
    return {
        'statusCode': 200,
        'body': json.dumps('Palm Personal Finance API is Healthy!')
    }