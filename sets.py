#Sets are useful for storing unique elements and performing operations like unions or intersections.

# Unique Hosts in a Cluster
# Sets can help ensure no duplicate entries are present in a cluster of servers.

cluster_a = {"192.168.1.10", "192.168.1.11", "192.168.1.12"}
cluster_b = {"192.168.1.12", "192.168.1.13", "192.168.1.14"}

# Find common hosts
common_hosts = cluster_a & cluster_b
print(common_hosts)  # Output: {'192.168.1.12'}

# Get all unique hosts
all_hosts = cluster_a | cluster_b
print(all_hosts)  # Output: {'192.168.1.10', '192.168.1.11', '192.168.1.12', '192.168.1.13', '192.168.1.14'}
