from flask import Flask, jsonify, request
from consistent_hash_map import ConsistentHashMap
import random
import string

app = Flask(__name__)

# Create an instance of ConsistentHashMap
chm = ConsistentHashMap(3, 512, 9)

# Initialize the list of server replicas
server_replicas = ["Server 1", "Server 2", "Server 3"]


# HTTP endpoints
@app.route('/rep', methods=['GET'])
def get_replicas():
    return jsonify(message={"N": len(server_replicas), "replicas": server_replicas}, status="successful"), 200


@app.route('/add', methods=['POST'])
def add_replicas():
    data = request.get_json()
    n = data.get('n')
    hostnames = data.get('hostnames', [])
    if len(hostnames) > n:
        return jsonify(message="<Error> Length of hostname list is more than newly added instances",
                       status="failure"), 400
    for i in range(n):
        if i < len(hostnames):
            server_replicas.append(hostnames[i])
        else:
            # Use the server ID to generate the server name
            server_replicas.append('S' + str(i + 1))

    # Update the ConsistentHashMap instance to reflect the new number of servers
    chm.set_num_servers(len(server_replicas))

    print(
        f'Updated number of servers in ConsistentHashMap: {len(server_replicas)}')  # Print statement to confirm update

    return jsonify(
        message={"N": len(server_replicas), "replicas": server_replicas, "updated_servers": len(server_replicas)},
        status="successful"), 200


@app.route('/rm', methods=['DELETE'])
def remove_replicas():
    data = request.get_json()
    n = data.get('n')
    hostnames = data.get('hostnames', [])
    if len(hostnames) > n:
        return jsonify(message="<Error> Length of hostname list is more than removable instances",
                       status="failure"), 400
    for hostname in hostnames:
        if hostname in server_replicas:
            server_replicas.remove(hostname)
            n -= 1
    while n > 0 and server_replicas:
        # Remove a random server replica
        server_replicas.pop(random.randint(0, len(server_replicas) - 1))
        n -= 1

    # Update the ConsistentHashMap instance to reflect the new number of servers
    chm.set_num_servers(len(server_replicas))

    print(
        f'Updated number of servers in ConsistentHashMap: {len(server_replicas)}')  # Print statement to confirm update

    return jsonify(
        message={"N": len(server_replicas), "replicas": server_replicas, "updated_servers": len(server_replicas)},
        status="successful"), 200


@app.route('/<path:path>', methods=['GET'])
def route_request(path):
    # Route the request to a server replica
    server = chm.get_server(path)
    if server < len(server_replicas):
        return jsonify(message=f"Request routed to {server_replicas[server]}", status="successful"), 200
    else:
        return jsonify(message=f"<Error> ’/{path}’ endpoint does not exist in server replicas", status="failure"), 400


@app.route('/fail', methods=['POST'])
def simulate_failure():
    data = request.get_json()
    hostname = data.get('hostname')
    if hostname in server_replicas:
        server_replicas.remove(hostname)
        chm.set_num_servers(len(server_replicas))
        return jsonify(message=f"Simulated failure of {hostname}.", status="successful"), 200
    else:
        return jsonify(message=f"<Error> {hostname} does not exist in server replicas", status="failure"), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
