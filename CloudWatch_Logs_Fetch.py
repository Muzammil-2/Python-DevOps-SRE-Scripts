import boto3

client = boto3.client('logs')

def get_log_events(log_group, log_stream):
    response = client.get_log_events(
        logGroupName=log_group,
        logStreamName=log_stream,
        startFromHead=True
    )
    for event in response['events']:
        print(event['message'])
