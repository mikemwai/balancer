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
 docker run --name=balancer --rm --detach -p 5000:5000 balancer
```

- Stop the Docker container:
```sh
 docker stop balancer
```

## Usage

- Open your browser and go to:
   - http://127.0.0.1:5000/ to navigate to the home page.
   - http://127.0.0.1:5000/home to navigate to the /home endpoint.
   - http://127.0.0.1:5000/heartbeat to navigate to the /heartbeat endpoint.