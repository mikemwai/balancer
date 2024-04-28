from flask import Flask, jsonify, request
import os

app = Flask(__name__)


@app.route('/home', methods=['GET'])
def home():
    server_id = os.getenv('SERVER_ID', 'N/A')
    return jsonify(message=f"Hello from Server: {server_id}", status='successful'), 200


@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    # Sends an empty response with a valid response code
    return '', 200


@app.errorhandler(404)
def page_not_found(e):
    return jsonify(message=f"<Error> ’{request.path}’ endpoint does not exist", status="failure"), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
