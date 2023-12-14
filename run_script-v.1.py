import subprocess
import threading

def run_script(num_instances):
    processes = []
    
    for _ in range(num_instances):
        process = subprocess.Popen(["python", "request-script-v.6.py"])
        processes.append(process)
    
    for process in processes:
        process.wait()

def stop_scripts(processes):
    input("Type 'stop' to stop all running scripts: ")
    for process in processes:
        process.terminate()

if __name__ == "__main__":
    try:
        num_instances = int(input("Enter the number of times you want to run the script: "))
        processes = []

        # Start the run_script function in a separate thread
        run_thread = threading.Thread(target=run_script, args=(num_instances,))
        run_thread.start()

        # Start the stop_scripts function in the main thread
        stop_scripts(processes)

        # Wait for the run_thread to finish
        run_thread.join()

    except ValueError:
        print("Please enter a valid number.")
