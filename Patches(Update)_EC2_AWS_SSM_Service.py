#### To patch (update) an AWS EC2 server using a Python script, you typically use the 

# AWS Systems Manager (SSM) service, which allows you to securely manage EC2 instances without 
# needing SSH access.

# Below is a Python script using boto3 to send a patch command to an EC2 instance via SSM.

# PREREQUISITES

# ✅ Prerequisites
# Your EC2 instance must:

# Be SSM-enabled (SSM Agent installed and running)

# Have an IAM Role attached with AmazonSSMManagedInstanceCore permission

# You must have:

# AWS CLI configured or ~/.aws/credentials set

# Python 3 and boto3 installed

### Python Script: Patch EC2 via SSM

import boto3
import time

# Replace these with your actual values
INSTANCE_ID = 'i-0abc123def4567890'
REGION = 'us-east-1'

ssm_client = boto3.client('ssm', region_name=REGION)

# Send command to patch instance
response = ssm_client.send_command(
    InstanceIds=[INSTANCE_ID],
    DocumentName='AWS-RunPatchBaseline',
    Parameters={
        'Operation': ['Install']
    },
    Comment='Applying patches using AWS-RunPatchBaseline',
)

command_id = response['Command']['CommandId']
print(f"Patch command sent. Command ID: {command_id}")

# Optionally wait and get status
time.sleep(5)

output = ssm_client.get_command_invocation(
    CommandId=command_id,
    InstanceId=INSTANCE_ID,
)

print("Status:", output['Status'])
print("Standard Output:", output.get('StandardOutputContent', ''))
print("Standard Error:", output.get('StandardErrorContent', ''))
