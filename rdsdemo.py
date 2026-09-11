import boto3
rds=boto3.client("rds",region_name="ap-south-1")
rds.create_db_instance(
    DbInstanceIdentifier="shrutidemo",
    DbInstanceClass="db.t4g.micro",
    Engine="mysql",
    MasterUsername="Root",
    MasterUserPassword="Root1234",
    AllocatedStorage=20
)