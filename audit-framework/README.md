o# Cloud Security Audit & Compliance Engine

## Objectives
- Parse and analyze multi-format system configuration artifacts (SSH settings, JSON firewall rules, YAML user permission tables).
- Ingest and evaluate authentication and web access logs using regular expressions and frequency counters.
- Compute a weighted security compliance score (0-100) based on vulnerability severities (Critical, High, Medium, Low).
- Compile executive HTML compliance reports for audit readiness and stakeholder review.

## Tools Used
- **Python 3 `json`, `yaml`, `re`, `collections`**: Structured data parsing, log pattern analysis, and score calculation.
- **`jq`**: Command-line JSON verification and metric inspection.

## Key Skills Demonstrated
- Cloud Security Posture Management (CSPM) and artifact auditing.
- Automated compliance framework construction and scoring normalization.
- Security reporting and executive dashboard compilation.

## Troubleshooting Log
- **Directory Auto-Creation**: Added `os.makedirs` routines to ensure report output directories are created prior to JSON and HTML writes.
- **Severity Weighting**: Standardized penalty scales in `generate_report.py` to ensure accurate compliance scoring across mixed finding types.
