import boto3

from Dynamo_db import put_data_in_db
def lambda_database_function(event , context):
    
    client = boto3.client('dynamodb')
    table='Ali_alarm_table'
    existing_tables = client.list_tables()["TableNames"]
    if table not in existing_tables:
        #Create Table:
        response = client.create_table(
            AttributeDefinitions=[
            {
                'AttributeName': 'Timestamp',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'sns_message',
                'AttributeType': 'S'
            },
        ],
         TableName=table,
         KeySchema=[
            {
                'AttributeName': 'Timestamp',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'sns_message',
                'KeyType': 'RANGE'
            }
        ],
         BillingMode='PAY_PER_REQUEST'
        )
        response="Table Created"
    else:
        timestamp= str(event["Records"][0]["Sns"]["Timestamp"])
        message= str(event["Records"][0]["Sns"]["Message"])
    #   url=str(events['Records'][0]["Sns"]["id"])
        print(message , timestamp , table)
        response=put_data_in_db(timestamp,message,table)
    return