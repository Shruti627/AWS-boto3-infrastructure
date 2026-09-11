import boto3

data = boto3.client("ec2", region_name="ap-south-1")

response = data.create_internet_gateway()

igw_id = response["InternetGateway"]["InternetGatewayId"]

print("Internet Gateway created:", igw_id)