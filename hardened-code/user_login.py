import sqlite3

def authenticate_user(username, password):
    """
    Authenticate user against database.
    WARNING: This code contains security vulnerabilities!
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # VULNERABLE: Direct string concatenation in SQL query
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return True
    return False

if __name__ == "__main__":
    user = input("Enter username: ")
    pwd = input("Enter password: ")
    
    if authenticate_user(user, pwd):
        print("Login successful!")
    else:
        print("Login failed!")
