import requests

def push_metric_to_prometheus(job_name, instance, metric_name, value):
    payload = f"{metric_name} {value}\n"
    url = f"http://localhost:9091/metrics/job/{job_name}/instance/{instance}"
    response = requests.post(url, data=payload)
    print(f"Status: {response.status_code}")
