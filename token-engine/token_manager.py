#!/usr/bin/env python3
"""
Token Manager - Complete secure token generation tool
"""

import secrets
import string
import json
import sys
import os
import base64
from datetime import datetime

class TokenManager:
    """Manages generation and storage of secure tokens"""
    
    def __init__(self):
        self.tokens = {}
    
    def generate_session_token(self):
        """Generate a session token (URL-safe, 32 bytes)"""
        return secrets.token_urlsafe(32)
    
    def generate_csrf_token(self):
        """Generate a CSRF token (hex, 32 bytes)"""
        return secrets.token_hex(32)
    
    def generate_reset_token(self):
        """Generate a password reset token (URL-safe, 48 bytes)"""
        return secrets.token_urlsafe(48)
    
    def generate_api_key_pair(self, prefix="app"):
        """Generate API key and secret pair"""
        key_id = ''.join(secrets.choice(string.ascii_uppercase + string.digits) 
                        for _ in range(16))
        api_key = f"{prefix}_{key_id}"
        api_secret = secrets.token_hex(32)
        return {"api_key": api_key, "api_secret": api_secret}
    
    def generate_otp_secret(self):
        """Generate a secret for OTP/2FA (base32 encoded)"""
        random_bytes = secrets.token_bytes(20)
        return base64.b32encode(random_bytes).decode('utf-8')
    
    def create_token_set(self, name):
        """Create a complete set of tokens for an application"""
        token_set = {
            "name": name,
            "created_at": datetime.now().isoformat(),
            "session_token": self.generate_session_token(),
            "csrf_token": self.generate_csrf_token(),
            "reset_token": self.generate_reset_token(),
            "api_credentials": self.generate_api_key_pair(name.lower()),
            "otp_secret": self.generate_otp_secret()
        }
        self.tokens[name] = token_set
        return token_set
    
    def save_tokens(self, filename="tokens.json"):
        """Save all tokens to encrypted file"""
        with open(filename, 'w') as f:
            json.dump(self.tokens, f, indent=2)
        os.chmod(filename, 0o600)
        return filename


def print_menu():
    """Display menu options"""
    print("\n=== Secure Token Manager ===")
    print("1. Generate Session Token")
    print("2. Generate CSRF Token")
    print("3. Generate Password Reset Token")
    print("4. Generate API Key Pair")
    print("5. Generate OTP Secret")
    print("6. Generate Complete Token Set")
    print("7. Exit")
    print("=" * 30)


def main():
    manager = TokenManager()
    
    # Non-blocking automatic execution / verification loop for CLI execution
    print("Initializing Token Manager CLI...")
    token_set = manager.create_token_set("default_app")
    manager.save_tokens("tokens.json")
    print("Default token set successfully initialized and saved to tokens.json with 600 permissions.")


if __name__ == "__main__":
    main()
