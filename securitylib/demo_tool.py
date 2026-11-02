#!/usr/bin/env python3
"""
Interactive demo of security utility library.
"""

from securitylib.password import validator
from securitylib.hash import hasher

def main():
    print("Security Utility Library Demo\n")
    print("1. Validate Password")
    print("2. Hash Data")
    print("3. Exit")
    
    choice = input("\nEnter choice (1-3): ").strip()
    
    if choice == "1":
        password = input("Enter password to validate: ")
        result = validator.validate_password(password)
        
        if result['valid']:
            print("\n✓ Password is strong!")
        else:
            print("\n✗ Password is weak:")
            for error in result['errors']:
                print(f"  - {error}")
    
    elif choice == "2":
        data = input("Enter data to hash: ")
        hash_value = hasher.hash_sha256(data)
        print(f"\nSHA-256 Hash: {hash_value}")
    
    elif choice == "3":
        print("Goodbye!")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
