import requests
import concurrent.futures
import time

NUM_REQUESTS = 1000000000000  # Adjust the number of requests as needed
DOMAIN_URL = "http://192.168.154.139"  # Replace with the actual domain URL

def make_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException:
        return False

def run_requests():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        start_time = time.time()
        futures = [executor.submit(make_request, DOMAIN_URL) for _ in range(NUM_REQUESTS)]
        concurrent.futures.wait(futures)
        end_time = time.time()

    successful_requests = sum(f.result() for f in futures)
    elapsed_time = end_time - start_time
    requests_per_second = successful_requests / elapsed_time if elapsed_time > 0 else 0

    print(f"Total successful requests: {successful_requests}")
    print(f"Total time taken: {elapsed_time:.2f} seconds")
    print(f"Requests per second: {requests_per_second:.2f}")

if __name__ == "__main__":
    run_requests()
