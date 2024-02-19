import json

def get_expenses(client):
    res = client.scan(TableName="Expenses")["Items"]
    return {
        'statusCode': 200,
        'body': json.dumps(res)
    }

def put_expenses(client, event):
    body = json.loads(event['body'])
    print(body)
    print(type(body))
    if (body and 'amount' in body and 'id' in body and 'name' in body):
        res = client.put_item(
            TableName="Expenses",
            Item=body
        )
        return {
            'statusCode': res['ResponseMetadata']['HTTPStatusCode'],
            'body': json.dumps(res)
        }
        else:
            return {
                'statusCode': 400,
                'body': json.dumps('amount, id, and name are all required fields')
            }

def delete_expenses(client):
    return {
        'statusCode': 200,
        'body': json.dumps('FIXME')
    }