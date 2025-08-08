# Scenario: Deciding Notification Channel
#A script to send alerts via email or Slack based on the severity level of a monitoring alert.

alert_severity = "high"  # Possible values: "low", "medium", "high"

if alert_severity == "high":
    print("Sending alert to Slack channel.")
    # Code to send Slack alert
else:
    print("Sending alert via email.")
    # Code to send email alert
