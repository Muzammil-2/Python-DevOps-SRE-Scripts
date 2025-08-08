# Scenario: Validating Disk Space Before Deployment
#Before deploying a new build, the script checks if sufficient disk space is available.
import shutil

threshold = 6  # Minimum free space in GB required for deployment
total, used, free = shutil.disk_usage("/")

free_gb = free // (2**30)  # Convert bytes to GB

if free_gb >= threshold:
    print("Sufficient disk space available. Proceeding with deployment.")
    # Code to trigger deployment
else:
    print(f"Insufficient disk space! Only {free_gb}GB free. Deployment aborted.")
