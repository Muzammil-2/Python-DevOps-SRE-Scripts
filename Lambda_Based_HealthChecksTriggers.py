import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    response = ec2.describe_instance_status(IncludeAllInstances=True)
    for instance in response['InstanceStatuses']:
        if instance['InstanceStatus']['Status'] != 'ok':
            ec2.reboot_instances(InstanceIds=[instance['InstanceId']])
            print(f"Rebooted instance {instance['InstanceId']}")
