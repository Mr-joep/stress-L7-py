import subprocess
import time
import os
import shutil
import glob

def get_latest_request_number():
    log_folder = "requests_log"
    log_files = glob.glob(os.path.join(log_folder, "requests_log-*.txt"))

    if log_files:
        latest_log_file = max(log_files, key=os.path.getctime)
        with open(latest_log_file, "r") as file:
            content = file.read()
            return content

    return None

def run_request_script(num_times, delay=1.2):
    request_script = "request-script-v1.1.py"
    data_collection_script = "data-colection-v.3.py"
    processes = []
    data_collection_started = False  # Flag to track if data-colection-v.3.py has started

    try:
        # Check if "requests_log" folder exists and delete it
        if os.path.exists("requests_log"):
            shutil.rmtree("requests_log")

        for _ in range(num_times):
            # Start the request script in a separate process
            request_process = subprocess.Popen(["python", request_script])
            processes.append(request_process)
            time.sleep(delay)  # Set a 1.2-second delay between process launches

        # Wait for all instances of request-script-v1.1.py to finish
        for process in processes:
            process.wait()

        # Start data collection script only once after all instances of request-script-v1.1.py have finished
        if not data_collection_started:
            data_collection_result = subprocess.run(["python", data_collection_script], capture_output=True, text=True)
            print(f"Output of {data_collection_script}:\n{data_collection_result.stdout}")
            data_collection_started = True

        # Get and display the contents of each request log file
        log_folder = "requests_log"
        log_files = glob.glob(os.path.join(log_folder, "requests_log-*.txt"))
        for log_file in log_files:
            with open(log_file, "r") as file:
                content = file.read()
                print(f"Contents of {log_file}:\n{content}")

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    try:
        num_times = int(input("Enter the number of times to run the script: "))
        run_request_script(num_times)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
