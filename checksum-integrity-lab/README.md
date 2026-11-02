# File Integrity and Checksum Verification Tool

A robust Bash-based security automation utility designed to generate cryptographic checksums (SHA-256, MD5), establish baseline manifests, and automate file integrity verification to detect unauthorized modifications or data corruption.

## Objectives
- Generate high-entropy cryptographic hash values for individual files and multi-file directories.
- Automate baseline snapshot generation using recursive file searches (`find` + `sha256sum`).
- Perform integrity audits against saved manifest files (`sha256sum -c`).
- Detect file tampering and corruption events programmatically via a unified CLI script.

## Tools Used
- **Coreutils:** `sha256sum`, `md5sum`
- **Bash Scripting & File Utilities:** `find`, `cat`
- **Linux CLI / SSH**

## Key Skills Demonstrated
- **Supply Chain Security:** Verifying file integrity prior to execution or deployment.
- **Cryptographic Hashing:** Utilizing SHA-256 for collision-resistant file fingerprinting.
- **Automation & Error Handling:** Building structured CLI scripts with switch-case dispatchers and status checks.

## Troubleshooting Log
- *Path Consistency:* Ensured relative file path references match the workspace directory structure during batch verification runs.
- *Coreutils Availability:* Verified standard POSIX hashing utilities are present across target Linux environments.
