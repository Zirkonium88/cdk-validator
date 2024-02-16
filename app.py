#!/usr/bin/env python3
from aws_cdk import App, Environment
from cdk_validator.cdk_validator_stack import CdkValidatorStack
from cdklabs import cdk_validator_cfnguard as cfn_guard


class CdkSampleRepo(App):
    """Create the CDK App for network management.

    Args:
        App (aws_cdk.App): CDK App class
    """
    def __init__(self, *args, **kwargs):
        """Initialise this ensemble class."""
        super().__init__(*args, **kwargs)
        """Create the actual CloudFormation stack tree."""
        self.default_env = Environment(
            account="12345678910",
            region="eu-central-1",
        )
        self.list_of_stacks = []

    def create_cfn_stacks(self):
        """Create CFN stacks."""
        zpa_stack = CdkValidatorStack(
            self,
            construct_id="CdkValidatorStack",
            stack_name=f"my-bucket-sample-stack",
        )
        self.list_of_stacks.append(zpa_stack)

if __name__ == "__main__":
    app = CdkSampleRepo(
        policy_validation_beta1=[
            cfn_guard.CfnGuardValidator(control_tower_rules_enabled=True)
        ]
    )
    app.create_cfn_stacks()
    app.synth()
