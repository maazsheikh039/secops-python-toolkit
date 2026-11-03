# secure_password_manager.py
import bcrypt
import json
import os

class SecurePasswordManager:
    """
    A secure password manager using bcrypt for hashing and salting
    """
    
    def __init__(self, storage_file='secure_passwords.json'):
        """
        Initialize the password manager
        
        Args:
            storage_file: JSON file to store hashed passwords
        """
        self.storage_file = storage_file
        self.users = self._load_users()
    
    def _load_users(self):
        """
        Load existing users from storage file
        
        Returns:
            Dictionary of users and their hashed passwords
        """
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}
    
    def _save_users(self):
        """
        Save users dictionary to storage file
        """
        with open(self.storage_file, 'w', encoding='utf-8') as f:
            json.dump(self.users, f, indent=2)
    
    def hash_password(self, password):
        """
        Hash a password with automatic salt generation
        
        Args:
            password: Plain text password string
            
        Returns:
            Hashed password as string
        """
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password_bytes, salt)
        return hashed.decode('utf-8')
    
    def register_user(self, username, password):
        """
        Register a new user with hashed password
        
        Args:
            username: Username string
            password: Plain text password
            
        Returns:
            True if successful, False if user exists
        """
        if username in self.users:
            print(f"[ERROR] User '{username}' already exists")
            return False
        
        hashed_password = self.hash_password(password)
        self.users[username] = hashed_password
        self._save_users()
        print(f"[SUCCESS] User '{username}' registered successfully")
        return True
    
    def verify_password(self, username, password):
        """
        Verify a user's password
        
        Args:
            username: Username to verify
            password: Plain text password to check
            
        Returns:
            True if password matches, False otherwise
        """
        if username not in self.users:
            print(f"[ERROR] User '{username}' not found")
            return False
        
        stored_hash = self.users[username].encode('utf-8')
        password_bytes = password.encode('utf-8')
        
        result = bcrypt.checkpw(password_bytes, stored_hash)
        
        if result:
            print(f"[SUCCESS] Password verified for '{username}'")
        else:
            print(f"[FAILED] Invalid password for '{username}'")
        
        return result
    
    def list_users(self):
        """
        List all registered usernames (not passwords!)
        """
        return list(self.users.keys())


if __name__ == "__main__":
    print("=== SECURE PASSWORD MANAGER ===\n")
    manager = SecurePasswordManager()
    
    print("--- Registering Users ---")
    manager.register_user("alice", "SecurePass123!")
    manager.register_user("bob", "MyP@ssw0rd")
    manager.register_user("alice", "duplicate")
    
    print("\n--- Verifying Passwords ---")
    manager.verify_password("alice", "SecurePass123!")
    manager.verify_password("alice", "WrongPassword")
    manager.verify_password("bob", "MyP@ssw0rd")
    manager.verify_password("charlie", "anything")
    
    print("\n--- Registered Users ---")
    print(f"Users: {manager.list_users()}")
