import boto3

s3 = boto3.resource('s3')

for image in ['sample.jpg', 'sample2.jpg']:
    s3.Bucket('storage-aws-recognition').upload_file(image, image)
    