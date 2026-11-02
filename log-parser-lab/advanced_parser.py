#!/usr/bin/env python3
"""
Advanced Log Parser with Statistics
"""

import csv
import re
from collections import Counter
from datetime import datetime
from typing import Dict, List
from log_parser import parse_log_file

def generate_statistics(parsed_logs: List[Dict]) -> Dict:
    """
    Generate statistics from parsed logs.
    """
    stats = {
        'total_entries': len(parsed_logs),
        'level_counts': Counter(log['level'] for log in parsed_logs),
        'unique_ips': len(set(log['ip_address'] for log in parsed_logs)),
        'top_ips': Counter(log['ip_address'] for log in parsed_logs).most_common(3)
    }
    return stats


def extract_ip_addresses(parsed_logs: List[Dict]) -> List[str]:
    """
    Extract all IP addresses from parsed logs.
    
    Args:
        parsed_logs: List of parsed log dictionaries
    
    Returns:
        List of IP addresses
    """
    return [log['ip_address'] for log in parsed_logs]


def search_logs(parsed_logs: List[Dict], keyword: str) -> List[Dict]:
    """
    Search logs for entries containing keyword in message.
    """
    kw_lower = keyword.lower()
    return [log for log in parsed_logs if kw_lower in log['message'].lower()]


def export_to_csv(parsed_logs: List[Dict], output_file: str):
    """
    Export parsed logs to CSV format.
    """
    fieldnames = ['timestamp', 'ip_address', 'level', 'message']
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for log in parsed_logs:
                writer.writerow(log)
        print(f"Successfully exported {len(parsed_logs)} entries to {output_file}")
    except Exception as e:
        print(f"Error exporting to CSV: {e}")


def main():
    print("=== Advanced Log Parser ===\n")
    
    logs = parse_log_file('sample.log')
    if not logs:
        return
        
    stats = generate_statistics(logs)
    print("--- Log Statistics ---")
    print(f"Total Entries : {stats['total_entries']}")
    print(f"Level Counts  : {dict(stats['level_counts'])}")
    print(f"Unique IPs    : {stats['unique_ips']}")
    print(f"Top IPs       : {stats['top_ips']}")
    print("-" * 30)
    
    ips = extract_ip_addresses(logs)
    print(f"\nExtracted IP Addresses (Sample): {ips[:4]}")
    
    keyword = "login"
    print(f"\nSearching logs for keyword: '{keyword}'")
    matching = search_logs(logs, keyword)
    for m in matching:
        print(m)
        
    print("\nExporting results to CSV...")
    export_to_csv(logs, 'output.csv')
    
    print("\nProcessing complete!")


if __name__ == "__main__":
    main()
