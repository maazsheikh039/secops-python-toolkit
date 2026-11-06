# Local Object Storage Exposure Simulator & Scanner

## Objectives
- Deploy and configure a local S3-compatible object storage server (MinIO) inside an isolated test environment.
- Provision storage buckets with intentionally misconfigured public read access control lists (ACLs).
- Upload confidential assets (customer databases, API keys, financial ledgers) to validate exposure risks.
- Build automated shell scanning utilities to audit bucket policies and verify unauthenticated resource accessibility.

## Tools Used
- **MinIO Server & Client (`mc`)**: S3-compatible object storage and administrative management CLI.
- **`curl` & Bash Scripting**: HTTP endpoint probing and vulnerability scanner automation.

## Key Skills Demonstrated
- Cloud Security Posture Management (CSPM) and object storage auditing.
- Threat simulation for data exposure vectors (public bucket misconfigurations).
- Automated security scanning and compliance report generation.

## Troubleshooting Log
- **MinIO Background Execution**: Managed background process lifecycle cleanly using persistent redirection and PID tracking.
- **Anonymous Policy Validation**: Queried MinIO access policies using explicit `mc anonymous list` commands to confirm anonymous download vector exposures.
