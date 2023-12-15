import subprocess
import time
import os
import shutil

def run_scripts(num_request_scripts, num_data_scripts, request_delay=1.2, data_delay=0):
    request_script_name = "request-script-v1.1.py"
    data_script_name = "data-colection-v.3.py"

    try:
        # Check if "requests_log" folder exists and delete it
        if os.path.exists("requests_log"):
            shutil.rmtree("requests_log")

        # Run request scripts
        for _ in range(num_request_scripts):
            request_process = subprocess.Popen(["python", request_script_name])
            time.sleep(request_delay)

        # Run data script
        data_process = subprocess.Popen(["python", data_script_name])

        # Wait for all request processes to finish
        request_process.wait()

        # Wait for the data process to finish
        data_process.wait()

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    try:
        num_request_scripts = int(input("Enter the number of times to run the request script: "))
        num_data_scripts = 1  # Start 1 data script
        run_scripts(num_request_scripts, num_data_scripts)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
