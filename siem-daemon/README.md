# Automated Incident Alerting Service & SIEM Monitor

## Objectives
- Deploy an automated real-time log monitoring daemon parsing YAML-based security rules.
- Implement threshold-based event matching and pattern detection using Python's regular expressions (`re`).
- Construct structured alert formatting and multi-channel notification dispatch (console output and persistent incident logs).
- Simulate live Security Operations Center (SOC) incident workflows.

## Tools Used
- **Python 3 `yaml` & `re`**: Configuration parsing and regular expression pattern matching.
- **Python File Streaming**: Tail-like file monitoring (`seek(0, 2)` and continuous polling).
- **Persistent Audit Logging**: Automated incident record generation.

## Key Skills Demonstrated
- Real-time log monitoring and anomaly detection engine design.
- Threshold and state management for security alert suppression and dispatch.
- Security Information and Event Management (SIEM) workflow automation.

## Troubleshooting Log
- **File Tail Synchronization**: Configured file-pointer positioning (`f.seek(0, 2)`) to ensure incoming log writes are captured dynamically without processing historical logs on startup.
- **Threshold Reset Logic**: Implemented state reset counters upon alert dispatch to ensure recurring threat patterns trigger sequential notifications.
