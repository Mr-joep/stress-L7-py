import aiohttp
import asyncio
import time

DOMAIN_URL = "http://192.168.154.139"  # Replace with the actual domain URL

async def make_request(session):
    try:
        async with session.get(DOMAIN_URL) as response:
            response.raise_for_status()
            return True
    except aiohttp.ClientError:
        return False

async def run_requests(max_concurrent_requests):
    start_time = time.time()
    request_count = 0

    try:
        async with aiohttp.ClientSession() as session:
            while True:
                tasks = [make_request(session) for _ in range(max_concurrent_requests)]
                results = await asyncio.gather(*tasks)
                request_count += sum(results)
                await asyncio.sleep(0.001)  # Sleep for 1 second

                # Display request count every second
                current_time = time.time()
                elapsed_time = current_time - start_time
                print(f"Requests per second: {request_count / elapsed_time:.2f}")

    except KeyboardInterrupt:
        pass
    finally:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Total successful requests: {request_count}")
        print(f"Total time taken: {elapsed_time:.2f} seconds")
        print(f"Average requests per second: {request_count / elapsed_time:.2f}")

if __name__ == "__main__":
    max_concurrent_requests = int(input("Enter the maximum number of concurrent requests: "))
    asyncio.run(run_requests(max_concurrent_requests))
