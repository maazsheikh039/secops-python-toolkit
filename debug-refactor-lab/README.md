# Script Debugging, Refactoring, and Security Hardening Suite

A comprehensive collection of remediation exercises fixing critical security flaws (command injection, hardcoded credentials), logic bypasses, and unhandled runtime exceptions across Python and Bash automation scripts.

## Objectives
- Eliminate plaintext hardcoded credentials by implementing cryptographic hashing (`hashlib`).
- Prevent command injection vulnerabilities by replacing shell concatenation with safe process execution (`subprocess.run`).
- Fix logical authentication errors and enforce strict input validation.
- Refactor Bash automation scripts using robust error handling (`set -euo pipefail`), quoted variables, and static analysis tools (`shellcheck`).

## Tools Used
- **Python 3** (`subprocess`, `hashlib`, `sys`)
- **Bash & ShellCheck** (Static code analysis)
- **Linux CLI / Bash**

## Key Skills Demonstrated
- **Secure Code Review & Remediation:** Identifying and patching OWASP Top 10 vulnerabilities in legacy scripts.
- **Defensive Shell Scripting:** Eliminating word-splitting bugs, unquoted variables, and unchecked command failures.
- **Exception & Error Handling:** Implementing context managers (`with` blocks) and graceful failure modes.

## Troubleshooting Log
- *Command Injection Mitigation:* Substituted insecure `os.system()` string concatenation with structured `subprocess.run()` arguments list.
- *Bash Pipe Failures:* Enabled strict pipeline exit status propagation via `set -o pipefail`.
