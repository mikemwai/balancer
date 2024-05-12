import asyncio
import aiohttp
import time
import matplotlib.pyplot as plt
import numpy as np
import requests
from consistent_hash_map import ConsistentHashMap


async def make_request(session, url):
    start_time = time.time()
    async with session.get(url) as response:
        await response.text()
    end_time = time.time()
    time_taken = end_time - start_time
    return time_taken


async def main():
    url = 'http://localhost:5001/home'
    average_loads = []
    num_requests = 10000

    for N in range(2, 7):
        total_time_taken = 0

        # Make a POST request to the /add endpoint to update the number of servers in the load balancer
        requests.post('http://localhost:5001/add', json={'n': N})

        async with aiohttp.ClientSession() as session:
            tasks = [make_request(session, url) for _ in range(num_requests)]
            times = await asyncio.gather(*tasks)
            total_time_taken += sum(times)

        average_load = total_time_taken / num_requests
        average_loads.append(average_load)

        print(f'Average Load for {num_requests} Requests with {N} server containers: {average_load}')

    # Plot the average load against the number of server containers
    plt.plot(range(2, 7), average_loads)
    plt.xlabel('Number of Server Containers')
    plt.ylabel('Average Load')
    plt.title('Average Load vs Number of Server Containers')
    plt.show()

if __name__ == "__main__":
    asyncio.run(main())
