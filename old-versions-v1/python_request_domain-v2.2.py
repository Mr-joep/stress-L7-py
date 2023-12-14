import requests
import concurrent.futures
import time

DOMAIN_URL = "http://192.168.154.139"  # Replace with the actual domain URL

def make_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException:
        return False

def run_requests():
    start_time = time.time()
    request_count = 0

    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            while True:
                futures = [executor.submit(make_request, DOMAIN_URL) for _ in range(200)]  # Adjust the batch size as needed
                concurrent.futures.wait(futures)
                request_count += sum(f.result() for f in futures)
                time.sleep(1)  # Sleep for 1 second

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
    run_requests()
