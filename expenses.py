import json

def get_expenses():
    res = client.scan(TableName="Expenses")["Items"]
    return {
        'statusCode': 200,
        'body': json.dumps(res)
    }