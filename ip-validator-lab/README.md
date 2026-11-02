# Network Identifier Validation Toolkit

A modular Python security and network automation utility designed to validate, classify, and audit IPv4 addresses, IPv6 addresses, and hostnames according to strict RFC standards.

## Objectives
- Perform manual octet parsing and range validation for IPv4 identifiers.
- Leverage Python's `ipaddress` module for robust IPv6 address parsing.
- Enforce RFC-compliant hostname rules using regular expressions (label length limits, hyphen placement, character sets).
- Implement an automated dispatcher to detect and validate mixed network target formats.

## Tools Used
- **Python 3** (`ipaddress`, `re`)
- **Linux CLI / Bash**

## Key Skills Demonstrated
- **Network Engineering & Protocol Compliance:** Deep understanding of IP formatting and DNS naming standards.
- **Defensive Programming & Input Sanitization:** Preventing invalid routing or connection configs through rigorous parsing.
- **Regex Pattern Matching:** Validating structured sub-components in domain labels.

## Troubleshooting Log
- *Colon vs Dot Detection:* Resolved by pre-filtering input strings based on delimiter characteristics before parsing IPv4 vs IPv6 modules.
- *Label Boundary Checks:* Enforced strict anchoring in regex patterns to prevent illegal leading/trailing hyphens in hostnames.
