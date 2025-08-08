''' Here Python script that demonstrates OOP Object-Oriented-Programming in role of DevOps Engineer
    it include managing deployment for different environments (e.g. Dev,Stage and Production)
    tasks like starting a deployment,checking server health and rolling back if needed '''

class Environment:
    def __init__(self,name,servers):
        self.name = name
        self.servers = servers
        self.deployed_version = None
    def deploy(self, version):
        self.deployed_version = version
        for server in self.servers:
            print(f"Deploying to {server} ")

print(f"[{self.name.upper()}] Deploying version {version} to {len(self.servers)} servers ...")
print(f"[{self.name.upper()}] Deploying version {version} complete. \n")  

    def check_health(self):
print(f"[{self.name.upper()}] checking health check of servers...")

         for server in self.servers:
            print(f"- server {server} is healthy")
print(f"[{self.name.upper()}] all servers are healthy servers...\n")

    def rollback(self,previous_version):
 
    
       