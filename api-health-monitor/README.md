# Local Mock API Health Monitor

A robust Python-based reliability monitoring daemon and mock REST API service designed to track endpoint availability, measure latency, handle connection timeouts and HTTP error codes, and maintain persistent audit logs and JSON status manifests.

## Objectives
- Deploy a local Flask-based mock REST API service simulating random latency and intermittent HTTP 500 errors.
- Build an automated health monitoring agent that polls endpoints at configurable intervals.
- Measure HTTP response times in milliseconds and handle connection exceptions gracefully.
- Maintain persistent system logs and structured JSON status dashboards (`current_status.json`).

## Tools Used
- **Python 3** (`requests`, `flask`, `json`, `time`, `datetime`)
- **Linux CLI / Curl**

## Key Skills Demonstrated
- **Service Reliability Engineering (SRE):** Designing automated health check daemons for uptime tracking.
- **Error Handling & Resilience:** Catching network timeouts, connection drops, and HTTP error statuses without crashing.
- **Observability & Logging:** Generating timestamped operational logs and structured status state files.

## Troubleshooting Log
- *Port Bindings:* Ensured Flask runs cleanly on port 5000 and background PIDs are tracked for clean process termination.
- *Timeout Resilience:* Configured explicit request timeout thresholds (`timeout=5`) to prevent hanging monitor threads during unresponsive service states.
