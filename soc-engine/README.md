# SOC Automation Platform & Threat Detection Engine

## Objectives
- Build a modular Security Operations Center (SOC) automation workflow on Linux.
- Implement continuous log generation simulating normal user activity and malicious threat vectors (brute-force attacks, port scans, and reverse shells).
- Construct a real-time threat detection engine using regular expression signatures.
- Automate security incident report compilation with metric summaries and remediation guidelines.

## Tools Used
- **Python 3 `re`, `random`, `datetime`, `collections`**: Regex pattern matching, randomized event simulation, and statistical categorization.
- **Linux Background Daemons**: Process management (`nohup` style background execution and PID file tracking).

## Key Skills Demonstrated
- Security Information and Event Management (SIEM) log parsing automation.
- Signature-based intrusion detection systems (IDS) engineering.
- Automated incident response reporting and threat analytics.

## Troubleshooting Log
- **File Pointer Synchronization**: Configured file-seeking routines (`f.seek(0, 2)`) in the threat detector to ensure continuous ingestion of live log streams.
- **Alert Line Parsing**: Implemented robust string splitting logic in `report_generator.py` to cleanly extract threat categories and timestamps from persisted alert files.
