# Observability Stack & Incident Response Drill Framework

## Objectives
- Deploy and configure an end-to-end observability stack with Prometheus, Grafana, Node Exporter, Loki, and Promtail.
- Instrument a Python Flask application with Prometheus client counters, histograms, and gauges.
- Define custom Prometheus alerting rules for high CPU usage, memory pressure, and low disk space.
- Execute simulated failure drills using `stress-ng` and traffic generators to validate incident response workflows.

## Tools Used
- **Prometheus & Node Exporter**: Time-series metrics collection and hardware telemetry.
- **Grafana**: Visualization and dashboarding platform.
- **Loki & Promtail**: Centralized log aggregation and log scraping agents.
- **Python Flask & `stress-ng`**: Instrumented application workload and system load testing tool.

## Key Skills Demonstrated
- SRE observability pipeline architecture and deployment.
- Alert rule engineering and threshold tuning.
- Chaos engineering and incident response validation.

## Troubleshooting Log
- **Systemd User Context**: Configured service user accounts (`prometheus`) correctly to maintain secure separation across telemetry components.
- **Log Path Resolution**: Ensured Promtail scrapers point accurately to home directory application log volumes.
