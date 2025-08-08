# In a real scenario, you might combine dictionaries and sets for more complex tasks.

# Example: Server Role Mapping
roles = {
    "web": {"192.168.1.10", "192.168.1.11"},
    "db": {"192.168.1.20"},
    "cache": {"192.168.1.30"},
}

# Add a new server to the 'web' role
roles["web"].add("192.168.1.15")

# Check servers common to 'web' and 'cache' roles
common_servers = roles["web"] & roles["cache"]
print(common_servers)  # Output: set() (empty set if no overlap)
