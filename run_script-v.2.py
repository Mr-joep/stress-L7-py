import subprocess
import threading
import signal

class ScriptRunner:
    def __init__(self):
        self.total_requests = 0
        self.stop_flag = threading.Event()
        signal.signal(signal.SIGINT, self.handle_stop_signal)

    def run_script(self, num_instances):
        processes = []

        for _ in range(num_instances):
            process = subprocess.Popen(["python", "request-script-v.6.py"])
            processes.append(process)

        for process in processes:
            process.wait()
            self.total_requests += process.returncode

    def stop_scripts(self):
        input("Type 'stop' to stop all running scripts: ")
        self.stop_flag.set()

    def handle_stop_signal(self, signum, frame):
        self.stop_flag.set()

if __name__ == "__main__":
    try:
        num_instances = int(input("Enter the number of times you want to run the script: "))
        runner = ScriptRunner()

        # Start the run_script function in a separate thread
        run_thread = threading.Thread(target=runner.run_script, args=(num_instances,))
        run_thread.start()

        # Start the stop_scripts function in the main thread
        runner.stop_scripts()

        # Wait for the run_thread to finish
        run_thread.join()

        print(f"Combined total requests: {runner.total_requests}")

    except ValueError:
        print("Please enter a valid number.")
