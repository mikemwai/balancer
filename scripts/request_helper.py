import asyncio
import aiohttp
import logging

logger = logging.getLogger(__name__)

async def fetch(session, url):
    try:
        async with session.get(url) as response:
            logger.info(f"Request to {url} returned status {response.status}")
            return await response.text()
    except Exception as e:
        logger.error(f"Request to {url} failed: {e}")

async def fetch_multiple(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)
