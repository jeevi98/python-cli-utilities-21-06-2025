import time
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def countdown(minutes, label):
    seconds = minutes * 60
    while seconds:
        mins = seconds // 60
        secs = seconds % 60
        print(f"{label}  {mins:02}:{secs:02}", end="\r")
        time.sleep(1)
        seconds -= 1
    print(f"{label}  DONE!{' ' * 20}")


def pomodoro_timer():
    work_sessions = 0
    while True:
        clear_screen()
        print(" Pomodoro Timer Started!")
        countdown(25, "Work")
        work_sessions += 1

        if work_sessions % 4 == 0:
            print(" Take a long break (15 mins)")
            countdown(15, "Long Break")
        else:
            print(" Take a short break (5 mins)")
            countdown(5, "Short Break")

        choice = input("▶Press Enter to continue to next session or type 'exit' to quit: ").strip().lower()
        if choice == 'exit':
            print(" Exiting Pomodoro Timer. Stay focused!")
            break


def main():
    print("=== Pomodoro Timer CLI ===")
    print("1. Start Pomodoro Timer")
    print("2. Exit")
    while True:
        option = input("Choose an option (1/2): ")
        if option == '1':
            pomodoro_timer()
            break
        elif option == '2':
            print(" Goodbye!")
            break
        else:
            print(" Invalid option. Try 1 or 2.")

if __name__ == "__main__":
    main()
