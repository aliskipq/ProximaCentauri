from aws_cdk import (
    core as cdk,
    # aws_sqs as sqs,
    aws_events as events_,
    aws_events_targets as targets_,
    core,
    aws_lambda as lambda_,
    aws_iam
    
)

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.

class AliDemoRepoStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # The code that defines your stack goes here
        
        
        lambda_role = self.Create_lambda_role()
        
        preiodic_lambda_handler= self.create_lambda('PreiodicLambda' , './resources' , 'PreiodicLambda.PeriodicLambdaHandler',lambda_role)
        priodic_event= events_.Schedule.rate(cdk.Duration.minutes(1))
        priodic_event_target= targets_.LambdaFunction(handler=preiodic_lambda_handler)
        priodic_event_rule= events_.Rule(self,"PriodicWebMonitoringRule",enabled=True,schedule=priodic_event,targets=[priodic_event_target])
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
        
        
