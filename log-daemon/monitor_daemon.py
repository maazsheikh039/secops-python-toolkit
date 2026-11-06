#!/usr/bin/env python3
"""
Continuous Monitoring Daemon
Replays log data and monitors for critical events
"""

import time
import sys
import os
from datetime import datetime

class LogMonitor:
    """
    A daemon that replays log files and monitors for specific events
    """
    
    def __init__(self, log_file, output_file, replay_speed=1.0):
        """
        Initialize the monitoring daemon
        
        Args:
            log_file: Path to the log file to replay
            output_file: Path to write alerts
            replay_speed: Speed multiplier for replay (1.0 = real-time)
        """
        self.log_file = log_file
        self.output_file = output_file
        self.replay_speed = replay_speed
        self.alert_count = 0
        
    def parse_log_line(self, line):
        """
        Parse a single log line and extract components
        
        Args:
            line: A single line from the log file
            
        Returns:
            Dictionary with parsed components or None if invalid
        """
        parts = line.strip().split(' ', 3)
        
        if len(parts) < 4:
            return None
            
        return {
            'date': parts[0],
            'time': parts[1],
            'level': parts[2],
            'message': parts[3]
        }
    
    def check_alert_conditions(self, log_entry):
        """
        Check if log entry requires an alert
        
        Args:
            log_entry: Parsed log entry dictionary
            
        Returns:
            True if alert needed, False otherwise
        """
        level = log_entry.get('level', '')
        return level in ['ERROR', 'CRITICAL']
    
    def write_alert(self, log_entry):
        """
        Write alert to output file
        
        Args:
            log_entry: Parsed log entry that triggered alert
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        alert_msg = f"[ALERT {timestamp}] {log_entry['level']}: {log_entry['message']}\n"
        
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)
        with open(self.output_file, 'a') as f:
            f.write(alert_msg)
        
        self.alert_count += 1
        print(f"ALERT: {log_entry['level']} - {log_entry['message']}")
    
    def run(self):
        """
        Main daemon loop - replays log file and monitors continuously
        """
        print(f"Starting monitoring daemon...")
        print(f"Reading from: {self.log_file}")
        print(f"Writing alerts to: {self.output_file}")
        print(f"Replay speed: {self.replay_speed}x")
        print("-" * 60)
        
        try:
            with open(self.log_file, 'r') as f:
                lines = f.readlines()
            
            for line in lines:
                log_entry = self.parse_log_line(line)
                
                if log_entry is None:
                    continue
                
                print(f"[{log_entry['date']} {log_entry['time']}] "
                      f"{log_entry['level']}: {log_entry['message']}")
                
                if self.check_alert_conditions(log_entry):
                    self.write_alert(log_entry)
                
                time.sleep(0.5 / self.replay_speed)
            
            print("-" * 60)
            print(f"Monitoring complete. Total alerts: {self.alert_count}")
            
        except FileNotFoundError:
            print(f"ERROR: Log file not found: {self.log_file}")
            sys.exit(1)
        except KeyboardInterrupt:
            print("\nMonitoring stopped by user")
            print(f"Total alerts generated: {self.alert_count}")
            sys.exit(0)

def main():
    """
    Main entry point for the daemon
    """
    log_file = "logs/access.log"
    output_file = "output/alerts.log"
    replay_speed = 2.0
    
    monitor = LogMonitor(log_file, output_file, replay_speed)
    monitor.run()

if __name__ == "__main__":
    main()
