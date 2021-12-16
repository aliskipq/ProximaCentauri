import urllib3
import constants
import datetime
from cloudwatchmatric import CloudWatchMetricsDefinition
def PeriodicLambdaHandler(events , context):
    values= dict()
    cw =CloudWatchMetricsDefinition()
    
    latency= get_latency()
    
    dim = [
        {
            'Name':'URL',
            'Value':constants.UrlToMonitor
        }
        ]
        
    cw._PutData_(constants.MetricNameSpace,constants.UrlMonitorNameLatency,dim ,latency)
    availability=get_avalaibality()
    cw._PutData_(constants.MetricNameSpace,constants.UrlMonitorNameAvailability,dim,availability)
    values.update({"latency":latency , "availability" :availability })
    return values

def get_latency():
    http = urllib3.PoolManager()
    start = datetime.datetime.now()
    res = http.request('GET' , constants.UrlToMonitor)
    end = datetime.datetime.now()
    delta = end-start
    latsec = round(delta.microseconds * .000001 , 4)
    return latsec
    
def get_avalaibality():
    http=urllib3.PoolManager()
    res = http.request('GET' , constants.UrlToMonitor)
    if res.status == 200:
        return 1.0
    else:
        return 0.0