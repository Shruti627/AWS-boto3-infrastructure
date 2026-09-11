import boto3
ec2demo=boto3.client("ec2",region_name="us-east-1")
ec2demo.run_instances(
    ImageId="ami-0bdc7d025135d7b49",
    InstanceType="t3.micro",
    MinCount=1,
    MaxCount=1
)

