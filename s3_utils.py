import boto3
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME

s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

def upload_file_to_s3(file_name, bucket_name=AWS_STORAGE_BUCKET_NAME, object_name=None):
    if object_name is None:
        object_name = file_name

    try:
        s3.upload_file(file_name, bucket_name, object_name)
        print(f"File {file_name} uploaded to {bucket_name}/{object_name}")
    except Exception as e:
        print(f"Error uploading file: {e}")

def download_file_from_s3(object_name, bucket_name=AWS_STORAGE_BUCKET_NAME, file_name=None):
    if file_name is None:
        file_name = object_name

    try:
        s3.download_file(bucket_name, object_name, file_name)
        print(f"File {object_name} downloaded from {bucket_name} to {file_name}")
    except Exception as e:
        print(f"Error downloading file: {e}")
