import requests
import time

# Define the base URL of the load balancer
base_url = "http://localhost:5001"

# Define the endpoints of the load balancer
endpoints = ["/rep", "/add", "/rm", "/test", "/fail"]


# Define a function to simulate server failure
def simulate_server_failure(endpoint):
    url = base_url + endpoint
    try:
        if endpoint == "/add":
            # Simulate adding a server replica
            data = {"n": 1}
            response = requests.post(url, json=data)
        elif endpoint == "/rm":
            # Simulate removing a server replica
            data = {"n": 1}
            response = requests.delete(url, json=data)
        elif endpoint == "/fail":
            # Simulate a server failure
            data = {"hostname": "balancer-server1-1"}
            response = requests.post(url, json=data)
        else:
            response = requests.get(url)

        if response.status_code == 200:
            print(f"{url} is up and running.")
        else:
            print(f"{url} is down. Spawning a new server instance...")
            time.sleep(5)  # Simulate the time it takes to spawn a new instance
            print(f"New server instance of {url} has been spawned.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


# Test all endpoints
for endpoint in endpoints:
    simulate_server_failure(endpoint)