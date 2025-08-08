# Scenario: Checking Service Status
#A script that checks if a service is running and restarts it if it is not.

import os

service_name = "nginx"

status = os.system(f"systemctl is-active --quiet {service_name}")

if status == 0:  # Exit code 0 means the service is running
    print(f"{service_name} is running.")
else:
    print(f"{service_name} is not running. Attempting to restart...")
    os.system(f"systemctl restart {service_name}")
