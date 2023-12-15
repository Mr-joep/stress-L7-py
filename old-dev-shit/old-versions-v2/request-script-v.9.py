import aiohttp
import asyncio
import time

async def check_website_once(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                print(f"Website {url} is online.")
    except aiohttp.ClientError as e:
        print(f"Website {url} is down. Error: {e}")

async def make_request(session, url):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            return 1
    except aiohttp.ClientError:
        return 0

async def monitor_website(url, max_concurrent_requests=50):
    start_time = time.time()
    request_count = 0

    try:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=max_concurrent_requests)) as session:
            while True:
                tasks = [make_request(session, url) for _ in range(max_concurrent_requests)]
                request_count += sum(await asyncio.gather(*tasks))

                time_elapsed = time.time() - start_time
                if time_elapsed >= 1:
                    with open("requests_log.txt", "a") as file:
                        file.write(f"Requests per second: {request_count / time_elapsed:.2f}\n")
                    start_time = time.time()
                    request_count = 0

    except KeyboardInterrupt:
        pass

    total_time = time.time() - start_time
    average_requests_per_second = request_count / total_time if total_time > 0 else 0
    with open("requests_log.txt", "a") as file:
        file.write(f"\nAverage requests per second: {average_requests_per_second:.2f}\n")

if __name__ == "__main__":
    website_url = "http://192.168.154.139"

    # Step 1: Check if the website is online
    asyncio.run(check_website_once(website_url))

    # Step 2 and 3: Monitor the website indefinitely with increased concurrent requests
    asyncio.run(monitor_website(website_url, max_concurrent_requests=100))
