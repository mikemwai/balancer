import asyncio
import aiohttp
import time
import json
import matplotlib.pyplot as plt


async def make_request(session, url, semaphore):
    async with semaphore:
        start_time = time.time()
        try:
            async with session.get(url) as response:
                await response.text()
        except (aiohttp.ClientError, OSError):
            return None
        end_time = time.time()
        return end_time - start_time


async def set_server_count(session, target_count):
    async with session.get('http://localhost:5001/rep') as response:
        response.raise_for_status()
        payload = await response.json()
    current_count = payload['message']['N']

    if target_count > current_count:
        async with session.post('http://localhost:5001/add', json={'n': target_count - current_count}) as response:
            response.raise_for_status()
    elif target_count < current_count:
        async with session.delete('http://localhost:5001/rm', json={'n': current_count - target_count}) as response:
            response.raise_for_status()


async def main():
    url = 'http://localhost:5001/home'
    average_loads = []
    num_requests = 10000

    for N in range(2, 7):
        total_time_taken = 0

        connector = aiohttp.TCPConnector(limit=20, limit_per_host=20)
        semaphore = asyncio.Semaphore(20)
        async with aiohttp.ClientSession(connector=connector) as session:
            # Reset the load balancer to the exact target server count for this run.
            await set_server_count(session, N)

            tasks = [make_request(session, url, semaphore) for _ in range(num_requests)]
            times = await asyncio.gather(*tasks)
            successful_times = [time_taken for time_taken in times if time_taken is not None]
            total_time_taken += sum(successful_times)

        average_load = total_time_taken / len(successful_times)
        average_loads.append(average_load)

        print(f'Average Load for {len(successful_times)} Requests with {N} server containers: {average_load}')

    xs = list(range(2, 7))
    plt.plot(xs, average_loads)
    plt.xlabel('Number of Server Containers')
    plt.ylabel('Average Load')
    plt.title('Average Load vs Number of Server Containers')
    # Save chart and data for later review
    plt.tight_layout()
    chart_path = 'load_balancer/average_loads_A2.png'
    plt.savefig(chart_path, dpi=200)
    # Save the raw numbers alongside the N values
    data_path = 'load_balancer/average_loads_A2.json'
    with open(data_path, 'w', encoding='utf-8') as f:
        json.dump({'N': xs, 'average_loads': average_loads}, f, indent=2)
    plt.show()

if __name__ == "__main__":
    asyncio.run(main())
