import constants

def lambda_hwhandler(events , context):
    # for i in range(len(constants.UrlToMonitor)):
    #     print(constants.UrlToMonitor[i])
    return "hello {} {} !".format(events['first_name'] , events['last_name'])