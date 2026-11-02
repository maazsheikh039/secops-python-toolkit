# Secure Input Sanitizer and Validation Engine

A modular Python security utility designed to prevent injection attacks, path traversal, cross-site scripting (XSS), and SQL manipulation by enforcing strict input validation, sanitization, and HTML escaping.

## Objectives
- Neutralize command injection vectors and malicious shell metacharacters.
- Prevent path traversal vulnerabilities during file system access operations.
- Detect potential SQL injection keywords and syntax patterns.
- Secure web outputs against XSS via robust HTML entity escaping.

## Tools Used
- **Python 3** (`re`, `html`, `os`)
- **Linux CLI / Bash**

## Key Skills Demonstrated
- **Application Security & Defensive Programming:** Mitigating OWASP Top 10 injection risks.
- **Regular Expression Filtering:** Precise character class validation and enforcement.
- **Modular Architecture:** Reusable security libraries for backend integration.

## Troubleshooting Log
- *Path Traversal Exploits:* Prevented via `os.path.basename()` and strict regex filtering.
- *SQL Keyword Matching:* Implemented case-insensitive substring checks against high-risk SQL directives.
