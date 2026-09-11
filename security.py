import boto3

ec2 = boto3.client("ec2", region_name="ap-south-1")

response = ec2.create_security_group(
    GroupName="shruti-sg",
    Description="Security group for shruti EC2",
    VpcId="vpc-08744eb7da0143cdc"
)

print("Security Group ID:", response["GroupId"])