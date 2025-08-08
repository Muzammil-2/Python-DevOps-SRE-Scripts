# Python operators are frequently used in DevOps engineering tasks to streamline processes, 
# manipulate data, and automate workflows. Here are examples of how various types of operators are 

# 1. Arithmetic Operators (+, -, *, /, %, **, //)
# scenario: monitoring disk space
import shutil

total, used, free = shutil.disk_usage("/")
percentage_used = (used / total) * 100  # `/` for division, `*` for multiplication
print(f"Disk Usage: {percentage_used:.2f}%")
 
