import boto3
import constants

class CloudWatchMetricsDefinition:
    def __init__(self):
        self.client = boto3.client('cloudwatch')
    def _PutData_(self,nameSpace,matricName,dimensions,value):
       response= self.client.put_metric_data(
           Namespace=nameSpace,
           MetricData=[
               {
                 'MetricName':matricName,
                 'Dimensions':dimensions,
                    'Value':value
                   
               }
               ])
        