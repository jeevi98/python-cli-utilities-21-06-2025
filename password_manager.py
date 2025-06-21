# password_manager.py

from cryptography.fernet import Fernet
import os

# Generate key (once) and save to a file
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt and save password
def add_password(account, password):
    key = load_key()
    f = Fernet(key)
    encrypted = f.encrypt(password.encode())

    with open("passwords.txt", "a") as f_file:
        f_file.write(f"{account} | {encrypted.decode()}\n")
    print("✅ Password saved securely!")

# View all saved passwords (decrypted)
def view_passwords():
    key = load_key()
    f = Fernet(key)

    if not os.path.exists("passwords.txt"):
        print("⚠️ No passwords stored yet.")
        return

    with open("passwords.txt", "r") as f_file:
        for line in f_file.readlines():
            account, enc_pwd = line.strip().split(" | ")
            try:
                decrypted = f.decrypt(enc_pwd.encode()).decode()
                print(f" {account}: {decrypted}")
            except:
                print(f" Could not decrypt password for {account}")


def main():
    if not os.path.exists("secret.key"):
        generate_key()

    while True:
        print("\n=== Password Manager ===")
        print("1. Add new password")
        print("2. View saved passwords")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            acc = input("Enter account/site name: ")
            pwd = input("Enter password: ")
            add_password(acc, pwd)
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            print(" Exiting Password Manager. Stay safe!")
            break
        else:
            print(" Invalid option. Try again.")

if __name__ == "__main__":
    main()
