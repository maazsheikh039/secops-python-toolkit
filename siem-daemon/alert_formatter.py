#!/usr/bin/env python3
"""
Alert Formatting and Notification System
Formats incident alerts and sends notifications
"""

from datetime import datetime
import os

class AlertFormatter:
    def __init__(self, notification_config):
        """
        Initialize alert formatter
        
        Args:
            notification_config: Dictionary with notification settings
        """
        self.config = notification_config
        self.log_file = self.config.get('log_file', 'alerts/incidents.log')
        
        # Ensure alert directory exists
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)
    
    def format_alert(self, rule_name, severity, log_entry, count):
        """
        Format alert message with incident details
        
        Args:
            rule_name: Name of triggered rule
            severity: Alert severity level
            log_entry: Original log entry that triggered alert
            count: Number of occurrences
        
        Returns:
            Formatted alert string
        """
        alert_template = f"""
{'='*60}
SECURITY ALERT
{'='*60}
Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Rule: {rule_name}
Severity: {severity.upper()}
Occurrences: {count}
Log Entry: {log_entry.strip()}
{'='*60}
"""
        return alert_template
    
    def send_alert(self, alert_message):
        """
        Send alert through configured channels
        
        Args:
            alert_message: Formatted alert message
        """
        if self.config.get('console_enabled', True):
            print(alert_message)
        
        if self.config.get('log_file'):
            self.write_to_log(alert_message)
    
    def write_to_log(self, message):
        """Write alert to log file"""
        with open(self.log_file, 'a') as f:
            f.write(message + "\n")

# Example usage
if __name__ == "__main__":
    config = {
        'log_file': 'alerts/incidents.log',
        'console_enabled': True
    }
    
    formatter = AlertFormatter(config)
    test_alert = formatter.format_alert(
        "Failed Login Attempt",
        "medium",
        "Failed password for user admin",
        3
    )
    formatter.send_alert(test_alert)
