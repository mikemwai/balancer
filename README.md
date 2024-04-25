# balancer
A distributed load balancer.

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop)

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
 docker run --name=balancer --rm --detach balancer
```

- Stop the Docker container:
```sh
 docker stop balancer
```