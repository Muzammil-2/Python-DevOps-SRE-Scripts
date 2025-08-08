# Tracking Service Ports
# You might use a dictionary to track services and their associated ports.

service_ports = {
    "nginx": 80,
    "mysql": 3306,
    "redis": 6379,
}

# Adding a new service
service_ports["rabbitmq"] = 5672

service_ports["ssh"] = 22

print(type(service_ports))

