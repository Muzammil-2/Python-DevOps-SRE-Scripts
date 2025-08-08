import boto3

ec2 = boto3.client('ec2')

def terminate_unhealthy_instances():
    instances = ec2.describe_instance_status(IncludeAllInstances=True)
    for status in instances['InstanceStatuses']:
        if status['InstanceStatus']['Status'] != 'ok':
            instance_id = status['InstanceId']
            print(f"Terminating unhealthy instance: {instance_id}")
            ec2.terminate_instances(InstanceIds=[instance_id])
