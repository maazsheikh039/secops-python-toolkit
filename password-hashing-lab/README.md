# Password Hashing and Verification System

A secure credential management tool and demonstration suite built in Python implementing industry-standard cryptographic hashing (`bcrypt`) with dynamic salt generation to prevent rainbow table attacks and credential leaks.

## Objectives
- Contrast insecure plain-text credential storage with cryptographic hashing mechanisms.
- Implement automatic salt generation using `bcrypt.gensalt()` for every user registration.
- Build a secure verification pipeline (`bcrypt.checkpw`) resistant to timing attacks and reverse decryption.
- Provide both a programmatic library (`SecurePasswordManager`) and an interactive CLI tool (`password_cli.py`).

## Tools Used
- **Python 3** (`bcrypt`, `json`, `os`, `getpass`)
- **Linux CLI / SSH**

## Key Skills Demonstrated
- **Cryptographic Hashing:** Utilizing adaptive, one-way hash algorithms designed for password security.
- **Salting Implementation:** Defending against precomputed rainbow table lookups via unique randomized salts.
- **Defensive Credential Management:** Enforcing secure file storage formats (`secure_passwords.json`) that never expose plain-text secrets.

## Troubleshooting Log
- *Bcrypt Library Dependencies:* Ensured `bcrypt` module is correctly installed within the active Python environment.
- *String/Bytes Encoding:* Handled explicit UTF-8 string-to-byte conversions required by the bcrypt C-binding functions.
