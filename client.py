import boto3

def initiate_client():
    client = boto3.client('dynamodb')
    print('boto3 dynamodb client started')
    return client