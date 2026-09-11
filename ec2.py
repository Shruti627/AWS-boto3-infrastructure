import boto3

data = boto3.client("ec2", region_name="ap-south-1")


res=data.run_instances(
    ImageId="ami-035827357e3c7e810",
    InstanceType="t3.micro",
    MinCount=1,
    MaxCount=1,
    SubnetId="subnet-0814e3e65b8ae2d39",
    SecurityGroupIds=["sg-076c0a0f8c58b621a"]

    
)

print(res)