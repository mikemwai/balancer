# balancer
A distributed load balancer.

## Installation

- Install the needed packages:
```sh
 pip install -r requirements.txt 
```

- Build the Docker image:
```sh
 docker build -t balancer .
```

- Run the Docker container:
```sh
 docker run -d -p 5000:5000 -e SERVER_ID=3 balancer
```