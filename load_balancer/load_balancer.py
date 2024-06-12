import logging
from logging_config import setup_logging
from flask import Flask, jsonify, request
from consistent_hash_map import ConsistentHashMap
import random

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)

app = Flask(__name__)

chm = ConsistentHashMap(3, 512, 9)
server_replicas = ["Server 1", "Server 2", "Server 3"]

def add_server(servers, server_id):
    if server_id not in servers:
        servers.append(server_id)
        logger.info(f"Server {server_id} added to load balancer")
    else:
        logger.warning(f"Server {server_id} is already in the server list")

def remove_server(servers, server_id):
    if server_id in servers:
        servers.remove(server_id)
        logger.info(f"Server {server_id} removed from load balancer")
    else:
        logger.error(f"Attempted to remove non-existent server {server_id}")

def handle_request(servers, path):
    if not servers:
        logger.error("No servers available to handle the request")
        return "503 Service Unavailable", 503

    server_id = servers[0]  # Simplified for this example
    logger.debug(f"Handling request {path} with {server_id}")
    return f"Hello from {server_id}", 200

# HTTP endpoints
@app.route('/rep', methods=['GET'])
def get_replicas():
    logger.info('GET /rep - Returning replicas list')
    return jsonify(message={"N": len(server_replicas), "replicas": server_replicas}, status="successful"), 200

@app.route('/add', methods=['POST'])
def add_replicas():
    data = request.get_json()
    n = data.get('n')
    hostnames = data.get('hostnames', [])
    if len(hostnames) > n:
        logger.error('POST /add - Error: Length of hostname list is more than newly added instances')
        return jsonify(message="<Error> Length of hostname list is more than newly added instances",
                       status="failure"), 400
    for i in range(n):
        if i < len(hostnames):
            server_replicas.append(hostnames[i])
        else:
            server_replicas.append('Server ' + str(i + 1))

    chm.set_num_servers(len(server_replicas))

    logger.info(f'POST /add - Updated number of servers in ConsistentHashMap: {len(server_replicas)}')

    return jsonify(
        message={"N": len(server_replicas), "replicas": server_replicas, "updated_servers": len(server_replicas)},
        status="successful"), 200

@app.route('/rm', methods=['DELETE'])
def remove_replicas():
    data = request.get_json()
    n = data.get('n')
    hostnames = data.get('hostnames', [])
    if len(hostnames) > n:
        logger.error('DELETE /rm - Error: Length of hostname list is more than removable instances')
        return jsonify(message="<Error> Length of hostname list is more than removable instances",
                       status="failure"), 400
    for hostname in hostnames:
        if hostname in server_replicas:
            server_replicas.remove(hostname)
            n -= 1
    while n > 0 and server_replicas:
        server_replicas.pop(random.randint(0, len(server_replicas) - 1))
        n -= 1

    # Update the ConsistentHashMap instance to reflect the new number of servers
    chm.set_num_servers(len(server_replicas))

    logger.info(f'DELETE /rm - Updated number of servers in ConsistentHashMap: {len(server_replicas)}')

    return jsonify(
        message={"N": len(server_replicas), "replicas": server_replicas, "updated_servers": len(server_replicas)},
        status="successful"), 200

@app.route('/<path:path>', methods=['GET'])
def route_request(path):
    # Route the request to a server replica
    server = chm.get_server(path)
    if server < len(server_replicas):
        logger.info(f'GET /{path} - Request routed to {server_replicas[server]}')
        return jsonify(message=f"Request routed to {server_replicas[server]}", status="successful"), 200
    else:
        logger.error(f'GET /{path} - Error: Endpoint does not exist in server replicas')
        return jsonify(message=f"<Error> ’/{path}’ endpoint does not exist in server replicas", status="failure"), 400

@app.route('/fail', methods=['POST'])
def simulate_failure():
    data = request.get_json()
    hostname = data.get('hostname')
    if hostname in server_replicas:
        server_replicas.remove(hostname)
        chm.set_num_servers(len(server_replicas))
        logger.info(f'POST /fail - Simulated failure of {hostname}')
        return jsonify(message=f"Simulated failure of {hostname}.", status="successful"), 200
    else:
        logger.error(f'POST /fail - Error: {hostname} does not exist in server replicas')
        return jsonify(message=f"<Error> {hostname} does not exist in server replicas", status="failure"), 400

if __name__ == '__main__':
    servers = []
    add_server(servers, "Server1")
    add_server(servers, "Server2")
    print(handle_request(servers, "/home"))
    remove_server(servers, "Server1")
    print(handle_request(servers, "/home"))
    remove_server(servers, "Server3")

    app.run(host='0.0.0.0', port=5001)
