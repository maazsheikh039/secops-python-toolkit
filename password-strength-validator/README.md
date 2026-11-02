# Password Strength Validation and Security Audit Tool

A robust Python-based command-line security utility designed to evaluate credential complexity, enforce password length policies, detect dictionary vulnerabilities, and calculate quantitative strength scores using regular expression analysis and heuristic pattern matching.

## Objectives
- Enforce strict enterprise password compliance (length, character classes).
- Prevent deployment of weak, blacklisted, or dictionary-based credentials.
- Detect structural anomalies such as sequential characters and character repetition.
- Provide actionable user feedback and automated batch auditing capabilities.

## Tools Used
- **Python 3** (Standard Libraries: `re`, `sys`, `os`)
- **Linux CLI / Bash** (Environment orchestration & file management)

## Key Skills Demonstrated
- **Application Security & Secure Coding:** Implementing defense-in-depth through multi-layered validation logic.
- **Regular Expressions (Regex):** Advanced pattern matching for character sets, sequences, and repetitions.
- **Automated Compliance Auditing:** Building batch-processing utilities for security analysis.

## Troubleshooting Log
- *File Not Found:* Resolved by implementing robust error handling (`try/except FileNotFoundError`) during external dictionary file loading.
- *Case Sensitivity:* Ensured case-insensitive checks against blacklisted dictionary words by normalizing input strings.
