import paramiko

class ServerDeployer:
    # Class Attributes (Common for all instances)
    HOST = "your-ec2-public-ip"
    USER = "ec2-user"
    PRIVATE_KEY_PATH = "path/to/your/private-key.pem"
    DOCKER_IMAGE = "your-dockerhub-username/your-app:latest"
    CONTAINER_NAME = "your-app-container"

    def __init__(self):
        """ Initialize SSH Client """
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        """ Connect to EC2 Instance """
        try:
            print(f"Connecting to {self.HOST}...")
            self.ssh.connect(self.HOST, username=self.USER, key_filename=self.PRIVATE_KEY_PATH)
            print("Connection successful.")
        except Exception as e:
            print(f"Connection failed: {e}")

    def deploy(self):
        """ Deploy Docker Container """
        commands = [
            f"docker pull {self.DOCKER_IMAGE}",
            f"docker stop {self.CONTAINER_NAME} || true",
            f"docker rm {self.CONTAINER_NAME} || true",
            f"docker run -d --name {self.CONTAINER_NAME} -p 80:80 {self.DOCKER_IMAGE}"
        ]

        for cmd in commands:
            print(f"Executing: {cmd}")
            stdin, stdout, stderr = self.ssh.exec_command(cmd)
            print(stdout.read().decode(), stderr.read().decode())

        print("Deployment completed.")

    def close(self):
        """ Close SSH Connection """
        self.ssh.close()
        print("Connection closed.")

# Usage Example
if __name__ == "__main__":
    deployer = ServerDeployer()
    deployer.connect()
    deployer.deploy()
    deployer.close()
