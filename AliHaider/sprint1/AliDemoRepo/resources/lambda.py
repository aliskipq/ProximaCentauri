import datetime
import urllib3
import constants
from cloudwatchMetric import CloudWatchMetricsDefinition

def lambda_handler(events , context):
    # UrlToMonitor = 'www.skipq.org'
    values = dict()
    cw = CloudWatchMetricsDefinition();
    latency = get_latency(constants.UrlToMonitor)
    dim=[
        {
            "Name":"URL",
            "Value":constants.UrlToMonitor
        }
        ]
    cw.ShowData('AliCloudWatch' , constants.UrlMonitorNameLatency , dim , latency)
    availability = get_avalaibality(constants.UrlToMonitor)
    
    cw.ShowData('AliCloudWatch' , constants.UrlMonitorNameAvailability , dim , availability)
    values.update({'Availability':availability , 'Latency':latency})
    
    return values
    
def get_latency(url_to_monitor):
    http = urllib3.PoolManager()
    start = datetime.datetime.now()
    r = http.request('GET', url_to_monitor)
    end = datetime.datetime.now()
    delta = end-start
    latsec = round(delta.microseconds * .000001 , 4) 
    return latsec
    
    
def get_avalaibality(url_to_monitor):
    http = urllib3.PoolManager()
    r = http.request('GET', url_to_monitor)
    if r.status==200:
        return 1.0
    else:
        return 0.0