from flask import Flask, jsonify
from load_balancer.consistent_hash_map import ConsistentHashMap

app = Flask(__name__)

# Create an instance of ConsistentHashMap
chm = ConsistentHashMap(3, 512, 9)


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
