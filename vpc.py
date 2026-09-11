import boto3

data = boto3.client("ec2", region_name="ap-south-1")

data.create_vpc(
    CidrBlock="10.0.0.0/16",
    TagSpecifications=[
        {
            "ResourceType": "vpc",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "shruti"
                }
            ]
        }
    ]
)