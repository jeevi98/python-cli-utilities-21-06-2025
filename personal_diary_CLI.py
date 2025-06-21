import os
from datetime import datetime

DIARY_FILE = "diary.txt"

def write_entry():
    print("\n Write your journal entry. Type 'END' on a new line to finish.")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    if lines:
        with open(DIARY_FILE, "a") as f:
            f.write(f"\n=== {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n")
            f.write('\n'.join(lines) + "\n")
        print(" Entry saved successfully!")
    else:
        print(" No entry written.")

def view_entries():
    if not os.path.exists(DIARY_FILE):
        print(" No entries found.")
        return

    print("\n Your Diary Entries:")
    with open(DIARY_FILE, "r") as f:
        print(f.read())

def main():
    while True:
        print("\n=== Personal Diary CLI ===")
        print("1. Write a new entry")
        print("2. View past entries")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            write_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print(" Goodbye! Keep writing.")
            break
        else:
            print(" Invalid choice. Try again.")

if __name__ == "__main__":
    main()
