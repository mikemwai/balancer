import requests
import time
import os
import random
import socket
import json


# Function to simulate server failure
def simulate_server_failure(server_id):
    os.system(f'docker stop server{server_id}')


# Function to check the health of the servers
def check_server_health(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return True
    except:
        return False


def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0


# Function to spawn a new server instance
def spawn_new_server(server_id):
    # Remove any existing container with the same name
    os.system(f'docker rm -f server{server_id}')
    # Check if the port is in use
    if is_port_in_use(5001 + server_id):
        print(f'Port {5001 + server_id} is in use. Trying to free it...')
        os.system(
            f'FOR /F "tokens=5" %a IN (\'netstat -aon ^| find ":{5001 + server_id} " ^| find "LISTENING"\') DO taskkill /F /PID %a')
    # Spawn a new server instance
    os.system(f'docker run --name=server{server_id} --rm -d -e SERVER_ID={server_id} -p 500{1 + server_id}:5000 server')


# Test script
def test_load_balancer():
    server_ids = [1, 2, 3, 4, 5, 6]
    endpoints = ['/rep', '/add', '/rm', '/test']  # Add your endpoints here

    while True:
        for server_id in server_ids:
            for endpoint in endpoints:
                url = f'http://localhost:500{server_id}{endpoint}'
                if endpoint == '/add':
                    response = requests.post(url, json={'n': 1})
                elif endpoint == '/rm':
                    response = requests.delete(url, json={'n': 1})
                else:
                    response = requests.get(url)

                if response.status_code != 200:
                    print(f'Server {server_id} failed at {endpoint}. Spawning a new instance...')
                    spawn_new_server(server_id)
                    time.sleep(5)  # Wait for the new server instance to start
                else:
                    print(f'Server {server_id} responded with status code {response.status_code} at {endpoint}')
        time.sleep(1)  # Wait before the next round of health checks

        # Simulate server failure at random intervals
        if random.random() < 0.1:
            failed_server_id = random.choice(server_ids)
            print(f'Simulating failure of server {failed_server_id}...')
            simulate_server_failure(failed_server_id)


test_load_balancer()