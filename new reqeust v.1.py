import requests
import time

def check_host_status(url):
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

def test_website(url):
    start_time = time.time()
    total_requests = 0

    try:
        while True:
            if not check_host_status(url):
                print(f"Host {url} is down. Stopping the script.")
                break

            response = requests.get(url)
            total_requests += 1

            # Print status every second
            time_elapsed = time.time() - start_time
            print(f"Requests: {total_requests} | Elapsed Time: {int(time_elapsed)}s | Requests/s: {total_requests / time_elapsed:.2f}", end='\r')

            time.sleep(1)

    except KeyboardInterrupt:
        pass
    finally:
        end_time = time.time()
        runtime = end_time - start_time

        if total_requests > 0:
            average_requests_per_second = total_requests / runtime
            print(f"\n\nTest finished!\nRuntime: {runtime:.2f}s\nAverage Requests/s: {average_requests_per_second:.2f}")
        else:
            print("\n\nNo requests were made.")

if __name__ == "__main__":
    website_url = input("Enter the website URL to test: ")
    test_website(website_url)
