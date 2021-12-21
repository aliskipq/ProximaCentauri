import boto3
import ast
import constants

def s3_bucket_get_data():
    #initialize variables:
    access_key_id=''
    secret_key=''
    region='us-east-2'
    bucket_name='tempbucket1'
    bucket_file_name='URLS.JSON'
    #Make S3 client:
    client = boto3.client(
    's3',
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_key,
    region_name=region)
    #list all Buckets:
    clientResponse = client.list_buckets()
    print(clientResponse['Buckets'])
    names = []
    # for bucket in clientResponse['Buckets']:
    obj = client.get_object(
    Bucket = bucket_name,
    Key = bucket_file_name)
    dict1=obj['Body'].read()
    dict1=ast.literal_eval(dict1.decode("utf-8"))
    
    #return List of Urls in Bucket file
    return dict1
    
    