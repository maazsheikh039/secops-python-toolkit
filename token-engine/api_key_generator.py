#!/usr/bin/env python3
"""
API Key and Secret Generator
Creates API keys with prefixes and associated secrets
"""

import secrets
import string
import json
import os
from datetime import datetime

def generate_api_key(prefix="sk", length=32):
    """
    Generate an API key with a prefix.
    
    Args:
        prefix: String prefix for the key (e.g., 'sk' for secret key)
        length: Length of the random portion
    
    Returns:
        API key string with prefix
    """
    alphabet = string.ascii_letters + string.digits
    random_part = ''.join(secrets.choice(alphabet) for i in range(length))
    api_key = f"{prefix}_{random_part}"
    return api_key


def generate_secret_key(length=64):
    """
    Generate a secret key for signing/encryption.
    
    Args:
        length: Number of bytes
    
    Returns:
        Hexadecimal secret key
    """
    return secrets.token_hex(length)


def generate_password(length=16, use_special=True):
    """
    Generate a secure random password.
    
    Args:
        length: Password length
        use_special: Include special characters
    
    Returns:
        Secure password string
    """
    alphabet = string.ascii_letters + string.digits
    if use_special:
        alphabet += string.punctuation
    
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password


def save_credentials(filename, credentials):
    """
    Save credentials to a JSON file securely.
    
    Args:
        filename: Output file path
        credentials: Dictionary of credentials
    """
    with open(filename, 'w') as f:
        json.dump(credentials, f, indent=2)
    
    # Set restrictive file permissions (owner read/write only: 600)
    os.chmod(filename, 0o600)


def main():
    print("=== API Key and Secret Generator ===\n")
    
    credentials = {
        "generated_at": datetime.now().isoformat(),
        "api_key": generate_api_key("sk", 32),
        "api_secret": generate_secret_key(64),
        "webhook_secret": generate_secret_key(32),
        "admin_password": generate_password(20, use_special=True),
        "database_password": generate_password(24, use_special=True)
    }
    
    print("Generated Credentials:")
    print("-" * 60)
    for key, value in credentials.items():
        if key != "generated_at":
            print(f"{key:20s}: {value}")
    print("-" * 60)
    
    output_file = "credentials.json"
    save_credentials(output_file, credentials)
    print(f"\nCredentials saved to: {output_file}")
    print("File permissions set to 600 (owner read/write only)")


if __name__ == "__main__":
    main()
