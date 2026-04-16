import boto3

file_path = "output/quotes.csv"
bucket_name = "bucketqoutes100"
s3_key = "output/quotes.csv"

s3 = boto3.client("s3")
s3.upload_file(file_path, bucket_name, s3_key)

print("Upload successful")