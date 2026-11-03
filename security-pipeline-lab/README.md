# Event Alert Response Processing Pipeline

A robust, real-time security event monitoring and automated incident response (SOAR) pipeline written in Python that ingests log streams, correlates events against declarative YAML security rules, maintains threshold counters, and dispatches structured JSON alerts and automated response logs.

## Objectives
- Parse unstructured log streams reliably using standard delimiter parsing.
- Load dynamic security rules from external YAML configuration files.
- Track event frequencies across source IPs to enforce threshold triggers.
- Generate structured JSON incident alerts and automated response actions (`block_ip`, `alert_admin`, `log_only`).

## Tools Used
- **Python 3** (`yaml`, `json`, `time`, `collections`)
- **Linux CLI / Bash**

## Key Skills Demonstrated
- **SIEM & SOAR Engine Architecture:** Building event-driven threat detection and automated remediation loops.
- **Stateful Event Correlation:** Tracking cumulative attack patterns over time using threshold counters.
- **Artifact Generation:** Storing structured audit trails and forensic evidence in JSON format.

## Troubleshooting Log
- *File Tailing Synchronization:* Configured file pointer tracking and flush calls to ensure real-time daemon event ingestion during simulation runs.
- *YAML Dependency Management:* Verified `pyyaml` library availability within target runtime environments.
