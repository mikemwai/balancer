# Load Balancer

## Overview
![Overview](https://res.cloudinary.com/dkmblonw5/image/upload/f_auto,q_auto/v1/balancer/overview)

- This project implements a customizable load balancer that routes requests coming from several clients asynchronously among several servers so that the load is nearly evenly distributed among them.

## Design Choices
- The load balancer is designed using a consistent hashing mechanism. This design choice was made to ensure that the load balancer can handle a large number of requests and distribute them evenly across the servers. The consistent hashing mechanism also allows the load balancer to handle changes in the number of servers without causing a significant disruption in the distribution of requests.

## Assumptions
-The following assumptions were made during the development of this load balancer:
    - The servers are capable of handling the load distributed to them by the load balancer.
    - The number of servers can change dynamically, and the load balancer can handle these changes.
    - The hash function used for consistent hashing provides a good distribution of requests across the servers.

## Testing
- The load balancer was tested using a series of tests that simulate a variety of scenarios, including a large number of requests, changes in the number of servers, and server failures. The tests were designed to measure the performance of the load balancer and ensure that it can handle these scenarios effectively.

## Performance Analysis

- The performance of the load balancer was analyzed by measuring the total time taken to handle a large number of requests and the average load on the servers. The results of this analysis showed that the load balancer is able to distribute the load evenly across the servers and handle a large number of requests efficiently.

## i) A-1

-  Launch 10000 async requests on N = 3 server containers and report the request count handled by each server instance
in a bar chart. Explain your observations in the graph and your view on the performance.

### Observations

![graphA1.1](https://res.cloudinary.com/dkmblonw5/image/upload/f_auto,q_auto/v1/balancer/balancerA-1-1)

![consoleA1.2](https://res.cloudinary.com/dkmblonw5/image/upload/f_auto,q_auto/v1/balancer/balancerA-1-2)

- For more details on how to run:

  - [The Server](./server/README.md)
  - [The Load Balancer](./load_balancer/README.md)

## ii) A-2

-  Next, increment N from 2 to 6 and launch 10000 requests on each such increment. Report the average load of the servers 
at each run in a line chart. Explain your observations in the graph and your view on the scalability of the load balancer
implementation.

### Observations

![graphA2.1](https://res.cloudinary.com/dkmblonw5/image/upload/f_auto,q_auto/v1/balancer/balancerA-2-1)

![consoleA2.2](https://res.cloudinary.com/dkmblonw5/image/upload/f_auto,q_auto/v1/balancer/balancerA-2-2)

## iii) A-3

-  Test all endpoints of the load balancer and show that in case of server failure, the load balancer spawns a new instance
quickly to handle the load.

### Observations

![Task 3](https://res.cloudinary.com/dkmblonw5/image/upload/f_auto,q_auto/v1/balancer/balancer-A-3)

## iv) A-4

-  Finally, modify the hash functions H(i), Φ(i, j) and report the observations from (A-1) and (A-2).

### Observations

i) A-1:

![Task 1-1](https://res.cloudinary.com/dkmblonw5/image/upload/f_auto,q_auto/v1/balancer/balancer-A-4-1)

![Task 1-2](https://res.cloudinary.com/dkmblonw5/image/upload/f_auto,q_auto/v1/balancer/balancer-A-4-2)

ii) A-2:

![Task 2-1](https://res.cloudinary.com/dkmblonw5/image/upload/f_auto,q_auto/v1/balancer/balancer-A-4-2-1)

![Task 2-2](https://res.cloudinary.com/dkmblonw5/image/upload/f_auto,q_auto/v1/balancer/balancer-A-4-2-2)

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
