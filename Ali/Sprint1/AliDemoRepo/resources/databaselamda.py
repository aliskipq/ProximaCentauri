import boto3

from Dynamo_db import put_data_in_db

def database(event,context):
    
    #get event data from Sns subscription:
    timestamp= str(event["Records"][0]["Sns"]["Timestamp"])
    message= str(event["Records"][0]["Sns"]["Message"])
    response = put_data_in_db(timestamp,message)
    
    return response