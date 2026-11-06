#!/usr/bin/env python3
"""
Incident Monitoring System
Monitors security logs and triggers alerts based on patterns
"""

import time
import yaml
import re
from datetime import datetime
from collections import defaultdict

class IncidentMonitor:
    def __init__(self, config_file):
        """
        Initialize the incident monitor
        
        Args:
            config_file: Path to YAML configuration file
        """
        self.load_config(config_file)
    
    def load_config(self, config_file):
        """Load alert rules from configuration file"""
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
            self.rules = config['alert_rules']
            self.notification = config['notification']
    
    def check_pattern(self, log_line, rule):
        """
        Check if log line matches alert pattern
        
        Args:
            log_line: Single line from log file
            rule: Alert rule dictionary
        
        Returns:
            Boolean indicating if pattern matched
        """
        if re.search(rule['pattern'], log_line, re.IGNORECASE):
            return True
        return False
    
    def monitor_log(self, log_file):
        """
        Monitor log file for security incidents
        
        Args:
            log_file: Path to security log file
        """
        print(f"[*] Starting incident monitor on {log_file}")
        
        with open(log_file, 'r') as f:
            # Seek to end to monitor new incoming log entries
            f.seek(0, 2)
            while True:
                line = f.readline()
                if not line:
                    time.sleep(0.5)
                    continue
                print(f"[LOG] {line.strip()}")

# Main execution
if __name__ == "__main__":
    monitor = IncidentMonitor("config/alert_config.yaml")
    monitor.monitor_log("logs/security.log")
