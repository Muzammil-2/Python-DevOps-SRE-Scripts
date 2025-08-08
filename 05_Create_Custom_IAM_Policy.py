import json

def create_custom_policy(name):
    policy_document = {
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Action": ["s3:ListBucket"],
            "Resource": ["arn:aws:s3:::example-bucket"]
        }]
    }

    response = iam.create_policy(
        PolicyName=name,
        PolicyDocument=json.dumps(policy_document)
    )
    print(f"Policy created: {response['Policy']['Arn']}")

create_custom_policy("S3ListBucketPolicy")
