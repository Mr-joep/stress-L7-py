import aiohttp
import asyncio
import time

async def make_request(session, url):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            return 1
    except aiohttp.ClientError:
        return 0

async def monitor_website(url, max_sessions=10, max_requests_per_session=120):
    start_time = time.time()
    request_count = 0

    try:
        async with aiohttp.ClientSession() as session:
            while True:
                tasks = [make_request(session, url) for _ in range(max_requests_per_session)]
                request_count += sum(await asyncio.gather(*tasks))

                time_elapsed = time.time() - start_time
                if time_elapsed >= 1:
                    print(f"Requests per second: {request_count / time_elapsed:.2f}")
                    start_time = time.time()
                    request_count = 0

    except KeyboardInterrupt:
        pass

    total_time = time.time() - start_time
    average_requests_per_second = request_count / total_time if total_time > 0 else 0
    print(f"\nAverage requests per second: {average_requests_per_second:.2f}")

if __name__ == "__main__":
    website_url = "http://192.168.154.139"

    # Step 1: Monitor the website with parallel sessions and requests
    asyncio.run(monitor_website(website_url, max_sessions=10, max_requests_per_session=100))
