# purpose of using request for health checks
''' 1. check if service is reachable (UP/DOWN)
    2. Verify response code 200 is ok
    3. Measure response time if 
    4. Log or alert based on service status'''
import requests

def check_health(url):
    try:
        response = requests.get(url,timeout=5)
        if response.status_code == 200:
            print(f"service at {url} is UP")
        else:
            print(f"service at {url} is DOWN Status: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Service at {url} is DOWN Error: {e}")

# check a few services
check_health("https://json.typcode.com/posts")
check_health("https://url.com")
          