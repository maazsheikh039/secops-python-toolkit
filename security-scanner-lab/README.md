# Command-Line Security Scanner Tool

A robust Python-based static security analysis CLI utility designed to inspect source code, configuration files, and project directories for hardcoded credentials, leaked API keys, cryptographic private keys, and sensitive network identifiers.

## Objectives
- Parse and handle command-line arguments and flags efficiently using Python's `argparse`.
- Traverse file systems recursively (`os.walk`) while ignoring binary and hidden assets.
- Detect high-risk security anti-patterns using compiled regular expression heuristics.
- Generate structured, categorized terminal compliance reports.

## Tools Used
- **Python 3** (`argparse`, `re`, `os`, `sys`)
- **Linux CLI / Bash**

## Key Skills Demonstrated
- **Static Application Security Testing (SAST):** Automated detection of hardcoded secrets and credentials.
- **CLI Tool Engineering:** Designing intuitive command-line interfaces with robust error handling and help text formatting.
- **Regular Expression Pattern Matching:** Identifying structured patterns like private key headers, email addresses, and IP blocks.

## Troubleshooting Log
- *Encoding Resilience:* Integrated `errors='ignore'` within file I/O operations to prevent decoder crashes when encountering non-UTF8 or binary files.
- *Directory Traversal:* Implemented checks to skip hidden files (starting with `.`) during recursive directory scans.
