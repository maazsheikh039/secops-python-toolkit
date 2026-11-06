# Cryptographic Token and Secret Generator Engine

## Objectives
- Implement cryptographically secure pseudo-random number generation using Python's `secrets` module.
- Build automated generators for hex tokens, URL-safe base64 tokens, alphanumeric API keys, and multi-factor authentication (TOTP) secrets.
- Enforce strict POSIX file permission hardening (`0o600`) on serialized credential files.
- Validate entropy strength and verify collision resistance across large token sets.

## Tools Used
- **Python 3 `secrets` Module**: Cryptographically strong random number generation.
- **Python `string` & `base64`**: Character set manipulation and encoding.
- **POSIX File System Permissions**: Access control list restriction (`chmod 600`).

## Key Skills Demonstrated
- Secure software development lifecycle (Secure SDLC) principles for credential management.
- Cryptographic entropy verification and collision avoidance testing.
- Automated secret provisioning and secure storage best practices.

## Troubleshooting Log
- **Permission Hardening**: Programmatically bound file write operations with explicit `os.chmod(filename, 0o600)` calls to eliminate risk of accidental world-readable secret exposure.
- **Entropy Guarantee**: Replaced all instances of pseudo-random `random` module calls with operating-system-backed entropy via `secrets`.
