import boto3

data = boto3.client("ec2", region_name="ap-south-1")

# Create Route Table
response = data.create_route_table(
    VpcId="vpc-08744eb7da0143cdc"
)

route_table_id = response["RouteTable"]["RouteTableId"]

print("Route Table created:", route_table_id)


# Create Internet Route
data.create_route(
    RouteTableId=route_table_id,
    DestinationCidrBlock="0.0.0.0/0",
    GatewayId="igw-01661382c76be55c1"
)

print("Internet route created")