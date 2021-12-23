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
    aws_s3 as s3_
    # aws_lambda_event_sources as event_source,

    # aws_lambda_event_sources import SnsEventSource
    
)
from ali_demo_repo.ali_demo_repo_stack import AliDemotempStack
from resources import constants
# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.

class AliPipeLineStage(cdk.Stage):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        Alidemotemp_stack = AliDemotempStack(self,'AliDemotempStack')
        