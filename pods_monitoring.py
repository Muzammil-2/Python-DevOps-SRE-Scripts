from kubernetes import client, config

def monitor_k8s_pods(namespace="default"):
    """
    Monitors the status of Kubernetes pods in a given namespace.
    Alerts if any pod is in a non-running state.
    """
    try:
        # Load the Kubernetes configuration (from ~/.kube/config or in-cluster)
        config.load_kube_config()

        v1 = client.CoreV1Api()
        pods = v1.list_namespaced_pod(namespace)

        alert_pods = []

        for pod in pods.items:
            pod_name = pod.metadata.name
            pod_status = pod.status.phase

            if pod_status not in ["Running", "Succeeded"]:
                alert_pods.append((pod_name, pod_status))

        if alert_pods:
            print("⚠️ ALERT: Some pods are not healthy!")
            for pod_name, status in alert_pods:
                print(f"  ❌ Pod '{pod_name}' is in '{status}' state")
        else:
            print("✅ All pods are running normally.")

    except Exception as e:
        print(f"Error while monitoring pods: {e}")

# Call the function 
monitor_k8s_pods(namespace="default")




# How It Works:
# Loads Kubernetes configuration.
# Fetches all pods in the specified namespace.
# Checks the status of each pod.
# Alerts if any pod is in a failed, pending, or unknown state.



# Possible Enhancements:
# ✅ Send alerts via Slack, Email, or PagerDuty if any pod is failing.
# ✅ Automate this script using a CronJob or Kubernetes Job.
# ✅ Extend it to monitor multiple namespaces or services.

# Would you like me to modify this script for another real-world DevOps scenario, such as CI/CD 
# automation or AWS resource monitoring?