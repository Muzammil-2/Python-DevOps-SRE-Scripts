# Storing Server Metadata
# A dictionary can be used to store details about servers.
servers = {
    "web-server-1": {"IP": "192.168.1.10", "OS": "Ubuntu", "Status": "Active"},
    "db-server-1": {"IP": "192.168.1.20", "OS": "CentOS", "Status": "Active"},
    "cache-server-1": {"IP": "192.168.1.30", "OS": "Debian", "Status": "Inactive"},
}

# Accessing data for a specific server
print(servers["cache-server-1"]["Status"])  # Output: 192.168.1.10
print(servers["db-server-1"]["IP"])