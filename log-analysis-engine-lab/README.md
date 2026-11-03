# Plugin-Driven Log Analysis Engine

A modular, extensible security log analysis framework in Python built upon a plugin design pattern and dynamic runtime module loading.

## Objectives
- Implement an abstract plugin base interface (`PluginBase`) enforcing standardized method signatures across analysis modules.
- Utilize Python's dynamic module loading (`importlib.util`) to automatically discover and load analyzer plugins at runtime.
- Build specialized detection plugins for authentication failures, security errors, and custom log patterns.
- Process log streams and output structured JSON incident reports with severity classifications.

## Tools Used
- **Python 3** (`importlib`, `re`, `json`, `os`)
- **Linux CLI / SSH**

## Key Skills Demonstrated
- **Extensible Architecture Design:** Decoupling core analysis engines from detection rules using the plugin pattern.
- **Dynamic Module Inspection:** Loading external Python files programmatically without static imports.
- **Security Incident Reporting:** Aggregating disparate log events into structured, prioritized telemetry data.

## Troubleshooting Log
- *Module Path Resolution:* Configured `sys.path` injection inside plugins to ensure clean relative imports of `plugin_base`.
- *Directory Verification:* Ensured `plugins`, `logs`, and `output` subdirectories exist prior to execution.
