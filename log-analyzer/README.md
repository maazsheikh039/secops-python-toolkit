ttack Detection Engine

## Objectives
- Parse unstructured authentication log data to extract timestamp, status, target username, and source IP vectors.
- Implement threshold-based heuristic detection algorithms for tracking repeated failed authentication attempts within configurable time windows.
- Automate security alert dispatch and persistent audit log generation for incident response workflows.

## Tools Used
- **Python 3 `datetime` & `collections`**: High-performance timestamp parsing and frequency mapping via `defaultdict`.
- **Linux Core Utilities**: `grep`, `wc`, file redirection.

## Key Skills Demonstrated
- Log parsing and string manipulation for security telemetry analysis.
- Heuristic anomaly detection design for identifying credential stuffing and brute-force intrusions.
- Automated security incident logging and audit trail reporting.

## Troubleshooting Log
- **Timestamp Parsing**: Standardized timestamp string combination (`date + time`) to ensure correct sequential calculation using Python `datetime.strptime`.
- **Threshold Tuning**: Configured window checks to ensure sliding-window threshold checks isolate malicious traffic without triggering false positives on dispersed failed logins.
