# backup from local to s3
# boto3 lib use to AWS tasks using python
# install awscli
import boto3

s3 = boto3.resource("s3")

def show_buckets(s3):
    for bucket in s3.buckets.all():
        print (bucket.name)
def create_bucket(s3):
    s3.create_bucket(Bucket='python_backup',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1',
    },)

    print("bucket successfully created")