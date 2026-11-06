# Continuous Log Monitoring Daemon with Replay Simulation

## Objectives
- Build a persistent log monitoring daemon capable of replaying historical log data at configurable speeds.
- Implement real-time log parsing, string tokenization, and severity-based threshold filtering (`ERROR` and `CRITICAL`).
- Manage background daemon execution (`nohup`, process ID tracking, and process termination).
- Construct statistical reporting utilities to aggregate generated security alerts.

## Tools Used
- **Python 3 `time`, `sys`, `os`**: Daemon lifecycle management, timing delays, and file I/O operations.
- **Linux Process Management**: `nohup`, `ps`, `kill`, PID file tracking.

## Key Skills Demonstrated
- Continuous monitoring daemon architecture for simulated live log streams.
- Real-time log parsing and conditional incident alerting.
- Background process automation and audit report generation.

## Troubleshooting Log
- **Directory Path Autocreation**: Added `os.makedirs` routines to ensure alert output directories are dynamically created prior to file writes.
- **Background Execution Control**: Captured process IDs (`echo $!`) to allow clean administrative teardown of background monitoring threads.
