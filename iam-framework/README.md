# Identity and Access Management (IAM) Risk Analysis Framework

## Objectives
- Ingest and correlate multi-source IAM datasets (user identities, resource permission matrices, and behavioral activity logs).
- Calculate granular permission risk scores based on access privilege tiers (Admin vs Write vs Read).
- Assess behavioral risk scores by tracking anomalous indicators (after-hours logins, failed authentication bursts, and high-risk operations).
- Compute weighted composite risk scores to classify users into risk bands (High, Medium, Low) and generate structured forensic audit reports.

## Tools Used
- **Python 3 `json`, `pandas`, `collections`**: Structured JSON data ingestion, relational mapping, and statistical aggregation.
- **File Automation**: Automated report compilation and directory provisioning.

## Key Skills Demonstrated
- Identity Governance and Administration (IGA) risk modeling.
- Behavioral analytics and privilege correlation for insider threat detection.
- Compliance reporting and risk prioritization.

## Troubleshooting Log
- **Directory Path Provisioning**: Added `os.makedirs` routines to ensure report output directories are dynamically created prior to text file writes.
- **Relational Joining**: Handled missing or unmapped user keys gracefully during data correlation across multiple JSON collections.
