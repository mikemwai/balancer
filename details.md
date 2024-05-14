## Prerequisites

- [Python 3.8](https://www.python.org/downloads/release/python-380/) : Programming language.
- [Docker Desktop](https://www.docker.com/products/docker-desktop) : Running the application in containers.
- [Postman](https://www.postman.com/downloads/) : Testing the HTTP API endpoints.

## Installation
- Create a virtual environment:

```sh
 python -m venv venv
```

- Activate the virtual environment:
- For Linux or macOS:
```sh
 source venv/bin/activate
```
- For Windows
```sh
 venv\Scripts\activate
```

## Usage

- Running the application for the first time:

```sh
 docker-compose up --build
```

- Running the application:

```sh
 docker-compose up
```

- Stopping the application:

```sh
 docker-compose down
```
 
- Docker compose project running:

  - Three server containers and the load balancer:
 
    ![three](https://res.cloudinary.com/dkmblonw5/image/upload/f_auto,q_auto/v1/balancer/docker-container3)
    
  - Six server containers and the load balancer:
  
    ![six](https://res.cloudinary.com/dkmblonw5/image/upload/f_auto,q_auto/v1/balancer/docker-containers)

- For more details on how to run:

  - [The Server](./server/README.md)
  - [The Load Balancer](./load_balancer/README.md)
