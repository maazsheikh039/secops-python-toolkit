# plain_text_demo.py
# This demonstrates INSECURE password storage (DO NOT USE IN PRODUCTION)

def store_password_insecure(username, password):
    """
    BAD PRACTICE: Storing passwords in plain text
    """
    with open('insecure_passwords.txt', 'a', encoding='utf-8') as f:
        f.write(f"{username}:{password}\n")
    print(f"[INSECURE] Stored password for {username}")

def verify_password_insecure(username, password):
    """
    BAD PRACTICE: Checking plain text passwords
    """
    try:
        with open('insecure_passwords.txt', 'r', encoding='utf-8') as f:
            for line in f:
                stored_user, stored_pass = line.strip().split(':')
                if stored_user == username and stored_pass == password:
                    return True
        return False
    except FileNotFoundError:
        return False

if __name__ == "__main__":
    print("=== INSECURE PASSWORD STORAGE DEMO ===")
    store_password_insecure("alice", "password123")
    store_password_insecure("bob", "qwerty456")
    
    print("\nVerifying passwords:")
    print(f"Alice login: {verify_password_insecure('alice', 'password123')}")
    print(f"Bob wrong password: {verify_password_insecure('bob', 'wrong')}")
    
    print("\n[WARNING] Check insecure_passwords.txt to see the danger!")
