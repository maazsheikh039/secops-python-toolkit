# Log Line Parsing, Tokenization, and Analytics Utility

A robust Python-based log processing engine designed to ingest raw system logs, parse structured telemetry using regular expressions, validate IP addresses, generate operational statistics, and export cleansed data to CSV format.

## Objectives
- Extract structured components (timestamps, IP addresses, log levels, messages) from raw log streams.
- Tokenize log message strings for deep pattern analysis.
- Validate source IPv4 addresses against network octet standards.
- Compute aggregate metrics and frequency counts using `collections.Counter`.
- Export structured telemetry into CSV reports for downstream SIEM integration.

## Tools Used
- **Python 3** (`re`, `datetime`, `collections`, `csv`, `typing`)
- **Linux CLI / Bash**

## Key Skills Demonstrated
- **Log Parsing & Telemetry Extraction:** Regular expression group capturing for structured log analysis.
- **Data Engineering & Aggregation:** Statistical summarization and frequency distribution tracking.
- **File I/O & Data Export:** Automated CSV report generation from parsed data dictionaries.

## Troubleshooting Log
- *Regex Capture Precision:* Ensured non-greedy and precise character classes (`\S+`, `\w+`) to safely handle variable-length message payloads.
- *Encoding Safety:* Explicitly defined `encoding='utf-8'` during file read and CSV write operations to prevent platform-specific decoding errors.
