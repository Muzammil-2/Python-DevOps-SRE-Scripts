# Bitwise Operators (&, |, ^, ~, <<, >>)
# Scenario: Managing file permissions in octal format.

permissions = 0o755  # File permission in octal
read_write_execute = 0o700

# Applying read, write, and execute permissions
new_permissions = permissions | read_write_execute  # `|` operator for bitwise OR
print(oct(new_permissions))
