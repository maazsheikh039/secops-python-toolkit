# Identity and Access Management (IAM) Risk Scoring & Anomaly Detection System

## Objectives
- Quantify IAM risk by combining multi-factor vectors including role permissions, behavioral activity patterns, and account security hygiene.
- Implement weighted risk calculation algorithms normalized across distinct scoring bands (Critical, High, Medium, Low).
- Detect behavioral anomalies using statistical standard deviation thresholds against peer group baselines.
- Automate executive risk assessment reporting and export audit summaries to CSV formats.

## Tools Used
- **Python 3 `pandas` & `statistics`**: Dataframe aggregations, calculations, and statistical standard deviation metrics.
- **JSON Data Generation**: Structured simulation of administrative and standard user telemetry.

## Key Skills Demonstrated
- Identity Governance and Administration (IGA) risk modeling.
- Statistical anomaly detection for insider threat and compromised account identification.
- Automated security posture assessment reporting.

## Troubleshooting Log
- **Standard Deviation Edge Cases**: Added safeguards to verify dataset length and standard deviation values prior to threshold evaluations to prevent division errors on uniform sample lists.
- **Score Capping**: Implemented maximum ceiling caps (`min(score, max_limit}`) across modular risk components to maintain stable and predictable risk weighting scales.
