import boto3
demo=boto3.client("iam")
demo.create_user(
    UserName="sss"
)