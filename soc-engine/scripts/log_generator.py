#!/usr/bin/env python3
"""
Simple log generator for SOC simulation
Generates sample security events including normal and suspicious activities
"""
import time
import random
from datetime import datetime

NORMAL_EVENTS = [
    "User login successful from 192.168.1.{} - user: employee{}",
    "File accessed: /home/user{}/documents/report.pdf",
    "Service started: web_server on port 80"
]

SUSPICIOUS_EVENTS = [
    "Failed login attempt from 10.0.0.{} - user: admin - attempt {}",
    "Port scan detected from 203.0.113.{} targeting ports 22,23,3389",
    "Unusual outbound connection to 198.51.100.{} on port 4444",
    "Multiple failed sudo attempts - user: guest{}"
]

def generate_log_entry(event_type):
    """
    Generate a single log entry
    
    Args:
        event_type: 'normal' or 'suspicious'
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if event_type == 'normal':
        template = random.choice(NORMAL_EVENTS)
        if "192.168.1.{}" in template:
            log_msg = template.format(random.randint(1, 50), random.randint(1, 10))
        elif "/home/user{}" in template:
            log_msg = template.format(random.randint(1, 10))
        else:
            log_msg = template
    else:
        template = random.choice(SUSPICIOUS_EVENTS)
        if "10.0.0.{}" in template:
            log_msg = template.format(random.randint(100, 200), random.randint(1, 5))
        elif "203.0.113.{}" in template:
            log_msg = template.format(random.randint(1, 50))
        elif "198.51.100.{}" in template:
            log_msg = template.format(random.randint(1, 50))
        elif "guest{}" in template:
            log_msg = template.format(random.randint(1, 10))
        else:
            log_msg = template
            
    # FIXED: Changed event_msg to log_msg
    return f"{timestamp} - {log_msg}"

def main():
    """Main function to generate continuous logs"""
    log_file = "logs/security.log"
    
    print("Starting log generation... (Press Ctrl+C to stop)")
    
    with open(log_file, "a") as f:
        while True:
            # 80% normal events, 20% suspicious events
            event_type = 'suspicious' if random.random() < 0.2 else 'normal'
            log_entry = generate_log_entry(event_type)
            f.write(log_entry + "\n")
            f.flush()
            time.sleep(0.5)

if __name__ == "__main__":
    main()
