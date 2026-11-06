# Secure Evidence Collection and Reporting System (DFIR Pipeline)

## Objectives
- Deploy a structured digital forensics evidence collection framework with strict directory isolation.
- Acquire forensically sound copies of suspicious files using `dcfldd` while computing simultaneous MD5 and SHA256 cryptographic checksums.
- Enforce strict read-only file permissions (`444`) on original evidence vaults to prevent data tampering.
- Maintain immutable chain of custody logs and generate automated forensic inventory reports via Python.

## Tools Used
- **`dcfldd` & `md5deep`**: Forensic disk and file acquisition utilities with built-in hashing.
- **Python 3 `hashlib` & `pathlib`**: Checksum calculation and file metadata analysis.
- **Linux File Permissions**: Access control list restriction for evidentiary integrity.

## Key Skills Demonstrated
- Digital Forensics and Incident Response (DFIR) evidence handling procedures.
- Cryptographic integrity verification via SHA256 manifests.
- Automated forensic report compilation and chain of custody documentation.

## Troubleshooting Log
- **Read-Only Preservation**: Applied explicit `chmod 444` rules immediately following `dcfldd` copying to guarantee original evidence immutability.
- **Path Resolution**: Utilized absolute `pathlib` references within Python reporting scripts to prevent working directory context errors.
