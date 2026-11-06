# Secure Prompt Engineering & LLM Hardening Framework

## Objectives
- Identify and analyze prompt injection vulnerabilities caused by direct string concatenation in LLM pipelines.
- Implement regex-based sanitization and input validation routines to filter malicious command overrides.
- Design structured prompts featuring clear role definitions, instruction hierarchies, and explicit boundary delimiters.
- Build advanced defense-in-depth mechanisms including request signatures, rate limiting, and anomaly detection.

## Tools Used
- **Python 3 `re`, `hashlib`, `json`**: Regular expressions, cryptographic hashing, and structured data handling.
- **Security Testing Suites**: Automated validation harnesses for prompt defense verification.

## Key Skills Demonstrated
- Large Language Model (LLM) security hardening and prompt engineering.
- Input filtering and jailbreak prevention techniques.
- Defense-in-depth architecture for AI applications.

## Troubleshooting Log
- **Regex Case-Insensitivity**: Utilized `re.IGNORECASE` flags across all injection pattern filters to catch varied capitalization bypasses.
- **Delimiter Containment**: Established explicit `USER QUERY START` and `USER QUERY END` markers to segregate trusted system rules from untrusted user inputs.
