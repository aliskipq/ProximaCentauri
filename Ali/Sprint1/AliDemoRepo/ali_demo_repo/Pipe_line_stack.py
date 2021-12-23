from aws_cdk import (
    core as cdk,
    pipelines as pipelines_,
    aws_codepipeline_actions as cpactions_
    )
from ali_demo_repo.pipe_line_stage import AliPipeLineStage

class AliPipe_line_Stack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        source = pipelines_.CodePipelineSource.git_hub(
            repo_string='aliskipq/ProximaCentauri',
            branch='main',
            authentication=cdk.SecretValue.secrets_manager("alisecretkey"),
            trigger=cpactions_.GitHubTrigger.POLL
            )
        synth=pipelines_.ShellStep("synth",
        input=source,
        commands=["cd Ali/Sprint1/AliDemoRepo" , "pip install -r requirements.txt", "npm install -g aws-cdk", "cdk synth"],
        primary_output_directory="Ali/Sprint1/AliDemoRepo/cdk.out"
        ) 
        pipeline = pipelines_.CodePipeline(self , 'Alicodepipeline' , synth=synth )
        beta = AliPipeLineStage(self,'Beta')
        pipeline.add_stage(beta)
        
        