# Encrypted Evidence Vault and DFIR Storage System

A robust, enterprise-grade digital forensics storage framework built upon Linux LUKS (`cryptsetup`) encryption, automated keyfile management, SHA-256 integrity verification, and GPG key backups.

## Objectives
- Create encrypted storage container volumes (`evidence_vault.img`) secured with LUKS AES-256 encryption.
- Implement multi-factor access control supporting both passphrases and randomized cryptographic keyfiles.
- Build automated management scripts (`vault_manager.sh`) for seamless mounting, unmounting, and status audits.
- Enforce evidence integrity checks via SHA-256 manifest validation (`verify_evidence.sh`).
- Maintain immutable operational audit trails (`audit_log.sh`) and secure GPG key backups.

## Tools Used
- **Encryption & Storage:** `cryptsetup` (LUKS), `dd`, `mkfs.ext4`
- **Security & Integrity:** `gpg`, `sha256sum`
- **Bash Scripting & Linux CLI**

## Key Skills Demonstrated
- **Data-at-Rest Encryption:** Protecting sensitive forensic evidence from unauthorized extraction or media theft.
- **Key Management & Access Control:** Automating secure container unlocking using least-privilege keyfiles.
- **Chain of Custody Enforcement:** Validating artifact integrity and logging administrative access events.

## Troubleshooting Log
- *Non-Interactive LUKS Setup:* Configured batch-mode piping to initialize LUKS containers cleanly within automated provisioning scripts.
- *Mount Point Permissions:* Ensured mount directories are provisioned correctly prior to mounting mapped LUKS block devices.
