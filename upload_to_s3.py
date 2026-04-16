import os
import boto3

def upload_csv():
    bucket_name = os.environ.get("bucketqoutes100")
    file_path = "output/quotes.csv"
    s3_key = "quotes/quotes.csv"

    if not bucket_name:
        raise ValueError("bucketqoutes100 is not set")

    s3 = boto3.client("s3")
    s3.upload_file(file_path, bucket_name, s3_key)

    print(f"Uploaded {file_path} to s3://{bucket_name}/{s3_key}")

if __name__ == "__main__":
    upload_csv()