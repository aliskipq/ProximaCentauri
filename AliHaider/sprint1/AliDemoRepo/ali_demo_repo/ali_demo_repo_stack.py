from aws_cdk import (
    core as cdk,
    # aws_sqs as sqs,
    aws_events as events_,
    aws_events_targets as targets_,
    aws_lambda as lambda_,
    aws_iam,
    aws_cloudwatch as cloudwatch_,
    aws_sns as sns_,
    aws_sns_subscriptions as subscriptions_,
    aws_cloudwatch_actions as actions_
)
from resources import constants
# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.

class AliDemoRepoStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # The code that defines your stack goes here
        
        
        lambda_role_dynamoDb = self.Create_lambda_role()
        
        preiodic_lambda_handler= self.create_lambda('PreiodicLambda' , './resources' , 'PreiodicLambda.PeriodicLambdaHandler',lambda_role)
        preiodic_lambda_handler= self.create_lambda('DynamoDBLambda' , './resources' , 'dynamodblambda.dynamo_db_handler',lambda_role_dynamoDb)
        priodic_event= events_.Schedule.rate(cdk.Duration.minutes(1))
        priodic_event_target= targets_.LambdaFunction(handler=preiodic_lambda_handler)
        priodic_event_rule= events_.Rule(self,"PriodicWebMonitoringRule",enabled=True,schedule=priodic_event,targets=[priodic_event_target])
        ######################Dynamodb lambda function###############################
        #create our table in dynamoDB
        dynamotable=self.create_table()
        
        ################Sns service for Messages#############
        topic=sns_.Topic(self, "WebHealthTopic")
        topic.add_subscription(subscriptions_.EmailSubscription('ali.haider.s@skipq.org'))
        topic.add_subscription(subscriptions_.LambdaSubscription())
        ################availability########################
        #define dimension map to exttact from Cloudwatch
        dimension={'URL':constants.UrlToMonitor}
        #first extract the cloud watch metric data: for that we have cloudwatch.metric class with 
        availability_metric=cloudwatch_.Metric(namespace=constants.MetricNameSpace,
            metric_name=constants.UrlMonitorNameAvailability,
            dimensions_map=dimension,
            period=cdk.Duration.minutes(1),
            label='Availability_Metric')
        #setup Alarm_availability:
        availability_Alarm=cloudwatch_.Alarm(self,id='AvailabilityAlarm',
            metric=availability_metric,
            comparison_operator=cloudwatch_.ComparisonOperator.LESS_THAN_THRESHOLD,
            datapoints_to_alarm=1,
            evaluation_periods=1,
            threshold=1)
        #######################latency####################
        #define dimension map to exttact from Cloudwatch
        dimension={'URL':constants.UrlToMonitor}
        #first extract the cloud watch metric data: for that we have cloudwatch.metric class with 
        latency_metric=cloudwatch_.Metric(namespace=constants.MetricNameSpace,
            metric_name=constants.UrlMonitorNameLatency,
            dimensions_map=dimension,
            period=cdk.Duration.minutes(1),
            label='Latency_Metric')
        #setup Alarm_availability:
        latency_Alarm=cloudwatch_.Alarm(self,id='LatencyAlarm',
            metric=latency_metric,
            comparison_operator=cloudwatch_.ComparisonOperator.GREATER_THAN_THRESHOLD,
            datapoints_to_alarm=1,
            evaluation_periods=1,
            threshold=0.3)
        #####################################################
        availability_Alarm.add_alarm_action(actions_.SnsAction(topic))
        latency_Alarm.add_alarm_action(actions_.SnsAction(topic))
        
            
        #lambda_role = self.Create_lambda_role()
        #hwhandler = self.create_lambda('hwlambdahandler' , './resources' , 'hwlambda.lambda_hwhandler' , lambda_role)
        
        # lambda funciton
        #webhealthlambda= self.create_lambda("webhealthlambda" , './resources' , 'lambda.lambda_handler')
        #first create an event scheduler ;
        #event_schedule=events_.Schedule.rate(cdk.Duration.minutes(1))
        # create event target on which the event will be trigerred:
        #event_target=targets_.LambdaFunction(handler=hwhandler)
        # then define the rule for that event to envoke on event:
        # lambda_rule=events_.Rule(self,"web_health_schedule_rule",description="Periodic Web Health Check",enabled=True
        # ,schedule=,
        # targets=[event_target])
        
    # def Create_lambda_role(self):
        
    def Create_lambda_role(self):
        policyName1='CloudWatchFullAccess'
        policyname2='service-role/AWSLambdaBasicExecutionRole'
        lambdaRole=aws_iam.Role(self,'LambdaRole',
            assumed_by=aws_iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies = [
            aws_iam.ManagedPolicy.from_aws_managed_policy_name(policyName1),
            aws_iam.ManagedPolicy.from_aws_managed_policy_name(policyname2)
            ])
        return lambdaRole
        # example resource
        # queue = sqs.Queue(
        #     self, "AliDemoRepoQueue",
        #     visibility_timeout=cdk.Duration.seconds(300),
        # )
        
    def create_lambda(self , newid , asset , handler,role):
        return lambda_.Function(self, id=newid ,
        code=lambda_.Code.asset(asset),
        handler=handler,
        runtime=lambda_.Runtime.PYTHON_3_6,
        role=role)
        
    def create_table(self):
        
        
