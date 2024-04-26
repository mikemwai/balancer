# Implementing a Customizable Load Balancer
![Overview](./overview.png)

## Prerequisites

- [Python 3.8](https://www.python.org/downloads/release/python-380/) : Programming language.
- [Docker Desktop](https://www.docker.com/products/docker-desktop) : Running the application in a container.
- [Postman](https://www.postman.com/downloads/) : Testing the API endpoints.

## Installation
- Create a virtual environment:

```sh
 python -m venv venv
```

- Activate the virtual environment:

```sh
 source venv/bin/activate
```

- Install the needed packages:

```sh
 pip install -r requirements.txt 
```

## Usage
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

- Open your browser and go to:
   - http://127.0.0.1:5000/ to navigate to the `home` page.
   - http://127.0.0.1:5000/home to navigate to the `/home` endpoint.
   - http://127.0.0.1:5000/heartbeat to navigate to the `/heartbeat` endpoint.