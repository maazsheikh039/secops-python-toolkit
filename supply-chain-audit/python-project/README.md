# Software Supply Chain Vulnerability & Dependency Scanner

## Objectives
- Configure multi-ecosystem dependency scanning tools (OWASP Dependency-Check, `npm audit`, and `Safety`).
- Generate and ingest vulnerability reports for vulnerable Node.js and Python software packages.
- Analyze Common Vulnerabilities and Exposures (CVEs) across critical, high, and moderate severity tiers.
- Execute remediation workflows via automated auditing and locked dependency upgrades.

## Tools Used
- **OWASP Dependency-Check**: Enterprise software bill of materials (SBOM) and vulnerability scanner.
- **npm audit**: Node.js ecosystem vulnerability detector and patch manager.
- **Safety**: Python package advisory scanner.

## Key Skills Demonstrated
- Software supply chain security management and dependency auditing.
- Automated vulnerability identification and CVE risk assessment.
- Remediation engineering and dependency version pinning.

## Troubleshooting Log
- **Virtual Environment Management**: Utilized isolated python virtual environments (`venv`) to prevent system-wide package pollution during dependency installations.
- **Dependency Database Caching**: Handled first-run download overhead for OWASP Dependency-Check rulesets successfully.
