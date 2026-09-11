
import boto3

data = boto3.client("ec2", region_name="ap-south-1")

subnet = data.create_subnet(
    VpcId="vpc-08744eb7da0143cdc",
    CidrBlock="10.0.1.0/24",
    TagSpecifications=[
        {
            "ResourceType": "subnet",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "shruti-subnet"
                }
            ]
        }
    ]
)

print("Subnet created:", subnet["Subnet"]["SubnetId"])