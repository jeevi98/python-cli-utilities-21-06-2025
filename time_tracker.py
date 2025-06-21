# time_tracker.py

import time
import json
from datetime import datetime

LOG_FILE = "time_log.json"

def load_log():
    try:
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_log(log_data):
    with open(LOG_FILE, "w") as f:
        json.dump(log_data, f, indent=4)

def start_task(task_name):
    start_time = time.time()
    print(f" Started task '{task_name}' at {datetime.now().strftime('%H:%M:%S')}")
    input(" Press Enter to stop the task...")
    end_time = time.time()

    duration = round(end_time - start_time, 2)
    log_data = load_log()

    if task_name in log_data:
        log_data[task_name].append(duration)
    else:
        log_data[task_name] = [duration]

    save_log(log_data)
    print(f" Stopped task '{task_name}' - Duration: {duration} seconds")

def show_report():
    log_data = load_log()
    if not log_data:
        print("📭 No tasks tracked yet.")
        return

    print("\n Task Time Report")
    for task, times in log_data.items():
        total = round(sum(times), 2)
        count = len(times)
        print(f"• {task}: {total} seconds over {count} session(s)")

def main():
    while True:
        print("\n=== Time Tracker ===")
        print("1. Start a new task")
        print("2. Show time report")
        print("3. Exit")
        choice = input("Select an option (1/2/3): ")

        if choice == "1":
            task = input("Enter task name: ")
            start_task(task)
        elif choice == "2":
            show_report()
        elif choice == "3":
            print(" Exiting Time Tracker. Stay productive!")
            break
        else:
            print(" Invalid choice. Try again.")

if __name__ == "__main__":
    main()
