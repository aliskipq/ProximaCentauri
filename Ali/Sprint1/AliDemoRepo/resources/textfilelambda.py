import datetime
import urllib3
import constants
import shutil
# import pandas
# import aws
# import aws_cdk.aws_s3 as s3
import boto3
import json
import ast
import s3_bucket
# from cloudwatchMetric import CloudWatchMetricsDefinition

def lambda_handler_textfile(events , context):
    Urlnames=s3_bucket.s3_bucket_get_data()
    print(Urlnames)
    # UrlToMonitor = 'https://tempbucket1.s3.us-east-2.amazonaws.com/newtemp.JSON'
    # http = urllib3.PoolManager()
    # client = boto3.client(
    # 's3',
    # aws_access_key_id = 'AKIAUTEXLE6CPTABHY7W',
    # aws_secret_access_key = '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',
    # region_name = 'us-east-2')
    
    # # resource = boto3.resource(
    # # 's3',
    # # aws_access_key_id = 'AKIAUTEXLE6CPTABHY7W',
    # # aws_secret_access_key = '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',
    # # region_name = 'us-east-2'
    # #     )
        
    
       
    # clientResponse = client.list_buckets()
    # # my_bucket=client.bucket('tempbucket1')
    # names = dict()
    # # Print the bucket names one by one
    # print('Printing bucket names...')
    # for bucket in clientResponse['Buckets']:
    #     if(bucket['Name']=='tempbucket1'):
    #         obj = client.get_object(
    #         Bucket = 'tempbucket1',
    #         Key = 'URLS.JSON')
    #         dict1=obj['Body'].read()
    #         dict2=ast.literal_eval(dict1.decode("utf-8"))
    #         # URL1 = dict2['URL1']
    #         values = dict2.values()
    #         for value in values:
    #             constants.UrlToMonitor.append(value)
                
            # json_acceptable_string = dict2.replace("'", '"')
            # dict2=ast.literal_eval(dict2)
            # print(URL1)#)names.update(dict1)
            
    
    # print(names['key'])
    
#     obj = client.get_object(
#     Bucket = 'tempbucket1',
#     Key = 'sql-shack-demo.csv')

        # names[f'{bucket}'] = {bucket["Name"]}
    return print('Done')
    # client = boto3.client('s3',aws_access_key_id = )
    # obj = client.get_object(
    # Bucket = 'tempbucket1',
    # Key = 'newtemp.JSON')
    # value_=pandas.read_csv(obj['Body'])
    # return value_
    # resp = http.request('GET',UrlToMonitor)
    # print(resp)
    # temp=resp.data
    # with open('constants.py', 'wt') as out:
    #     r = http.request('GET', UrlToMonitor , preload_content=False)
    #     shutil.copyfileobj(r, out)
    # # temp=json.dumps(resp)
    # r.release_conn()
    # return r.data
    
    
    
    # f = open(filename , 'wb')
    # f.write(resp.data)
    # f.close()
    
    # UrlToMonitor = 'www.skipq.org'
#     values = dict()
#     cw = CloudWatchMetricsDefinition();
#     latency = get_latency(constants.UrlToMonitor)
#     dim=[
#         {
#             "Name":"URL",
#             "Value":constants.UrlToMonitor
#         }
#         ]
#     cw.ShowData('AliCloudWatch' , constants.UrlMonitorNameLatency , dim , latency)
#     availability = get_avalaibality(constants.UrlToMonitor)
    
#     cw.ShowData('AliCloudWatch' , constants.UrlMonitorNameAvailability , dim , availability)
#     values.update({'Availability':availability , 'Latency':latency})
    
#     return values
    
# def get_latency(url_to_monitor):
#     http = urllib3.PoolManager()
#     start = datetime.datetime.now()
#     r = http.request('GET', url_to_monitor)
#     end = datetime.datetime.now()
#     delta = end-start
#     latsec = round(delta.microseconds * .000001 , 4) 
#     return latsec
    
    
# def get_avalaibality(url_to_monitor):
#     http = urllib3.PoolManager()
#     r = http.request('GET', url_to_monitor)
#     if r.status==200:
#         return 1.0
#     else:
#         return 0.0