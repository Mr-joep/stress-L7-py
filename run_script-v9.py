import subprocess
import time
import os
import shutil

def run_request_script(num_times, delay=1.2):
    script_name = "request-script-v1.1.py"
    processes = []

    try:
        # Check if "requests_log" folder exists and delete it
        if os.path.exists("requests_log"):
            shutil.rmtree("requests_log")

        for _ in range(num_times):
            process = subprocess.Popen(["python", script_name])
            processes.append(process)
            time.sleep(delay)  # Set a 1.2-second delay between process launches

        # Wait for all child processes to finish
        for process in processes:
            process.wait()

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    try:
        num_times = int(input("Enter the number of times to run the script: "))
        run_request_script(num_times)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
