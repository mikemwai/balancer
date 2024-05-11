# Usage

## Server
- Build the server Docker image:
- Navigate to the server directory and run the following terminal commands.

```sh
 docker build -t server .  
```

- Run the server Docker containers:

```sh
 docker run --name=server1 --rm -d -e SERVER_ID=1 -p 5002:5000 server
 docker run --name=server2 --rm -d -e SERVER_ID=2 -p 5003:5000 server
 docker run --name=server3 --rm -d -e SERVER_ID=3 -p 5004:5000 server
 docker run --name=server4 --rm -d -e SERVER_ID=4 -p 5005:5000 server
 docker run --name=server5 --rm -d -e SERVER_ID=5 -p 5006:5000 server
 docker run --name=server6 --rm -d -e SERVER_ID=6 -p 5007:5000 server
```

- Stop the Docker containers:

```sh
 docker stop server1 server2 server3 server4 server5 server6
```

- Open your browser and go to the server endpoints:
   - http://127.0.0.1:5002/home to navigate to the `/home` endpoint.
   - http://127.0.0.1:5002/heartbeat to navigate to the `/heartbeat` endpoint.