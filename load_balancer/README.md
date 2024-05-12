# Usage

- Especially when performing `Task 4`:

## Load Balancer
- Build the load balancer Docker image:

```sh
 docker build -t load_balancer .  
```

- Run the load balancer Docker containers:

```sh
 docker-compose -p balancer up -d
```

- Stop the load balancer Docker containers:

```sh
 docker-compose -p balancer down
```

- Open your browser and go to the load balancer endpoints:
   - http://127.0.0.1:5001/rep to navigate to the `/rep` endpoint.
   - http://127.0.0.1:5001/add to navigate to the `/add` endpoint.
   - http://127.0.0.1:5001/rm to navigate to the `/rm` endpoint.
   - http://127.0.0.1:5001/<path:path> to navigate to the `/<path:path>` endpoint.
