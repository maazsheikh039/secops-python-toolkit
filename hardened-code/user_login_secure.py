import sqlite3
import hashlib

def hash_password(password):
    """
    Hash password using SHA-256.
    In production, use bcrypt or argon2.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate_user(username, password):
    """
    Securely authenticate user against database.
    SECURE: Uses parameterized queries.
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # SECURE: Parameterized query prevents SQL injection
    query = "SELECT * FROM users WHERE username=? AND password=?"
    hashed_pwd = hash_password(password)
    cursor.execute(query, (username, hashed_pwd))
    
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return True
    return False

def validate_username(username):
    """
    Validate username format.
    """
    if not username or len(username) > 50:
        return False
    return username.replace('_', '').isalnum()

if __name__ == "__main__":
    user = input("Enter username: ")
    
    if not validate_username(user):
        print("Invalid username format!")
        exit(1)
    
    pwd = input("Enter password: ")
    
    if authenticate_user(user, pwd):
        print("Login successful!")
    else:
        print("Login failed!")
