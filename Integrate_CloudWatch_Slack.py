# script that also checks CloudWatch alarms  integrates ?

###  Features
# 1 Checks the state of CloudWatch alarms (e.g., ALARM, OK, INSUFFICIENT_DATA)

# 2 Filters for ALARM state alarms for EC2 instances

# 3 Reboots affected EC2 instances

# 4 Sends a Slack alert for each action taken

### pip install boto3 requests
# aws credntials configure

#🐍 Python Script: CloudWatch Integrated EC2 Health Check

import boto3
import logging
import requests
import time

# ========== Configuration ==========
REGION = 'us-west-2'
SLACK_WEBHOOK_URL = 'https://hooks.slack.com/services/your/webhook/url'
TAG_KEY = 'Environment'
TAG_VALUE = 'Production'

# ========== Logging ==========
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# ========== AWS Clients ==========
ec2_client = boto3.client('ec2', region_name=REGION)
cw_client = boto3.client('cloudwatch', region_name=REGION)

# ========== Slack Notification ==========
def send_slack_alert(message: str):
    response = requests.post(SLACK_WEBHOOK_URL, json={'text': message})
    if response.status_code != 200:
        logging.error(f"Slack notification failed: {response.text}")

# ========== Get EC2 Instances ==========
def get_instance_ids_by_tag():
    logging.info("Fetching EC2 instances with specific tags...")
    response = ec2_client.describe_instances(
        Filters=[
            {'Name': f'tag:{TAG_KEY}', 'Values': [TAG_VALUE]},
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
    )
    instance_ids = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])
    return instance_ids

# ========== Get CloudWatch Alarms ==========
def get_alarms_for_instance(instance_id):
    alarms_in_alarm = []
    paginator = cw_client.get_paginator('describe_alarms')
    for page in paginator.paginate(StateValue='ALARM'):
        for alarm in page['MetricAlarms']:
            # Check if this alarm is associated with this instance
            for dimension in alarm['Dimensions']:
                if dimension['Name'] == 'InstanceId' and dimension['Value'] == instance_id:
                    alarms_in_alarm.append(alarm['AlarmName'])
    return alarms_in_alarm

# ========== Reboot Instance ==========
def reboot_instance(instance_id, alarm_names):
    logging.warning(f"Rebooting instance {instance_id} due to alarms: {alarm_names}")
    ec2_client.reboot_instances(InstanceIds=[instance_id])
    send_slack_alert(f":rotating_light: Rebooted EC2 instance `{instance_id}` due to alarms: {', '.join(alarm_names)}")

# ========== Main ==========
def main():
    instance_ids = get_instance_ids_by_tag()

    for instance_id in instance_ids:
        alarms = get_alarms_for_instance(instance_id)
        if alarms:
            reboot_instance(instance_id, alarms)
            time.sleep(3)  # avoid API throttling
        else:
            logging.info(f"No alarms for instance {instance_id}")

    logging.info("CloudWatch alarm check completed.")

if __name__ == "__main__":
    main()


###  Real-World Considerations
# 1 Replace reboot logic with more careful decision-making in production (e.g., human confirmation, or auto-remediation only on known-safe alarms).

# 2 You could expand this by tagging alarms to group critical vs. non-critical types.

# 3 Use AWS Systems Manager Automation for sophisticated workflows.

# 4 Logs can be shipped to CloudWatch Logs for audit trail.