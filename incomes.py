import json
from aws_lambda_powertools.event_handler.api_gateway import Router

import client

router = Router()
db_client = client.initiate_client()

@router.get("/incomes")
def get_incomes():
    res = db_client.scan(TableName="Incomes")["Items"]
    return {
        'statusCode': 200,
        'body': json.dumps(res)
    }