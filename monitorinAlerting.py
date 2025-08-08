import random
import time

# Base class for a service
class Service:
    def __init__(self, name, cpu_threshold=80, memory_threshold=75):
        self.name = name
        self.cpu_threshold = cpu_threshold
        self.memory_threshold = memory_threshold

    def check_cpu_usage(self):
        usage = random.randint(0, 100)
        print(f"[{self.name}] CPU Usage: {usage}%")
        return usage

    def check_memory_usage(self):
        usage = random.randint(0, 100)
        print(f"[{self.name}] Memory Usage: {usage}%")
        return usage

    def is_healthy(self):
        cpu = self.check_cpu_usage()
        memory = self.check_memory_usage()
        return cpu < self.cpu_threshold and memory < self.memory_threshold


# Alerting mechanism
class AlertManager:
    def __init__(self):
        self.alerts = []

    def send_alert(self, service_name, issue):
        alert_msg = f"ALERT: {service_name} - {issue}"
        self.alerts.append(alert_msg)
        print(alert_msg)

    def show_alerts(self):
        print("\n--- Alert Summary ---")
        for alert in self.alerts:
            print(alert)


# Child class for a specific service type
class WebService(Service):
    def check_http_response(self):
        # Simulated response time
        response_time = random.randint(50, 500)  # in ms
        print(f"[{self.name}] HTTP Response Time: {response_time}ms")
        if response_time > 300:
            return False, response_time
        return True, response_time

    def is_healthy(self):
        base_health = super().is_healthy()
        http_ok, resp_time = self.check_http_response()
        return base_health and http_ok


# Monitor class to orchestrate everything
class ServiceMonitor:
    def __init__(self, services, alert_manager):
        self.services = services
        self.alert_manager = alert_manager

    def run_checks(self):
        for service in self.services:
            print(f"\nChecking {service.name}...")
            if not service.is_healthy():
                self.alert_manager.send_alert(service.name, "Health check failed")


# Example usage
if __name__ == "__main__":
    # Simulated services
    service1 = WebService("User-Service")
    service2 = WebService("Payment-Service", cpu_threshold=70, memory_threshold=65)

    # Alert system
    alert_mgr = AlertManager()

    # Monitor setup
    monitor = ServiceMonitor([service1, service2], alert_mgr)

    # Run simulated checks
    monitor.run_checks()
    alert_mgr.show_alerts()


############################# OutPut  ######################################
sql......
Checking User-Service...
[User-Service] CPU Usage: 75%
[User-Service] Memory Usage: 80%
[User-Service] HTTP Response Time: 310ms
ALERT: User-Service - Health check failed

Checking Payment-Service...
[Payment-Service] CPU Usage: 60%
[Payment-Service] Memory Usage: 50%
[Payment-Service] HTTP Response Time: 280ms

--- Alert Summary ---
ALERT: User-Service - Health check failed
