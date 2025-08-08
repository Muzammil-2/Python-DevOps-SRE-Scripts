#######  Use Case (Realistic for SRE in AWS):
# Monitor EC2 instance CPU usage.

# Send alerts if CPU usage exceeds threshold.

# OOP design to scale for more AWS services.


# Prerequisites:
# Boto3 installed (pip install boto3)

# AWS credentials configured (via ~/.aws/credentials or environment variables)

# Py script OOP + AWS Monitoring

import boto3
from datetime import datetime, timedelta

# Base class for AWS services
class AWSService:
    def __init__(self, region_name='us-east-1'):
        self.region = region_name
        self.cloudwatch = boto3.client('cloudwatch', region_name=region_name)

    def get_metric_statistics(self, namespace, metric_name, dimensions, stat='Average', period=300):
        end_time = datetime.utcnow()
        start_time = end_time - timedelta(minutes=10)

        response = self.cloudwatch.get_metric_statistics(
            Namespace=namespace,
            MetricName=metric_name,
            Dimensions=dimensions,
            StartTime=start_time,
            EndTime=end_time,
            Period=period,
            Statistics=[stat]
        )
        datapoints = response['Datapoints']
        if not datapoints:
            return None
        return sorted(datapoints, key=lambda x: x['Timestamp'])[-1][stat]


# Subclass for EC2-specific monitoring
class EC2Monitor(AWSService):
    def __init__(self, instance_id, threshold=70, region_name='us-east-1'):
        super().__init__(region_name)
        self.instance_id = instance_id
        self.threshold = threshold

    def check_cpu_utilization(self):
        cpu = self.get_metric_statistics(
            namespace='AWS/EC2',
            metric_name='CPUUtilization',
            dimensions=[{'Name': 'InstanceId', 'Value': self.instance_id}],
        )
        return cpu


# Alert Manager class
class AlertManager:
    def __init__(self):
        self.alerts = []

    def send_alert(self, service_name, metric_value):
        message = f"⚠️ ALERT: {service_name} CPU usage high: {metric_value:.2f}%"
        self.alerts.append(message)
        print(message)

    def show_alerts(self):
        print("\n--- Alert Summary ---")
        for alert in self.alerts:
            print(alert)


# Monitoring controller
class CloudMonitor:
    def __init__(self, services, alert_manager):
        self.services = services
        self.alert_manager = alert_manager

    def run_checks(self):
        for service in self.services:
            cpu = service.check_cpu_utilization()
            print(f"[{service.instance_id}] CPU Usage: {cpu}%")
            if cpu and cpu > service.threshold:
                self.alert_manager.send_alert(service.instance_id, cpu)


# Example usage
if __name__ == "__main__":
    # Add EC2 instances to monitor
    ec2_1 = EC2Monitor(instance_id='i-0123456789abcdef0', threshold=60)
    ec2_2 = EC2Monitor(instance_id='i-0abcdef1234567890', threshold=75)

    # Initialize alerting
    alert_mgr = AlertManager()

    # Run monitoring
    monitor = CloudMonitor([ec2_1, ec2_2], alert_mgr)
    monitor.run_checks()
    alert_mgr.show_alerts()

# Example Output

[i-0123456789abcdef0] CPU Usage: 65.2%
⚠️ ALERT: i-0123456789abcdef0 CPU usage high: 65.2%
[i-0abcdef1234567890] CPU Usage: 45.7%

--- Alert Summary ---
⚠️ ALERT: i-0123456789abcdef0 CPU usage high: 65.2%


# Monitor other AWS resources like RDS, Lambda, or ALB.