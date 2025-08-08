#  Environment Configuration
#  You can use sets to check for configuration discrepancies across environments.

dev_packages = {"nginx", "mysql", "redis"}
prod_packages = {"nginx", "mysql", "rabbitmq"}

# Find missing packages in production
missing_in_prod = dev_packages - prod_packages
print(missing_in_prod)  # Output: {'redis'}
