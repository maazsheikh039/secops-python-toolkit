# test_salt.py
import bcrypt

password = "SamePassword123"

print("Hashing the same password 3 times:\n")

for i in range(3):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    print(f"Hash {i+1}: {hashed.decode('utf-8')}")

print("\nNotice: Each hash is different due to unique salt!")
print("This prevents rainbow table attacks.")
