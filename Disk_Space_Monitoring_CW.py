# Disk Space Monitoring (using CloudWatch + SNS for alerts)

import boto3

cloudwatch = boto3.client('cloudwatch')

def create_disk_space_alarm(instance_id, sns_topic_arn):
    cloudwatch.put_metric_alarm(
        AlarmName='DiskSpaceLow',
        MetricName='DiskSpaceUtilization',
        Namespace='System/Linux',
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
        Statistic='Average',
        Period=300,
        EvaluationPeriods=1,
        Threshold=80.0,
        ComparisonOperator='GreaterThanThreshold',
        AlarmActions=[sns_topic_arn],
        Unit='Percent'
    )
    print(f"Alarm created for instance {instance_id}")
