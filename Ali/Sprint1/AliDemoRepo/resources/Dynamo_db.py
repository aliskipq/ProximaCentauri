import boto3
import constants
def put_data_in_db(timestamp , message):
    client = boto3.client('dynamodb')
    existing_tables = client.list_tables()["TableNames"]
    table = constants.table
    print(existing_tables)
    if table in existing_tables:
        client.put_item(
        TableName=constants.table,
        Item={
        'Timestamp':
            {'S':timestamp},
        'sns_message':
            {'S':message},
            }
            )
        response="Data Inserted"
        return response    