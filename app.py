from flask import Flask, jsonify
from consistent_hash_map import ConsistentHashMap
import os

app = Flask(__name__)

# Create an instance of ConsistentHashMap
chm = ConsistentHashMap(3, 512, 9)


@app.route('/', methods=['GET'])
def index():
    return 'Welcome to the home page!', 200


@app.route('/home', methods=['GET'])
def home():
    # Use the get_server method to get the server for a request
    server = chm.get_server(123)
    return jsonify(message=f'Hello from Server: {server}', status='successful'), 200


@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    return '', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
