#!/usr/bin/env python3
"""
Log Parser Utility
Parses structured log files and extracts key components
"""

import re
from datetime import datetime
from typing import Dict, List, Optional

def parse_log_line(line: str) -> Optional[Dict[str, str]]:
    """
    Parse a single log line into components.
    Expected format: YYYY-MM-DD HH:MM:SS IP_ADDRESS LEVEL MESSAGE
    """
    pattern = r'(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2})\s+(\S+)\s+(\w+)\s+(.+)'
    match = re.match(pattern, line.strip())
    
    if match:
        return {
            'timestamp': f"{match.group(1)} {match.group(2)}",
            'ip_address': match.group(3),
            'level': match.group(4),
            'message': match.group(5)
        }
    return None


def tokenize_message(message: str) -> List[str]:
    """
    Tokenize a log message into individual words.
    """
    tokens = message.split()
    return [token for token in tokens if token]


def extract_timestamp_components(timestamp_str: str) -> Dict[str, int]:
    """
    Extract date and time components from timestamp string.
    """
    dt = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
    return {
        'year': dt.year,
        'month': dt.month,
        'day': dt.day,
        'hour': dt.hour,
        'minute': dt.minute,
        'second': dt.second
    }


def validate_ip_address(ip: str) -> bool:
    """
    Validate if string is a valid IPv4 address.
    """
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(pattern, ip):
        parts = ip.split('.')
        return all(0 <= int(part) <= 255 for part in parts)
    return False


def parse_log_file(filename: str) -> List[Dict[str, str]]:
    """
    Parse entire log file and return list of parsed entries.
    """
    parsed_logs = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                parsed = parse_log_line(line)
                if parsed:
                    parsed_logs.append(parsed)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return parsed_logs


def filter_by_level(parsed_logs: List[Dict], level: str) -> List[Dict]:
    """
    Filter log entries by severity level.
    """
    return [log for log in parsed_logs if log['level'].upper() == level.upper()]


def main():
    """
    Main function to demonstrate log parsing functionality.
    """
    print("=== Log Parser Utility ===\n")
    logs = parse_log_file('sample.log')
    print(f"Total entries parsed: {len(logs)}")
    
    print("\nFirst 3 parsed entries:")
    for entry in logs[:3]:
        print(entry)
        
    print("\nFiltered ERROR entries:")
    errors = filter_by_level(logs, 'ERROR')
    for err in errors:
        print(err)


if __name__ == "__main__":
    main()
