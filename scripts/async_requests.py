import asyncio
import aiohttp
import logging

logging.basicConfig(filename='async_requests.log', level=logging.INFO, format='%(asctime)s %(message)s')


async def fetch(session, url, retry=3):
    for attempt in range(retry):
        try:
            async with session.get(url) as response:
                result = await response.text()
                logging.info(f'Request to {url} with response: {result}')
                return result
        except aiohttp.ClientConnectorError as e:
            logging.error(f'Failed to connect to {url} on attempt {attempt + 1}: {e}')
            if attempt == retry - 1:
                return None
        except aiohttp.ServerDisconnectedError as e:
            logging.error(f'Server disconnected on attempt {attempt + 1}: {e}')
            if attempt == retry - 1:
                return None
        await asyncio.sleep(1)


async def main():
    url = 'http://localhost:5001/home'
    num_requests = 10000
    tasks = []

    async with aiohttp.ClientSession() as session:
        for _ in range(num_requests):
            task = fetch(session, url)
            tasks.append(task)

        responses = await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
