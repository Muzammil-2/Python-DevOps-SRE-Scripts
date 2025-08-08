# Scenario: Validating User Input
#A script to verify if the provided username has the necessary privileges to run a deployment.
user_role = "developer"  # Example roles: "admin", "developer"

if user_role == "admin":
    print("User has sufficient privileges. Proceeding with deployment.")
    # Deployment code
else:
    print("User does not have sufficient privileges to deploy!")
