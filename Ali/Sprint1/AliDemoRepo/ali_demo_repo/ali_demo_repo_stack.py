from aws_cdk import (
    core as cdk,
    aws_events as events_,
    aws_events_targets as targets_,
    aws_lambda as lambda_,
    aws_iam,
    aws_cloudwatch as cloudwatch_,
    aws_sns as sns_,
    aws_sns_subscriptions as subscriptions_,
    aws_cloudwatch_actions as actions_,
    aws_dynamodb as db_,
    aws_sqs as sqs_,
    aws_events_targets as event_targets_,
    aws_lambda_event_sources as event_source,

    # aws_lambda_event_sources import SnsEventSource    
)

from resources import constants


# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.

class AliDemotempStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # The code that defines your stack goes here
        # dyno_lambda_role=self.Create_lambda_role()
        #try making DataBase:
        
        try:
            DB_= self.Create_data_base()
        except: pass
        
        #Create Lambda Role:
        lambda_role = self.Create_lambda_role()
        
        #create Lambdas:
        preiodic_lambda_handler= self.create_lambda('Cloudwatchputlambda' , './resources' , 'PreiodicLambda.Periodic_Lambda_Handler',lambda_role)
        Database_Lambda =self.create_lambda('DataBaseLambda' , './resources' , 'databaselamda.database',lambda_role )
        # lambda funciton grand access:
        DB_.grant_read_write_data(Database_Lambda)    
        
        # DynamoDB_Lambda_handler= self.create_lambda('Dynamoputdatalambda' , './resources' , 'DynamoLambda.lambda_database_function',lambda_role)
        #creation of Psuedo Event:
        priodic_event= events_.Schedule.rate(cdk.Duration.minutes(1))
        priodic_event_target= targets_.LambdaFunction(handler=preiodic_lambda_handler)
        priodic_event_rule= events_.Rule(self,"Priodic_Web_Monitoring_Rule",enabled=True,schedule=priodic_event,targets=[priodic_event_target])
        
        
        #create Topic:
        topic=sns_.Topic(self, "TopicDynamo")
        topic.add_subscription(subscriptions_.EmailSubscription('ali.haider.s@skipq.org'))
        topic.add_subscription(subscriptions_.LambdaSubscription(fn=Database_Lambda))
        
        
        
       
       ######why doesnt it let me create #######
        
        
        # dead_letter_queue = sqs_.Queue(self, "deadLetterQueue")
        # DynamoDB_Lambda_handler.add_event_source(event_source.SnsEventSource(topic,
        # filter_policy={},
        # dead_letter_queue=dead_letter_queue 
        #     ))
        
        # DynamoDBLambda_handler.add_event_source(event_source.SnsEventSource(topic,
        # filter_policy={},
        # dead_letter_queue=dead_letter_queue
        #     ))
        # Dblambdatarget=event_targets_.LambdaFunction(handler=DynamoDBLambda_handler)
        
        # rule = events_.Rule(self, "rule",
        #         event_pattern=events.EventPattern(
        #         source=
        #             )
        #         )
        
        
        
        # rule.add_target(targets.LambdaFunction(fn,
        # dead_letter_queue=queue,  # Optional: add a dead letter queue
        # max_event_age=cdk.Duration.hours(2),  # Optional: set the maxEventAge retry policy
        # retry_attempts=2
        #         ))
        
        # DynamoDBRule = events_.Rule(self , ) 
        
        
        
        # values = ["www.youtube.com","www.flightradar24.com","www.pakistan.gov.pk","www.skipq.org"]
        values=['www.youtube.com','www.flightradar24.com']
        for value in values:
            self.Urltomonitor_=value
            availability_Alarm=self.setup_Availability_alarms_()
            latency_Alarm=self.setup_Latency_alarms_()
            latency_Alarm.add_alarm_action(actions_.SnsAction(topic)) 
            availability_Alarm.add_alarm_action(actions_.SnsAction(topic))
    
    
    
    
    #Functions For Use:
    def Create_data_base(self):
        table = db_.Table(self, constants.table,
        partition_key=db_.Attribute(name="Timestamp", type=db_.AttributeType.STRING),
        sort_key=db_.Attribute(name="sns_message", type=db_.AttributeType.STRING),
        billing_mode=db_.BillingMode.PAY_PER_REQUEST
        )
        return table
    
    def setup_Availability_alarms_(self):
        
        dimension={'URL':self.Urltomonitor_}
        availability_metric=cloudwatch_.Metric(namespace=constants.UrlMonitorNameSpace,
            metric_name=constants.UrlMonitorNameAvailability,
            dimensions_map=dimension,
            period=cdk.Duration.minutes(1),
            label='Availability_Metric')
        #3.setup Alarm on data:
        availability_Alarm=cloudwatch_.Alarm(self,id=f'AvailabilityAlarm{self.Urltomonitor_}',
            metric=availability_metric,
            comparison_operator=cloudwatch_.ComparisonOperator.LESS_THAN_THRESHOLD,
            datapoints_to_alarm=1,
            evaluation_periods=1,
            threshold=1)
        
        return  availability_Alarm
    
    def setup_Latency_alarms_(self):

        dimension={'URL':self.Urltomonitor_}
        latency_metric=cloudwatch_.Metric(namespace=constants.UrlMonitorNameSpace,
            metric_name=constants.UrlMonitorNameLatency,
            dimensions_map=dimension,
            period=cdk.Duration.minutes(1),
            label='Latency_Metric')
        #setup Alarm on data:
        latency_Alarm=cloudwatch_.Alarm(self,id=f'LatencyAlarm{self.Urltomonitor_}',
            metric=latency_metric,
            comparison_operator=cloudwatch_.ComparisonOperator.GREATER_THAN_THRESHOLD,
            datapoints_to_alarm=1,
            evaluation_periods=1,
            threshold=0.52)
        
        return  latency_Alarm
        
    # def Create_lambda_role(self):
    def Create_lambda_role(self):
        policyName1='CloudWatchFullAccess'
        policyname2='service-role/AWSLambdaBasicExecutionRole'
        policyname3='AmazonDynamoDBFullAccess'
        lambdaRole=aws_iam.Role(self,'LambdaRole',
            assumed_by=aws_iam.CompositePrincipal(aws_iam.ServicePrincipal("lambda.amazonaws.com"),
            aws_iam.ServicePrincipal("sns.amazonaws.com"))
            ,
            managed_policies = [
            aws_iam.ManagedPolicy.from_aws_managed_policy_name(policyName1),
            aws_iam.ManagedPolicy.from_aws_managed_policy_name(policyname2),
            aws_iam.ManagedPolicy.from_aws_managed_policy_name(policyname3)
            ])
        return lambdaRole
    
   # create lambda Function: 
    def create_lambda(self , newid , asset , handler,role):#,#role):
        return lambda_.Function(self, id=newid ,
        code=lambda_.Code.asset(asset),
        handler=handler,
        runtime=lambda_.Runtime.PYTHON_3_6,
        role=role)
        
        
