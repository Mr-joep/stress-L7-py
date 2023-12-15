import os
import time

def display_new_data(directory_path):
    try:
        # Store the last read position for each file
        last_positions = {}

        while True:
            # List all files in the specified directory
            files = os.listdir(directory_path)

            # Iterate through each file
            for file_name in files:
                file_path = os.path.join(directory_path, file_name)

                # Get the last read position for the file
                last_position = last_positions.get(file_name, 0)

                # Read and display new data from the file
                try:
                    with open(file_path, 'r') as file:
                        file.seek(last_position)
                        new_data = file.read()
                        if new_data:
                            print(f"{new_data}", end="")
                            # Update the last read position
                            last_positions[file_name] = file.tell()
                except Exception as e:
                    print(f"Unable to read file content. Error: {e}")

            # Wait for 1 second before checking again
            time.sleep(1)

    except FileNotFoundError:
        print(f"Directory not found: {directory_path}")
    except PermissionError:
        print(f"Permission denied for directory: {directory_path}")
    except KeyboardInterrupt:
        print("\nScript terminated by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the directory path
directory_path = "requests_log"

# Display only new data from files in the specified directory every second
display_new_data(directory_path)
