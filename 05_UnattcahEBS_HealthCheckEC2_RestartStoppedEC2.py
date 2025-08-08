 # simple python script that used by sre in daily basis for aws infra management

# Here’s a simple Python script that a Site Reliability Engineer (SRE) might use daily for AWS infrastructure 
# management. This example shows a script that:

# ✅ Checks the health of EC2 instances
# ✅ Restarts stopped instances
# ✅ Cleans up unattached EBS volumes (optional)

# These are basic but common tasks to maintain infrastructure health.

'''----------------------------##########################-------------------------------------'''

import boto3
from datetime import datetime

region = 'us-east-1'
ec2 = boto3.client('ec2', region_name=region)

def check_ec2_instances():
    print("Checking EC2 instance states...")
    response = ec2.describe_instance_status(IncludeAllInstances=True)
    
    for instance in response['InstanceStatuses']:
        instance_id = instance['InstanceId']
        state = instance['InstanceState']['Name']
        system_status = instance['SystemStatus']['Status']
        instance_status = instance['InstanceStatus']['Status']
        print(f"{instance_id} | State: {state}, Sys: {system_status}, Inst: {instance_status}")

        if state == 'stopped':
            print(f"Starting stopped instance: {instance_id}")
            ec2.start_instances(InstanceIds=[instance_id])

def clean_unattached_volumes():
    print("Cleaning unattached EBS volumes...")
    volumes = ec2.describe_volumes(Filters=[{'Name': 'status', 'Values': ['available']}])
    for vol in volumes['Volumes']:
        volume_id = vol['VolumeId']
        print(f"Deleting unattached volume: {volume_id}")
        ec2.delete_volume(VolumeId=volume_id)

def main():
    print(f"\n AWS Daily SRE Tasks - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    check_ec2_instances()
    clean_unattached_volumes()
    print("\n Daily checks completed.\n")

if __name__ == '__main__':
    main()




#🛡️ Safety Notes
#This script starts stopped EC2 instances and deletes unattached volumes, so run it only if you're sure that's intended behavior.

#Wrap deletion in --dry-run checks if needed for safety.

#🔁 Want to Automate Daily?
#You could:

#Schedule it via cron (Linux) or Task Scheduler (Windows)

#Deploy as a Lambda function

#Run in a CI/CD job like Jenkins or GitHub Actions