# Automated Forensic Evidence Collection and Integrity Suite

A production-grade DFIR (Digital Forensics and Incident Response) automation tool written in Bash designed to capture critical volatile system telemetry, preserve logs securely, establish cryptographic chain-of-custody hashes, and package immutable evidence archives.

## Objectives
- Automate the collection of system metadata (hostname, uptime, kernel version, OS release).
- Capture current user sessions, process tables, network interfaces, routing tables, and socket listeners.
- Archive sensitive system and authentication logs (`auth.log`, `syslog`).
- Generate MD5 and SHA256 cryptographic hash manifests for every collected artifact to guarantee data integrity.
- Build automated verification and read-only tarball archiving pipelines.

## Tools Used
- **Coreutils:** `md5sum`, `sha256sum`, `date`, `hostname`, `du`, `find`
- **System Utilities:** `ip`, `ss`, `netstat`, `ps`, `w`, `last`, `lastb`
- **Bash Scripting & Linux CLI**

## Key Skills Demonstrated
- **Incident Response Automation:** Rapid, repeatable forensic triage of compromised hosts.
- **Chain of Custody & Integrity Verification:** Creating tamper-evident cryptographic manifests.
- **Defensive Hardening:** Enforcing read-only file permissions (`chmod 444`) on preserved evidence artifacts.

## Troubleshooting Log
- *Socket Tool Availability:* Integrated fallback handlers supporting both `ss` and `netstat` commands across varied Linux distributions.
- *Privilege Enforcement:* Requires root/sudo execution to successfully ingest restricted system logs and process lists.
