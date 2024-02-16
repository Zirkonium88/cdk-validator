from aws_cdk import Stack, aws_s3 as s3
from constructs import Construct


class CdkValidatorStack(Stack):
    """Create the actual deployment in each AWS account.

    Args:
        Stage (Stage): cdk Class stage
    """

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        **kwargs
    ) -> None:
        """Initialise CDK stack class."""
        super().__init__(scope, construct_id, **kwargs)
        """Create the actual CloudFormation stack."""
        s3.Bucket(
            self,
            id="MyBucket",
            block_public_access=s3.BlockPublicAccess(
                block_public_acls=True,
                block_public_policy=True,
                ignore_public_acls=True,
                restrict_public_buckets=True,
            ),
            versioned=True,
            enforce_ssl=True,
            encryption=s3.BucketEncryption.KMS_MANAGED,
        )
