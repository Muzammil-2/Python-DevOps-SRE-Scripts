#Logical Operators (and, or, not)
# Scenario: monitor service is healthy or not

cpu_usage = 70
memory_usage = 80

if cpu_usage < 80 and memory_usage < 90:
    print("service running healthy")
else:
    print("service unhealthy")