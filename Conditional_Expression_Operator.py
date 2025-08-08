#  Conditional Expression (?: equivalent in Python)
#  Scenario: Choosing deployment strategy
deployment_env = "production"
strategy = "blue-green" 

if deployment_env == "production":
     print(f"Deployment strategy: {strategy}")
else:
     print("rolling")

