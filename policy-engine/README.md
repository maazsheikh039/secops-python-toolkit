# Security Policy Misconfiguration Detection Engine

## Objectives
- Parse and analyze JSON-formatted security policy files (firewalls and access control lists).
- Implement algorithmic checks to detect overly permissive network sources (`0.0.0.0/0`).
- Identify conflicting firewall rules targeting identical traffic vectors with opposite actions.
- Audit access control lists for dangerous wildcard permissions and unauthorized sensitive resource access.

## Tools Used
- **Python 3 `json` & `sys`**: Structured policy ingestion and command-line parsing.
- **Object-Oriented Design**: Modular class architecture (`PolicyDetector`) separating rule validation functions.

## Key Skills Demonstrated
- Cloud Security Posture Management (CSPM) and policy auditing.
- Automated rule-base analysis for conflict detection and threat remediation.
- Security compliance verification.

## Troubleshooting Log
- **JSON File Loading**: Implemented resilient `FileNotFoundError` and `JSONDecodeError` blocks to handle missing configuration files or formatting errors gracefully.
- **Rule Collision Iteration**: Used pairwise index enumeration (`enumerate` and slicing) to accurately cross-compare network rules without redundant checks.
