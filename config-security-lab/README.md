# Secure Configuration Loader and Validator

A production-grade Python security utility designed to safely load, inspect, and validate YAML application configurations against strict compliance schemas and security best practices.

## Objectives
- Safely parse YAML configuration files using `yaml.safe_load`.
- Audit underlying file permissions to detect overly permissive (world-readable) configurations (`chmod 600` enforcement).
- Validate required schema definitions (sections and keys).
- Detect high-risk anti-patterns including weak passwords, unencrypted HTTP endpoints, disabled TLS/SSL settings, debug logging in production, and privileged database usernames (`root`/`admin`).
- Generate structured, colorized terminal security reports.

## Tools Used
- **Python 3 Virtual Environment** (`venv`)
- **Python Libraries:** `PyYAML`, `jsonschema`
- **Linux CLI / SSH**

## Key Skills Demonstrated
- **Secure Configuration Management:** Preventing credential exposure and insecure protocol defaults in deployment manifests.
- **File Permission Auditing:** Programmatically inspecting file stat modes to ensure least-privilege access.
- **Defensive Parsing:** Mitigating YAML deserialization risks using safe loader methods.

## Troubleshooting Log
- *Virtual Environment Activation:* Ensured dependencies (`pyyaml`) are installed inside the active `venv` environment.
- *File Permission Verification:* Utilized `os.stat` mode checks to flag world-readable configuration files automatically.
