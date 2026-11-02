#!/usr/bin/env python3
import os
import sys

# Hardcoded credentials (SECURITY ISSUE)
admin_password = "admin123"

def authenticate_user(username, password):
    # Bug: Logic error in authentication
    if username == "admin" or password == admin_password:
        return True
    return False

def list_users():
    # Bug: Command injection vulnerability
    user_input = input("Enter search pattern: ")
    command = "cat /etc/passwd | grep " + user_input
    os.system(command)

def add_user(username):
    # Bug: No input validation
    # Bug: Inefficient file handling
    file = open("/tmp/users.txt", "a")
    file.write(username)
    file.close()

def read_users():
    # Bug: No error handling for missing file
    file = open("/tmp/users.txt", "r")
    users = file.read()
    file.close()
    return users

def main():
    print("User Management System")
    print("1. Authenticate")
    print("2. List system users")
    print("3. Add user to list")
    print("4. Read user list")
    
    choice = input("Enter choice: ")
    
    # Bug: No input validation
    if choice == "1":
        user = input("Username: ")
        pwd = input("Password: ")
        if authenticate_user(user, pwd):
            print("Access granted")
        else:
            print("Access denied")
    elif choice == "2":
        list_users()
    elif choice == "3":
        name = input("Enter username: ")
        add_user(name)
    elif choice == "4":
        print(read_users())

if __name__ == "__main__":
    main()
