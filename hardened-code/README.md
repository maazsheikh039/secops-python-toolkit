# Hardening AI-Generated Insecure Code & Static Analysis

## Objectives
- Identify and analyze common security vulnerabilities in AI-generated code (SQL Injection, Path Traversal, and Command Injection).
- Execute static security analysis scans using Bandit to automatically discover high-risk code patterns.
- Refactor and harden insecure scripts using industry-best secure coding practices (parameterized queries, path validation, and subprocess argument lists).
- Verify remediation efficacy through comparative static analysis.

## Tools Used
- **Bandit**: Static application security testing (SAST) tool for Python.
- **Python 3 Standard Libraries (`sqlite3`, `pathlib`, `subprocess`, `re`)**: Secure database handling, path containment, and process execution.

## Key Skills Demonstrated
- Secure code review and vulnerability remediation for AI-generated assets.
- Input sanitization, strict regex validation, and parameterized query construction.
- Defensive programming principles and SAST pipeline integration.

## Troubleshooting Log
- **Path Traversal Constraints**: Implemented `.resolve()` and `.relative_to()` boundary checks using `pathlib` to prevent directory traversal outside sandbox upload directories.
- **Shell Injection Elimination**: Replaced insecure `os.system` string concatenations with argument arrays passed to `subprocess.run`.
