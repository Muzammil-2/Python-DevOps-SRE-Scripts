# Membership Operators (in, not in)
# Scenario: Checking whether a server is in the list of monitored servers.

monitored_servers = ["server1", "server2", "server3"]
current_server = "server4"

if current_server in monitored_servers:
    print(f"{current_server} is being monitored.")
else:
    print(f"{current_server} is not monitored.")
