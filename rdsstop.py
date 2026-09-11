import boto3

rds = boto3.client("rds", region_name="ap-south-1")

response = rds.stop_db_instance(
    DbInstanceIdentifier="demo"
)

print("Stop request sent successfully.")
print("DB status:", response["DBInstance"]["DBInstanceStatus"])