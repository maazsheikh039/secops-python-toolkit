# Login Anomaly Detection System

## Objectives
- Parse and analyze authentication telemetry datasets using Pandas dataframes.
- Establish baseline user behavior profiles based on successful historical login hours and geographic locations.
- Implement multi-vector heuristic anomaly detection covering temporal, spatial, and frequency-based intrusion patterns.
- Automate security audit report generation for Security Operations Center (SOC) analysis.

## Tools Used
- **Python 3 `pandas`**: High-performance dataframe manipulation and time-series extraction.
- **Python `datetime` & `collections`**: Temporal window calculations and frequency aggregation.
- **CSV Telemetry Datasets**: Structured log ingestion.

## Key Skills Demonstrated
- Behavioral analytics and user profiling for enterprise security monitoring.
- Multi-vector threat detection (time anomalies, geo-location anomalies, and high-frequency brute-force attempts).
- Automated SIEM log processing and report compilation.

## Troubleshooting Log
- **Relative Timestamp Windows**: Adjusted frequency anomaly windows to evaluate against dataset maxima rather than system clock time, ensuring robust evaluation on static test logs.
- **Dataframe Indexing**: Utilized boolean masking and iterative row parsing to efficiently isolate multi-variable anomalous records.
