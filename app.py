from flask import Flask, jsonify, request
from load_balancer.consistent_hash_map import ConsistentHashMap
import random
import string

app = Flask(__name__)

# Create an instance of ConsistentHashMap
chm = ConsistentHashMap(3, 512, 9)

# Initialize the list of server replicas
server_replicas = ["Server 1", "Server 2", "Server 3"]


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
            # Generate a random hostname
            server_replicas.append(''.join(random.choices(string.ascii_uppercase + string.digits, k=5)))
    return jsonify(message={"N": len(server_replicas), "replicas": server_replicas}, status="successful"), 200


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
    return jsonify(message={"N": len(server_replicas), "replicas": server_replicas}, status="successful"), 200


@app.route('/<path:path>', methods=['GET'])
def route_request(path):
    # Route the request to a server replica
    server = chm.get_server(path)
    if server < len(server_replicas):
        return jsonify(message=f"Request routed to {server_replicas[server]}", status="successful"), 200
    else:
        return jsonify(message=f"<Error> ’/{path}’ endpoint does not exist in server replicas", status="failure"), 400


@app.route('/', methods=['GET'])
def index():
    return '''
    <h1>Welcome to the home page!</h1>
    <p>
        <a href="/home"><button>Home Endpoint</button></a>
        <a href="/heartbeat"><button>Heartbeat Endpoint</button></a>
    </p>
    ''', 200


@app.route('/home', methods=['GET'])
def home():
    # Use the get_server method to get the server for a request
    servers = [chm.get_server(i) for i in range(1000)]
    server_counts = {server: servers.count(server) for server in set(servers)}
    return jsonify(server_counts=server_counts, status='successful'), 200


@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    # Sends an empty response with a valid response code
    return '', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
