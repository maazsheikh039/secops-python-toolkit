# HTTP Header Inspection and Security Analysis Tool

A robust Python command-line utility designed to fetch, parse, and evaluate HTTP response headers against OWASP security header recommendations and best practices.

## Objectives
- Fetch HTTP response headers securely with timeout protection and SSL fallback handling.
- Audit target URLs for missing critical security headers (`Strict-Transport-Security`, `Content-Security-Policy`, `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`, etc.).
- Detect insecure header configurations and weak parameters (e.g., short HSTS max-age, disabled XSS filtering).
- Present color-coded terminal reports for immediate vulnerability triage.

## Tools Used
- **Python 3** (`requests`, `sys`, `colorama`)
- **Linux CLI / SSH**

## Key Skills Demonstrated
- **Web Application Security Assessment:** Auditing security headers to prevent clickjacking, MIME sniffing, and MITM downgrade attacks.
- **HTTP Protocol Analysis:** Programmatically inspecting server response metadata.
- **CLI Tool Development:** Building user-friendly security utilities with formatted ANSI color output.

## Troubleshooting Log
- *SSL Certificate Handling:* Integrated automatic fallback handling for self-signed or invalid certificates during testing runs.
- *Case Insensitivity:* Normalized HTTP header keys to guarantee accurate dictionary lookups regardless of server casing.
