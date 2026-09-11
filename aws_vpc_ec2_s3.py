import boto3

aws_access_key_id = "AKIADEMO1234567890"
aws_secret_access_key = "DemoSecretKey1234567890abcdef"
region = "ap-south-1"

ec2 = boto3.client(
    "ec2",
    region_name=region,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

s3 = boto3.client(
    "s3",
    region_name=region,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

vpc = ec2.create_vpc(
    CidrBlock="10.0.0.0/16"
)

vpc_id = vpc["Vpc"]["VpcId"]
print("VPC:", vpc_id)

ec2.modify_vpc_attribute(
    VpcId=vpc_id,
    EnableDnsSupport={"Value": True}
)

ec2.modify_vpc_attribute(
    VpcId=vpc_id,
    EnableDnsHostnames={"Value": True}
)

subnet = ec2.create_subnet(
    VpcId=vpc_id,
    CidrBlock="10.0.1.0/24",
    AvailabilityZone="ap-south-1a"
)

subnet_id = subnet["Subnet"]["SubnetId"]
print("Subnet:", subnet_id)

igw = ec2.create_internet_gateway()

igw_id = igw["InternetGateway"]["InternetGatewayId"]
print("Internet Gateway:", igw_id)

ec2.attach_internet_gateway(
    InternetGatewayId=igw_id,
    VpcId=vpc_id
)

route_table = ec2.create_route_table(
    VpcId=vpc_id
)

route_table_id = route_table["RouteTable"]["RouteTableId"]
print("Route Table:", route_table_id)

ec2.create_route(
    RouteTableId=route_table_id,
    DestinationCidrBlock="0.0.0.0/0",
    GatewayId=igw_id
)

ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id
)

security_group = ec2.create_security_group(
    GroupName="demo-ec2-sg",
    Description="Demo EC2 Security Group",
    VpcId=vpc_id
)

security_group_id = security_group["GroupId"]
print("Security Group:", security_group_id)

ec2.authorize_security_group_ingress(
    GroupId=security_group_id,
    IpPermissions=[
        {
            "IpProtocol": "tcp",
            "FromPort": 22,
            "ToPort": 22,
            "IpRanges": [
                {"CidrIp": "0.0.0.0/0"}
            ]
        },
        {
            "IpProtocol": "tcp",
            "FromPort": 80,
            "ToPort": 80,
            "IpRanges": [
                {"CidrIp": "0.0.0.0/0"}
            ]
        }
    ]
)

ec2.modify_subnet_attribute(
    SubnetId=subnet_id,
    MapPublicIpOnLaunch={"Value": True}
)

key_name = "demo-key"
ami_id = "ami-0f918f7e67a3323f0"

instance = ec2.run_instances(
    ImageId=ami_id,
    InstanceType="t2.micro",
    MinCount=1,
    MaxCount=1,
    KeyName=key_name,
    NetworkInterfaces=[
        {
            "SubnetId": subnet_id,
            "DeviceIndex": 0,
            "AssociatePublicIpAddress": True,
            "Groups": [security_group_id]
        }
    ]
)

instance_id = instance["Instances"][0]["InstanceId"]
print("EC2:", instance_id)

bucket_name = "demo-boto3-bucket-20260911-12345"

s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        "LocationConstraint": region
    }
)

print("S3 Bucket:", bucket_name)

file_path = r"D:\AWS\test.txt"

s3.upload_file(
    file_path,
    bucket_name,
    "test.txt"
)

print("File uploaded successfully")