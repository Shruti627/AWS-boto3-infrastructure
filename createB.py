import boto3

awsbucket = boto3.client("s3", region_name="ap-south-1")

awsbucket.create_bucket(
    Bucket="shruti1233445555534566",
    CreateBucketConfiguration={
        "LocationConstraint": "ap-south-1"
    }
)

