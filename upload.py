import boto3

upload = boto3.client("s3", region_name="ap-south-1")

upload.upload_file(
    r"D:\shruti.txt",
    "shruti12334455555",
    "test.txt"
)

print("File uploaded successfully!")