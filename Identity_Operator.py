# Identity Operators (is, is not)
# Scenario: Checking if an object is None.

log_file = None

if log_file is None:
    print("No log file provided. Using default.")
else:
    print(f"Processing log file: {log_file}")
