import subprocess
import time
import os
import shutil
import glob

def get_latest_request_number():
    log_folder = "requests_log"
    log_files = glob.glob(os.path.join(log_folder, "requests_log*.txt"))

    if log_files:
        latest_log_file = max(log_files, key=os.path.getctime)
        with open(latest_log_file, "r") as file:
            lines = file.readlines()
            if lines:
                # Assuming the number is on the last line of the file
                last_number = int(lines[-1])
                return last_number

    return None

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

        # Get and display the latest request number
        latest_number = get_latest_request_number()
        if latest_number is not None:
            print(f"The latest request number is: {latest_number}")

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    try:
        num_times = int(input("Enter the number of times to run the script: "))
        run_request_script(num_times)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
