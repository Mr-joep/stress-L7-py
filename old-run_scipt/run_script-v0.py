import subprocess

def run_script(num_instances):
    processes = []
    
    for _ in range(num_instances):
        process = subprocess.Popen(["python", "request-script-v.6.py"])
        processes.append(process)
    
    for process in processes:
        process.wait()

if __name__ == "__main__":
    try:
        num_instances = int(input("Enter the number of times you want to run the script: "))
        run_script(num_instances)
    except ValueError:
        print("Please enter a valid number.")
