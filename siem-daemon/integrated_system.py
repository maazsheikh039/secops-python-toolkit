#!/usr/bin/env python3
"""
Integrated Incident Alerting System
Combines monitoring and alerting functionality
"""

import time
import yaml
import re
from datetime import datetime
from collections import defaultdict
from alert_formatter import AlertFormatter

class IntegratedAlertSystem:
    def __init__(self, config_file):
        """Initialize integrated system"""
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
        
        self.rules = config['alert_rules']
        self.formatter = AlertFormatter(config['notification'])
        self.incident_counts = defaultdict(int)
    
    def process_log_line(self, line):
        """
        Process single log line and check for incidents
        
        Args:
            line: Log line to process
        """
        for rule in self.rules:
            if re.search(rule['pattern'], line, re.IGNORECASE):
                rule_name = rule['name']
                self.incident_counts[rule_name] += 1
                current_count = self.incident_counts[rule_name]
                
                print(f"[*] Match found for rule '{rule_name}' (Count: {current_count}/{rule['threshold']})")
                
                if current_count >= rule['threshold']:
                    alert_msg = self.formatter.format_alert(
                        rule_name=rule_name,
                        severity=rule['severity'],
                        log_entry=line,
                        count=current_count
                    )
                    self.formatter.send_alert(alert_msg)
                    # Reset counter after triggering alert
                    self.incident_counts[rule_name] = 0
    
    def monitor(self, log_file):
        """
        Main monitoring loop
        
        Args:
            log_file: Path to log file to monitor
        """
        print(f"[*] Monitoring {log_file} for security incidents...")
        
        with open(log_file, 'r') as f:
            f.seek(0, 2)
            while True:
                line = f.readline()
                if not line:
                    time.sleep(0.5)
                    continue
                self.process_log_line(line)

if __name__ == "__main__":
    system = IntegratedAlertSystem("config/alert_config.yaml")
    system.monitor("logs/security.log")
