import boto3

def get_s3_bucket_sizes():
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()
    for bucket in buckets['Buckets']:
        total_size = 0
        objects = s3.list_objects_v2(Bucket=bucket['Name'])
        if 'Contents' in objects:
            for obj in objects['Contents']:
                total_size += obj['Size']
        print(f"{bucket['Name']}: {total_size / (1024 ** 2):.2f} MB")
