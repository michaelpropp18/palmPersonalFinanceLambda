import json

def get_incomes(client):
    res = client.scan(TableName="Incomes")["Items"]
    return {
        'statusCode': 200,
        'body': json.dumps(res)
    }