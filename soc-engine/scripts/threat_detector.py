#!/usr/bin/env python3
"""
Threat detection engine
Monitors logs and identifies suspicious patterns
"""
import re
import time
from datetime import datetime

THREAT_PATTERNS = {
    'brute_force': r'Failed login attempt.*user: admin',
    'port_scan': r'Port scan detected',
    'suspicious_connection': r'Unusual outbound connection.*port 4444',
    'privilege_escalation': r'Multiple failed sudo attempts'
}

def analyze_log_line(line):
    """
    Analyze a single log line for threats
    """
    for threat_type, pattern in THREAT_PATTERNS.items():
        if re.search(pattern, line):
            parts = line.split(" - ", 1)
            timestamp = parts[0] if len(parts) > 0 else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return {
                'threat_type': threat_type,
                'timestamp': timestamp,
                'raw_log': line.strip()
            }
    return None

def monitor_logs(log_file, alert_file):
    """
    Continuously monitor log file for threats
    """
    print(f"Monitoring {log_file} for threats...")
    
    with open(log_file, 'r') as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue
            
            threat = analyze_log_line(line)
            if threat:
                alert_msg = f"[{threat['timestamp']}] ALERT: {threat['threat_type'].upper()} -> {threat['raw_log']}"
                print(alert_msg)
                with open(alert_file, 'a') as af:
                    af.write(alert_msg + "\n")

def main():
    log_file = "logs/security.log"
    alert_file = "alerts/threats.txt"
    
    import os
    os.makedirs("alerts", exist_ok=True)
    
    monitor_logs(log_file, alert_file)

if __name__ == "__main__":
    main()
