import json
from aws_lambda_powertools.event_handler.api_gateway import Router

import client

router = Router()
db_client = client.initiate_client()

@router.get("/expenses")
def get_expenses():
    res = client.scan(TableName="Expenses")["Items"]
    return {
        'statusCode': 200,
        'body': json.dumps(res)
    }

@router.put("/expenses")
def put_expenses():
    body = json.loads(router.current_event['body'])
    print(body)
    print(type(body))
    if (body and 'amount' in body and 'id' in body and 'name' in body):
        res = db_client.put_item(
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

@router.delete("/expenses")
def delete_expenses():
    return {
        'statusCode': 200,
        'body': json.dumps('FIXME')
    }