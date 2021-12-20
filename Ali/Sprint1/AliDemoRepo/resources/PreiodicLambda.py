import urllib3
import constants
import datetime
from cloudwatchmatric import CloudWatchMetricsDefinition
import s3_bucket
def Periodic_Lambda_Handler(events , context):
    
    results=[]
    ###why doesnt s3 bucket work:
    # Urlnames=s3_bucket.s3_bucket_get_data()
    # values=Urlnames.values()
    
    #values = ["www.youtube.com","www.flightradar24.com","www.pakistan.gov.pk","www.skipq.org"] 
    values=['www.youtube.com']
    
    for value in values:
        health=get_health(value)
        Putdata_into_matric(value,health)
        results.append(health)
    
    return health

def Putdata_into_matric(UrlToMonitor,health):
    cw =CloudWatchMetricsDefinition()
    dim = [
        {
            'Name':'URL',
            'Value':UrlToMonitor
        }
        ]
    cw._PutData_(constants.UrlMonitorNameSpace,constants.UrlMonitorNameLatency,dim ,health['latency'])
    cw._PutData_(constants.UrlMonitorNameSpace,constants.UrlMonitorNameAvailability,dim,health['availability'])
    return print(f'done-Cloudwatch{UrlToMonitor}')

def get_health(UrlToMonitor):
    http = urllib3.PoolManager()
    start = datetime.datetime.now()
    res = http.request('GET' ,UrlToMonitor)
    end = datetime.datetime.now()
    delta = end-start
    latsec = round(delta.microseconds * .000001 , 4)
    if res.status == 200:
        return {'availability' : 1.0, 'latency' :latsec , 'url':UrlToMonitor}
    else:
        return {'availability' : 0.0, 'latency' :0 , 'url':UrlToMonitor}
        
