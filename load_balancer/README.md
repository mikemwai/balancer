# Usage

## Load Balancer
- Build the load balancer Docker image:
- Open new terminal and navigate to load_balancer directory

```sh
 docker build -t load_balancer .  
```

- Run the load balancer Docker container:

```sh
 docker run --name=load_balancer --rm --detach -p 5001:5001 load_balancer 
```

- Stop the load balancer Docker container:

```sh
 docker stop load_balancer
```

- Open your browser and go to the load balancer endpoints:
   - http://127.0.0.1:5001/rep to navigate to the `/rep` endpoint.
   - http://127.0.0.1:5001/add to navigate to the `/add` endpoint.
   - http://127.0.0.1:5001/rm to navigate to the `/rm` endpoint.
   - http://127.0.0.1:5001/<path:path> to navigate to the `/<path:path>` endpoint.
