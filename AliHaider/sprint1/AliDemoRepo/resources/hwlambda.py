def lambda_hwhandler(events , context):
    return "hello {} {} !".format(events['first_name'] , events['last_name'])