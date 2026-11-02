"""
Test script for security utility library.
"""

import sys
import os
sys.path.insert(0, '/home/ubuntu/security-lab5')

from securitylib.password import validator
from securitylib.hash import hasher

def test_password_validation():
    """Test password validation functions."""
    print("=== Testing Password Validation ===\n")
    
    test_passwords = [
        "weak",
        "StrongPass123!",
        "noupppercase123!",
        "NOLOWERCASE123!",
        "NoDigitsHere!",
        "NoSpecialChar123"
    ]
    
    for pwd in test_passwords:
        result = validator.validate_password(pwd)
        print(f"Password: {pwd}")
        print(f"Valid: {result['valid']}")
        if not result['valid']:
            print(f"Errors: {', '.join(result['errors'])}")
        print()


def test_hashing():
    """Test hashing functions."""
    print("=== Testing Hash Functions ===\n")
    
    # Test string hashing
    test_data = "SecureData123"
    hash_result = hasher.hash_sha256(test_data)
    print(f"Data: {test_data}")
    print(f"SHA-256: {hash_result}\n")
    
    # Test hash verification
    is_valid = hasher.verify_hash(test_data, hash_result)
    print(f"Hash verification: {is_valid}\n")
    
    # Test file hashing
    test_file_path = '/tmp/test_file.txt'
    with open(test_file_path, 'w', encoding='utf-8') as f:
        f.write("Test file content for hashing")
    
    file_hash = hasher.hash_file(test_file_path)
    print(f"File hash: {file_hash}\n")


if __name__ == "__main__":
    test_password_validation()
    test_hashing()
    print("=== All Tests Complete ===")
