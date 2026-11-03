#!/usr/bin/env python3
"""
Security Event Generator - Simulates security events for testing
"""

import time
from datetime import datetime

def generate_event(event_type, source_ip, details):
    """Generate a formatted log entry"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f"{timestamp} | {source_ip} | {event_type} | {details}\n"

def main():
    """Generate sample security events"""
    events = [
        ("FAILED_LOGIN", "192.168.1.100", "User: admin"),
        ("FAILED_LOGIN", "192.168.1.100", "User: root"),
        ("FAILED_LOGIN", "192.168.1.100", "User: admin"),
        ("UNAUTHORIZED_ACCESS", "10.0.0.50", "File: /etc/shadow"),
        ("PORT_SCAN", "172.16.0.25", "Ports: 22,80,443,3306"),
        ("PORT_SCAN", "172.16.0.25", "Ports: 8080,8443"),
        ("NORMAL_LOGIN", "192.168.1.10", "User: john"),
        ("PORT_SCAN", "172.16.0.25", "Ports: 21,23,25"),
        ("PORT_SCAN", "172.16.0.25", "Ports: 3389,5900"),
        ("PORT_SCAN", "172.16.0.25", "Ports: 1433,5432"),
    ]
    
    print("Generating security events...")
    
    with open('logs/security_events.log', 'a', encoding='utf-8') as f:
        for event_type, ip, details in events:
            log_entry = generate_event(event_type, ip, details)
            f.write(log_entry)
            f.flush()
            print(f"Generated: {event_type} from {ip}")
            time.sleep(0.5)
    
    print("\nEvent generation complete!")

if __name__ == "__main__":
    main()
