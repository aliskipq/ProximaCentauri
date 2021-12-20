import boto3
import constants
def put_data_in_db(timestamp , message , table):
    client = boto3.client('dynamodb')
    
    table = table
    client.put_item(
    TableName=table,
    Item={
    'Timestamp':
        {'S':timestamp},
    'sns_message':
        {'S':message},
        }
        )
    response="Data Inserted"
    
    return response    