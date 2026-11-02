#!/usr/bin/env python3
import os
import sys
import hashlib
import subprocess

ADMIN_PASSWORD_HASH = hashlib.sha256("admin123".encode()).hexdigest()

def authenticate_user(username, password):
    """
    Authenticate user with proper logic and hashed verification.
    """
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    if username == "admin" and password_hash == ADMIN_PASSWORD_HASH:
        return True
    return False

def list_users():
    """
    List system users safely without command injection.
    """
    try:
        result = subprocess.run(
            ["grep", "/bin/bash", "/etc/passwd"],
            capture_output=True,
            text=True,
            timeout=5
        )
        print(result.stdout)
    except subprocess.TimeoutExpired:
        print("Command timed out")
    except Exception as e:
        print(f"Error listing users: {e}")

def add_user(username):
    """
    Add user to list with validation and proper file handling.
    """
    if not username.isalnum() or len(username) < 3 or len(username) > 20:
        print("Invalid username. Use 3-20 alphanumeric characters.")
        return
    
    try:
        with open("/tmp/users.txt", "a") as file:
            file.write(username + "\n")
        print(f"User '{username}' added successfully")
    except IOError as e:
        print(f"Error writing to file: {e}")

def read_users():
    """
    Read users from file with error handling and context managers.
    """
    try:
        with open("/tmp/users.txt", "r") as file:
            users = file.read()
        return users if users else "No users found"
    except FileNotFoundError:
        return "User file not found. Add users first."
    except IOError as e:
        return f"Error reading file: {e}"

def main():
    print("User Management System (Secure Version)")
    print("1. Authenticate")
    print("2. List system users")
    print("3. Add user to list")
    print("4. Read user list")
    print("5. Exit")
    
    choice = input("Enter choice (1-5): ").strip()
    
    if not choice.isdigit() or int(choice) not in range(1, 6):
        print("Invalid choice. Please enter 1-5.")
        return
    
    choice = int(choice)
    
    if choice == 1:
        user = input("Username: ").strip()
        pwd = input("Password: ").strip()
        if authenticate_user(user, pwd):
            print("Access granted")
        else:
            print("Access denied")
    elif choice == 2:
        list_users()
    elif choice == 3:
        name = input("Enter username: ").strip()
        add_user(name)
    elif choice == 4:
        print(read_users())
    elif choice == 5:
        print("Exiting...")
        sys.exit(0)

if __name__ == "__main__":
    main()
