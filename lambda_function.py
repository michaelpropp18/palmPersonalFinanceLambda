import json
import boto3

METHOD_NOT_ALLOWED_RESPONSE = {
    'statusCode': 405,
    'body': json.dumps('Method not allowed')
}

def lambda_handler(event, context):
    # TODO implement
    print('Received event: ', event)
    print('Received context: ', context)
    client = boto3.client('dynamodb')
    print('boto3 dynamodb client started')
    
    event_path = event['path']
    event_http_method = event['httpMethod']
    
    if event_path == '/health':
        return {
            'statusCode': 200,
            'body': json.dumps('Hello from github attempt 2! Palm Personal Finance API is Healthy!')
        }
     
    elif event_path.startswith('/expenses'):
        if event_http_method == 'GET':
            res = client.scan(TableName="Expenses")["Items"]
            return {
                'statusCode': 200,
                'body': json.dumps(res)
            }
        elif event_http_method == ('PUT'):
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
        elif event_http_method == 'DELETE':
            return {
                'statusCode': 200,
                'body': json.dumps('FIXME')
            }
            
        else:
            return METHOD_NOT_ALLOWED_RESPONSE
    
    elif event_path.startswith('/incomes'):
        if event_http_method == 'GET':
            res = client.scan(TableName="Incomes")["Items"]
            return {
                'statusCode': 200,
                'body': json.dumps(res)
            }
        else:
            return METHOD_NOT_ALLOWED_RESPONSE
    else:  
        return METHOD_NOT_ALLOWED_RESPONSE
