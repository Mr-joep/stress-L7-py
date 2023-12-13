import requests
from concurrent.futures import ThreadPoolExecutor

# Function to make a single request to a given URL
def make_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException:
        return False

def request_domains_parallel(urls, num_threads=5):
    successful_requests = 0

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Use executor.map to concurrently execute the make_request function for each URL
        results = executor.map(make_request, urls)

    # Count the successful requests
    successful_requests = sum(results)

    print(f"Total successful requests: {successful_requests}")

if __name__ == "__main__":
    # Replace these URLs with the desired domains
    domain_urls = ["http://192.168.154.139/"] * 10000000  # Repeat the same URL 10 times

    # Specify the number of threads (concurrent requests)
    num_threads = 24

    # Make requests to the domains concurrently
    request_domains_parallel(domain_urls, num_threads)
