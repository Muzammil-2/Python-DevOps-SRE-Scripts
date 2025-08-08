# write a python script example of daily used by SRE Engineer for interacting aws cloud infra

# Here is an example of a daily-use Python script that an SRE (Site Reliability Engineer) might use to interact with AWS infrastructure, such as checking EC2 instance health, restarting unhealthy instances, and sending a Slack alert.

# This script uses:

# 1. Boto3 to interact with AWS.

# 2. Slack webhook for alerting.

# 3. Basic filtering for EC2 instances with a specific tag (e.g., "Environment=Production").

# Prerequisites:
# pip install boto3 requests
# Ensure your AWS credentials are set via environment variables, IAM role, or AWS config file.

import boto3
import requests
import logging

# ========== Configurations ==========
REGION = 'us-west-2'
TAG_FILTER = {'Key': 'Environment', 'Value': 'Production'}
SLACK_WEBHOOK_URL = 'https://hooks.slack.com/services/your/webhook/url'

# ========== Logging ==========
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# ========== AWS Clients ==========
ec2 = boto3.client('ec2', region_name=REGION)

# ========== Slack Notification ==========
def send_slack_alert(message: str):
    payload = {'text': message}
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)
    if response.status_code != 200:
        logging.error(f"Slack notification failed: {response.text}")

# ========== Health Check Function ==========
def get_instances():
    logging.info("Fetching EC2 instances...")
    response = ec2.describe_instances(
        Filters=[
            {'Name': f'tag:{TAG_FILTER["Key"]}', 'Values': [TAG_FILTER["Value"]]},
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
    )

    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append({
                'InstanceId': instance['InstanceId'],
                'State': instance['State']['Name'],
                'InstanceType': instance['InstanceType'],
                'PrivateIpAddress': instance.get('PrivateIpAddress', 'N/A')
            })
    return instances

def restart_instance(instance_id):
    logging.warning(f"Rebooting instance {instance_id}")
    ec2.reboot_instances(InstanceIds=[instance_id])
    send_slack_alert(f":warning: Rebooted EC2 instance `{instance_id}` due to health check failure.")

def main():
    instances = get_instances()
    for instance in instances:
        logging.info(f"Checking instance {instance['InstanceId']} ({instance['PrivateIpAddress']})")
        
        # Simulate a basic "health check" — in reality, use CloudWatch or custom scripts
        unhealthy = instance['PrivateIpAddress'] == 'N/A'  # For example purposes

        if unhealthy:
            restart_instance(instance['InstanceId'])

    logging.info("Health check completed.")

if __name__ == "__main__":
    main()

### What This Script Does
# 1 Lists all running EC2 instances with the Environment=Production tag.

# 2 Performs a dummy health check (can be replaced with real metrics).

# 3 Reboots any instance deemed "unhealthy".

# 4 Sends a Slack alert if any instance is rebooted.

### Notes for Real Usage
# Integrate with CloudWatch Alarms, StatusChecks, or SSM RunCommand for actual health verification.

# Add exception handling and CloudTrail logging if running in production.

# Consider AWS Lambda or cron jobs (via EventBridge) to automate it on a schedule.
