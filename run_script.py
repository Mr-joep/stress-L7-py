import subprocess

def run_request_script(num_times):
    script_name = "request-script-v.7.py"
    processes = []

    try:
        for _ in range(num_times):
            process = subprocess.Popen(["python", script_name])
            processes.append(process)

        # Wait for all child processes to finish
        for process in processes:
            process.wait()

    except KeyboardInterrupt:
        print("\nCtrl+C detected. Stopping the child processes.")
        for process in processes:
            process.terminate()

if __name__ == "__main__":
    try:
        num_times = int(input("Enter the number of times to run the script: "))
        run_request_script(num_times)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
