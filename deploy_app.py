import paramiko

# Define SSH and Deployment Details
HOST = "your-ec2-public-ip"
USER = "ec2-user"
PRIVATE_KEY_PATH = "path/to/your/private-key.pem"
DOCKER_IMAGE = "your-dockerhub-username/your-app:latest"
CONTAINER_NAME = "your-app-container"

# Define Commands to Run on EC2
commands = [
    f"docker pull {DOCKER_IMAGE}",
    f"docker stop {CONTAINER_NAME} || true",
    f"docker rm {CONTAINER_NAME} || true",
    f"docker run -d --name {CONTAINER_NAME} -p 80:80 {DOCKER_IMAGE}"
]

def deploy():
    """ Connects to EC2 and executes deployment commands """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        print("Connecting to EC2 instance...")
        ssh.connect(HOST, username=USER, key_filename=PRIVATE_KEY_PATH)
        
        for cmd in commands:
            print(f"Executing: {cmd}")
            stdin, stdout, stderr = ssh.exec_command(cmd)
            print(stdout.read().decode(), stderr.read().decode())
        
        print("Deployment completed successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        ssh.close()

if __name__ == "__main__":
    deploy()
