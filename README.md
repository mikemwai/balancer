# Implementing a Customizable Load Balancer

## Overview
![Overview](./overview.png)

## Prerequisites

- [Python 3.8](https://www.python.org/downloads/release/python-380/) : Programming language.
- [Docker Desktop](https://www.docker.com/products/docker-desktop) : Running the application in a container.
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