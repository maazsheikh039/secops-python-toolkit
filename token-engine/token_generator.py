#!/usr/bin/env python3
"""
Secure Token Generator
Generates cryptographically secure tokens for various purposes
"""

import secrets
import string
import hashlib
from datetime import datetime

def generate_hex_token(length=32):
    """
    Generate a hexadecimal token.
    
    Args:
        length: Number of bytes (token will be 2x this in hex chars)
    
    Returns:
        Hexadecimal string token
    """
    token = secrets.token_hex(length)
    return token


def generate_url_safe_token(length=32):
    """
    Generate a URL-safe token (base64 encoded).
    
    Args:
        length: Number of bytes
    
    Returns:
        URL-safe string token
    """
    token = secrets.token_urlsafe(length)
    return token


def generate_alphanumeric_token(length=16):
    """
    Generate an alphanumeric token.
    
    Args:
        length: Number of characters
    
    Returns:
        Alphanumeric string token
    """
    alphabet = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(alphabet) for i in range(length))
    return token


def main():
    print("=== Secure Token Generator ===\n")
    
    print("1. Hexadecimal Token (64 chars):")
    hex_token = generate_hex_token(32)
    print(f"   {hex_token}\n")
    
    print("2. URL-Safe Token:")
    url_token = generate_url_safe_token(32)
    print(f"   {url_token}\n")
    
    print("3. Alphanumeric Token (16 chars):")
    alpha_token = generate_alphanumeric_token(16)
    print(f"   {alpha_token}\n")


if __name__ == "__main__":
    main()
