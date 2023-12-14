import requests
import concurrent.futures
import time

def check_website_once(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"Website {url} is online.")
    except requests.RequestException as e:
        print(f"Website {url} is down. Error: {e}")

def make_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return 1
    except requests.RequestException:
        return 0

def monitor_website(url, duration=10, max_workers=10):
    start_time = time.time()
    request_count = 0

    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            while time.time() - start_time < duration:
                futures = [executor.submit(make_request, url) for _ in range(max_workers)]
                request_count += sum(future.result() for future in concurrent.futures.as_completed(futures))

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
    website_url = "http://192.168.154.139/"

    # Step 1: Check if the website is online
    check_website_once(website_url)

    # Step 2 and 3: Monitor the website for a specified duration
    monitor_website(website_url, duration=30, max_workers=20)
