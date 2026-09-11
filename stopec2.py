import boto3

stopdemo = boto3.client("ec2", region_name="us-east-1")

response = stopdemo.stop_instances(
    InstanceIds=["i-0a5511975c5d34e4e"]
)

print(response)