# Cloud Audit Log Security Analyzer

## Objectives
- Parse and analyze JSON-formatted cloud audit log files programmatically.
- Implement security rule engines to detect high-risk administrative actions (e.g., encryption disabling, audit logging tampering, key creation).
- Perform pattern matching on cloud resource configuration details to identify critical infrastructure misconfigurations (e.g., open SSH security groups).
- Flag suspicious operational anomalies including failed access attempts, external user telemetry, and unusual access timestamps.

## Tools Used
- **Python 3 `json` & `sys`**: Structured data ingestion and command-line execution handling.
- **Python `collections` & `datetime`**: Telemetry grouping and temporal anomaly evaluation.
- **Colorama**: Terminal styling for security severity indicators.

## Key Skills Demonstrated
- Cloud Security Posture Management (CSPM) and log analysis automation.
- Threat hunting heuristic design for IAM and network security monitoring.
- Compliance reporting generation for audit readiness.

## Troubleshooting Log
- **JSON Encoding Safety**: Utilized explicit JSON serialization checks (`json.dumps`) to safely scan nested resource metadata for misconfiguration strings.
- **File Integrity Handling**: Incorporated robust `FileNotFoundError` and `JSONDecodeError` exception handlers to prevent script termination on malformed input.
