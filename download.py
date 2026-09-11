import boto3

download = boto3.client("s3", region_name="ap-south-1")

download.download_file(
    "shruti12334455555",
    "test.txt",
    r"D:\downloaded.txt"
)

print("File downloaded successfully!")