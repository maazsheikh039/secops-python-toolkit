#!/usr/bin/env python3
"""
Brute-force Attack Detection Engine
Analyzes authentication logs to detect suspicious login patterns
"""

from datetime import datetime
from collections import defaultdict

class BruteForceDetector:
    """
    Detects brute-force attacks by analyzing failed login attempts
    """
    
    def __init__(self, threshold=5, time_window=300):
        """
        Initialize the detector with configurable parameters
        
        Args:
            threshold: Number of failed attempts to trigger alert (default: 5)
            time_window: Time window in seconds to check attempts (default: 300)
        """
        self.threshold = threshold
        self.time_window = time_window
        # Dictionary to store failed attempts per IP address
        self.failed_attempts = defaultdict(list)
        self.alerts = []
    
    def parse_log_line(self, line):
        """
        Parse a single log line and extract components
        
        Args:
            line: String containing log entry
            
        Returns:
            Dictionary with timestamp, status, user, and ip
            Returns None if line cannot be parsed
        """
        parts = line.strip().split()
        
        if len(parts) < 5:
            return None
        
        try:
            # Extract timestamp (combine date and time)
            timestamp_str = f"{parts[0]} {parts[1]}"
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            
            # Extract status (SUCCESS or FAILED)
            status = parts[2]
            
            # Extract username (remove "user=" prefix)
            user = parts[3].split('=')[1]
            
            # Extract IP address (remove "ip=" prefix)
            ip = parts[4].split('=')[1]
            
            return {
                'timestamp': timestamp,
                'status': status,
                'user': user,
                'ip': ip
            }
        except Exception as e:
            print(f"Error parsing line: {line.strip()} - {e}")
            return None
    
    def analyze_attempt(self, log_entry):
        """
        Analyze a single login attempt for brute-force patterns
        
        Args:
            log_entry: Dictionary containing parsed log information
        """
        if log_entry is None:
            return
        
        # Only track FAILED attempts
        if log_entry['status'] == 'FAILED':
            ip = log_entry['ip']
            timestamp = log_entry['timestamp']
            
            # Add this failed attempt to the list for this IP
            self.failed_attempts[ip].append({
                'timestamp': timestamp,
                'user': log_entry['user']
            })
            
            # Check if this IP has exceeded the threshold
            self.check_for_attack(ip)
    
    def check_for_attack(self, ip):
        """
        Check if an IP address shows brute-force attack patterns
        
        Args:
            ip: IP address to check
        """
        attempts = self.failed_attempts[ip]
        
        if len(attempts) < self.threshold:
            return
        
        # Get the most recent attempts
        recent_attempts = attempts[-self.threshold:]
        
        # Calculate time difference between first and last attempt
        first_time = recent_attempts[0]['timestamp']
        last_time = recent_attempts[-1]['timestamp']
        time_diff = (last_time - first_time).total_seconds()
        
        # If attempts occurred within time window, raise alert
        if time_diff <= self.time_window:
            alert = {
                'ip': ip,
                'attempts': len(attempts),
                'users_targeted': list(set([a['user'] for a in attempts])),
                'first_attempt': first_time,
                'last_attempt': last_time
            }
            
            # Only add if not already alerted for this IP
            if not any(a['ip'] == ip for a in self.alerts):
                self.alerts.append(alert)
                self.raise_alert(alert)
    
    def raise_alert(self, alert):
        """
        Display alert information for detected attack
        
        Args:
            alert: Dictionary containing attack details
        """
        print("\n" + "="*60)
        print("SECURITY ALERT: Brute-force Attack Detected!")
        print("="*60)
        print(f"Source IP: {alert['ip']}")
        print(f"Total Failed Attempts: {alert['attempts']}")
        print(f"Targeted Users: {', '.join(alert['users_targeted'])}")
        print(f"Attack Duration: {alert['first_attempt']} to {alert['last_attempt']}")
        print("="*60 + "\n")
    
    def save_alerts_to_file(self, filename='alerts.log'):
        """
        Save all detected alerts to a file
        
        Args:
            filename: Output file for alerts
        """
        with open(filename, 'w') as f:
            f.write("BRUTE-FORCE ATTACK DETECTION REPORT\n")
            f.write("="*60 + "\n\n")
            
            for i, alert in enumerate(self.alerts, 1):
                f.write(f"Alert #{i}\n")
                f.write(f"IP Address: {alert['ip']}\n")
                f.write(f"Failed Attempts: {alert['attempts']}\n")
                f.write(f"Targeted Users: {', '.join(alert['users_targeted'])}\n")
                f.write(f"Time Range: {alert['first_attempt']} to {alert['last_attempt']}\n")
                f.write("-"*60 + "\n\n")
        
        print(f"\nAlerts saved to {filename}")

    def process_log_file(self, filename):
        """
        Process entire log file and detect attacks
        
        Args:
            filename: Path to the log file
        """
        print(f"Analyzing log file: {filename}")
        print(f"Detection threshold: {self.threshold} failed attempts")
        print(f"Time window: {self.time_window} seconds\n")
        
        try:
            with open(filename, 'r') as f:
                for line in f:
                    log_entry = self.parse_log_line(line)
                    self.analyze_attempt(log_entry)
            
            self.print_summary()
            
        except FileNotFoundError:
            print(f"Error: File {filename} not found")
        except Exception as e:
            print(f"Error processing file: {e}")
    
    def print_summary(self):
        """
        Print detection summary
        """
        print("\n" + "="*60)
        print("DETECTION SUMMARY")
        print("="*60)
        print(f"Total IPs analyzed: {len(self.failed_attempts)}")
        print(f"Attacks detected: {len(self.alerts)}")
        
        if self.alerts:
            print("\nSuspicious IP Addresses:")
            for alert in self.alerts:
                print(f"  - {alert['ip']} ({alert['attempts']} failed attempts)")
        else:
            print("\nNo brute-force attacks detected.")
        print("="*60)


def main():
    """
    Main function to run the detector
    """
    detector = BruteForceDetector(threshold=5, time_window=300)
    detector.process_log_file('auth.log')
    
    if detector.alerts:
        detector.save_alerts_to_file('alerts.log')


if __name__ == "__main__":
    main()
