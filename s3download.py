import boto3
import botocore

BUCKET_NAME = 'storage-aws-recognition'
BUCKET_FILE_NAME = 'sample.jpg'
LOCAL_FILE_NAME = 'downloaded.jpg'

def download_s3_file():
    s3 = boto3.client('s3')
    s3.download_file(BUCKET_NAME, BUCKET_FILE_NAME, LOCAL_FILE_NAME)

download_s3_file()