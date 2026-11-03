# password_cli.py
from secure_password_manager import SecurePasswordManager
import getpass

def main():
    """
    Interactive command-line interface for password management
    """
    manager = SecurePasswordManager()
    
    print("=" * 50)
    print("SECURE PASSWORD MANAGEMENT SYSTEM")
    print("=" * 50)
    
    while True:
        print("\nOptions:")
        print("1. Register new user")
        print("2. Login (verify password)")
        print("3. List users")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == "1":
            username = input("Enter username: ").strip()
            password = getpass.getpass("Enter password: ")
            manager.register_user(username, password)
            
        elif choice == "2":
            username = input("Enter username: ").strip()
            password = getpass.getpass("Enter password: ")
            if manager.verify_password(username, password):
                print(f"\nWelcome, {username}!")
            else:
                print("\nAccess denied!")
            
        elif choice == "3":
            users = manager.list_users()
            print(f"\nRegistered users: {', '.join(users) if users else 'None'}")
            
        elif choice == "4":
            print("\nGoodbye!")
            break
            
        else:
            print("\n[ERROR] Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
