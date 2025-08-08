import boto3

iam = boto3.client('iam')    # This line creates a client (connection) to the AWS IAM service.

def list_iam_users():
    response = iam.list_users()   ##This asks AWS to give you a list of all IAM users in your account.
    for user in response['Users']:  # Loops through each user in the list of users returned.
        print(f"Username: {user['UserName']} | ARN: {user['Arn']}")

list_iam_users()
