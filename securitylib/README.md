# Modular Security Utility Library in Python

A production-grade, modular Python security library providing reusable components for credential compliance validation, cryptographic hashing, and file integrity verification.

## Objectives
- Implement modular software architecture using Python packages and submodules (`securitylib/password`, `securitylib/hash`).
- Provide robust password complexity enforcement (length, uppercase, lowercase, digits, special characters).
- Perform cryptographic SHA-256 hashing and stream-based file integrity verification.
- Establish an automated testing framework and an interactive CLI management tool.

## Tools Used
- **Python 3** (`hashlib`, `re`, `sys`, `os`)
- **Linux CLI / Bash**

## Key Skills Demonstrated
- **Modular Software Design:** Structuring code into clean, importable Python packages with explicit initializers (`__init__.py`).
- **Cryptographic Operations:** Secure string and binary file hashing via standard libraries.
- **Test-Driven Architecture:** Creating comprehensive validation test suites.

## Troubleshooting Log
- *Module Import Resolution:* Ensured explicit path insertion (`sys.path.insert(0, ...)`) and correct package directory hierarchies.
- *Binary File Hashing:* Implemented chunked read buffering (`b""` iterator) in `hash_file` to handle large files efficiently without memory overhead.
