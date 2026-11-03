#!/usr/bin/env python3
"""
Event Alert Response Processing Pipeline
Monitors security events, applies rules, and generates responses
"""

import yaml
import json
import time
from datetime import datetime
from collections import defaultdict

class EventProcessor:
    def __init__(self, rules_file):
        """
        Initialize the event processor with security rules
        
        Args:
            rules_file: Path to YAML file containing security rules
        """
        self.rules = self.load_rules(rules_file)
        self.event_counter = defaultdict(lambda: defaultdict(int))
        
    def load_rules(self, rules_file):
        """
        Load security rules from YAML file
        """
        with open(rules_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            return data.get('rules', [])
    
    def parse_event(self, log_line):
        """
        Parse a log line into an event dictionary
        """
        try:
            parts = log_line.strip().split('|')
            if len(parts) >= 4:
                return {
                    'timestamp': parts[0].strip(),
                    'source_ip': parts[1].strip(),
                    'event_type': parts[2].strip(),
                    'details': parts[3].strip()
                }
        except Exception as e:
            print(f"Error parsing event: {e}")
        return None
    
    def check_rules(self, event):
        """
        Check event against all security rules
        """
        triggered = []
        
        for rule in self.rules:
            if rule['pattern'] in event['event_type']:
                key = f"{event['source_ip']}_{rule['id']}"
                self.event_counter[key]['count'] += 1
                
                if self.event_counter[key]['count'] >= rule['threshold']:
                    triggered.append(rule)
                    
        return triggered
    
    def generate_alert(self, event, rule):
        """
        Generate alert file for triggered rule
        """
        alert = {
            'alert_time': datetime.now().isoformat(),
            'rule_id': rule['id'],
            'rule_name': rule['name'],
            'severity': rule['severity'],
            'source_ip': event['source_ip'],
            'event_type': event['event_type'],
            'details': event['details']
        }
        
        filename = f"alerts/alert_{rule['id']}_{int(time.time() * 1000)}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(alert, f, indent=2)
        
        print(f"[ALERT] {rule['severity']} - {rule['name']} from {event['source_ip']}")
    
    def execute_response(self, event, rule):
        """
        Execute automated response action
        """
        response_action = rule['response']
        response_log = {
            'timestamp': datetime.now().isoformat(),
            'action': response_action,
            'source_ip': event['source_ip'],
            'rule_id': rule['id']
        }
        
        filename = f"responses/response_{int(time.time() * 1000)}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(response_log, f, indent=2)
        
        if response_action == 'block_ip':
            print(f"[RESPONSE] Blocking IP: {event['source_ip']}")
        elif response_action == 'alert_admin':
            print(f"[RESPONSE] Alerting administrator about {event['source_ip']}")
        elif response_action == 'log_only':
            print(f"[RESPONSE] Logging event from {event['source_ip']}")
    
    def process_event(self, log_line):
        """
        Main processing function for each event
        """
        event = self.parse_event(log_line)
        if not event:
            return
        
        triggered_rules = self.check_rules(event)
        
        for rule in triggered_rules:
            self.generate_alert(event, rule)
            self.execute_response(event, rule)

def main():
    """Main execution function"""
    print("=== Security Event Processing Pipeline ===")
    print("Initializing processor...")
    
    processor = EventProcessor('rules/security_rules.yaml')
    
    log_path = 'logs/security_events.log'
    # Ensure log file exists before opening
    open(log_path, 'a').close()
    
    print(f"Monitoring {log_path} for events...")
    print("Press Ctrl+C to stop\n")
    
    try:
        with open(log_path, 'r', encoding='utf-8') as f:
            # Seek to end to monitor incoming new events, or read existing
            f.seek(0, 2)
            while True:
                line = f.readline()
                if line:
                    if line.strip():
                        processor.process_event(line)
                else:
                    time.sleep(0.5)
                    
    except KeyboardInterrupt:
        print("\n\nShutting down processor...")
    except FileNotFoundError:
        print("Error: Log file not found!")

if __name__ == "__main__":
    main()
