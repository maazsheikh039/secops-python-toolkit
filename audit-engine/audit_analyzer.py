#!/usr/bin/env python3
"""
Cloud Audit Log Analyzer
Analyzes cloud audit logs for security issues and risky actions
"""

import json
import sys
from datetime import datetime
from collections import defaultdict

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    COLORS_AVAILABLE = True
except ImportError:
    COLORS_AVAILABLE = False
    print("Note: Install colorama for colored output")

# Security rules configuration
RISKY_ACTIONS = [
    'DisableEncryption',
    'ModifyLogging',
    'DeleteBackup',
    'CreateAccessKey',
    'DisableMFA'
]

MISCONFIGURATION_PATTERNS = {
    'open_ssh': '0.0.0.0/0 on port 22',
    'open_rdp': '0.0.0.0/0 on port 3389',
    'public_access': 'public-read',
    'no_encryption': 'encryption: false'
}

def load_audit_logs(filename):
    """
    Load audit logs from JSON file
    
    Args:
        filename: Path to the JSON log file
    
    Returns:
        List of log entries
    """
    try:
        with open(filename, 'r') as f:
            logs = json.load(f)
        print(f"[+] Loaded {len(logs)} log entries from {filename}")
        return logs
    except FileNotFoundError:
        print(f"[!] Error: File '{filename}' not found")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"[!] Error: Invalid JSON format in '{filename}'")
        sys.exit(1)

def analyze_risky_actions(logs):
    """
    Detect risky actions in audit logs
    
    Args:
        logs: List of log entries
    
    Returns:
        List of risky action findings
    """
    findings = []
    
    for log in logs:
        action = log.get('action', '')
        if action in RISKY_ACTIONS:
            finding = {
                'severity': 'HIGH',
                'type': 'Risky Action',
                'timestamp': log.get('timestamp'),
                'user': log.get('user'),
                'action': action,
                'resource': log.get('resource'),
                'details': log.get('details', {})
            }
            findings.append(finding)
    
    return findings

def detect_misconfigurations(logs):
    """
    Detect security misconfigurations
    
    Args:
        logs: List of log entries
    
    Returns:
        List of misconfiguration findings
    """
    findings = []
    
    for log in logs:
        details_str = json.dumps(log.get('details', {}))
        
        for config_name, pattern in MISCONFIGURATION_PATTERNS.items():
            if pattern in details_str:
                finding = {
                    'severity': 'CRITICAL',
                    'type': 'Misconfiguration',
                    'timestamp': log.get('timestamp'),
                    'user': log.get('user'),
                    'action': log.get('action'),
                    'issue': config_name.replace('_', ' ').title(),
                    'details': log.get('details', {})
                }
                findings.append(finding)
    
    return findings

def detect_suspicious_activity(logs):
    """
    Detect suspicious activities like failed access attempts
    and unusual access times
    
    Args:
        logs: List of log entries
    
    Returns:
        List of suspicious activity findings
    """
    findings = []
    
    for log in logs:
        # Check for failed access attempts
        if log.get('status') == 'FAILED':
            finding = {
                'severity': 'MEDIUM',
                'type': 'Suspicious Activity',
                'timestamp': log.get('timestamp'),
                'user': log.get('user'),
                'action': log.get('action'),
                'issue': 'Failed Access Attempt',
                'source_ip': log.get('source_ip'),
                'details': log.get('details', {})
            }
            findings.append(finding)
        
        # Check for unusual access times (example: between 2-5 AM)
        timestamp = log.get('timestamp', '')
        if 'T02:' in timestamp or 'T03:' in timestamp or 'T04:' in timestamp:
            finding = {
                'severity': 'MEDIUM',
                'type': 'Suspicious Activity',
                'timestamp': timestamp,
                'user': log.get('user'),
                'action': log.get('action'),
                'issue': 'Unusual Access Time',
                'details': log.get('details', {})
            }
            findings.append(finding)
        
        # Check for external/unknown users
        user = log.get('user', '')
        if 'external' in user or 'unknown' in user:
            finding = {
                'severity': 'HIGH',
                'type': 'Suspicious Activity',
                'timestamp': log.get('timestamp'),
                'user': user,
                'action': log.get('action'),
                'issue': 'External User Activity',
                'source_ip': log.get('source_ip'),
                'details': log.get('details', {})
            }
            findings.append(finding)
    
    return findings

def generate_report(logs, risky_actions, misconfigs, suspicious):
    """
    Generate a comprehensive security report
    
    Args:
        logs: Original log entries
        risky_actions: List of risky action findings
        misconfigs: List of misconfiguration findings
        suspicious: List of suspicious activity findings
    """
    print("\n" + "="*70)
    print("           CLOUD AUDIT LOG SECURITY ANALYSIS REPORT")
    print("="*70)
    
    # Summary statistics
    print(f"\n[SUMMARY]")
    print(f"Total Log Entries Analyzed: {len(logs)}")
    print(f"Risky Actions Found: {len(risky_actions)}")
    print(f"Misconfigurations Found: {len(misconfigs)}")
    print(f"Suspicious Activities Found: {len(suspicious)}")
    
    total_issues = len(risky_actions) + len(misconfigs) + len(suspicious)
    print(f"\nTotal Security Issues: {total_issues}")
    
    # Risky Actions
    if risky_actions:
        print(f"\n{'='*70}")
        print("[RISKY ACTIONS DETECTED]")
        print('='*70)
        for idx, finding in enumerate(risky_actions, 1):
            print(f"\n{idx}. {finding['action']}")
            print(f"   Severity: {finding['severity']}")
            print(f"   User: {finding['user']}")
            print(f"   Time: {finding['timestamp']}")
            print(f"   Resource: {finding['resource']}")
            print(f"   Details: {finding['details']}")
    
    # Misconfigurations
    if misconfigs:
        print(f"\n{'='*70}")
        print("[SECURITY MISCONFIGURATIONS]")
        print('='*70)
        for idx, finding in enumerate(misconfigs, 1):
            print(f"\n{idx}. {finding['issue']}")
            print(f"   Severity: {finding['severity']}")
            print(f"   User: {finding['user']}")
            print(f"   Action: {finding['action']}")
            print(f"   Time: {finding['timestamp']}")
            print(f"   Details: {finding['details']}")
    
    # Suspicious Activities
    if suspicious:
        print(f"\n{'='*70}")
        print("[SUSPICIOUS ACTIVITIES]")
        print('='*70)
        for idx, finding in enumerate(suspicious, 1):
            print(f"\n{idx}. {finding['issue']}")
            print(f"   Severity: {finding['severity']}")
            print(f"   User: {finding['user']}")
            print(f"   Action: {finding['action']}")
            print(f"   Time: {finding['timestamp']}")
            if 'source_ip' in finding:
                print(f"   Source IP: {finding['source_ip']}")
    
    # Recommendations
    print(f"\n{'='*70}")
    print("[RECOMMENDATIONS]")
    print('='*70)
    if misconfigs:
        print("\n- Review and restrict security group rules")
        print("- Enable encryption for all storage resources")
    if risky_actions:
        print("- Implement approval workflows for sensitive actions")
        print("- Enable MFA for administrative accounts")
        print("- Review and rotate access keys regularly")
    if suspicious:
        print("- Investigate failed access attempts")
        print("- Monitor unusual access patterns")
        print("- Restrict access from unknown sources")
    
    print("\n" + "="*70 + "\n")

def main():
    """Main execution function"""
    print("\n=== Cloud Audit Log Analyzer ===\n")
    
    if len(sys.argv) < 2:
        print("Usage: python3 audit_analyzer.py <log_file.json>")
        print("Example: python3 audit_analyzer.py sample_audit_logs.json")
        sys.exit(1)
    
    log_file = sys.argv[1]
    logs = load_audit_logs(log_file)
    
    print("\n[*] Analyzing logs for security issues...")
    risky_actions = analyze_risky_actions(logs)
    misconfigs = detect_misconfigurations(logs)
    suspicious = detect_suspicious_activity(logs)
    
    generate_report(logs, risky_actions, misconfigs, suspicious)

if __name__ == "__main__":
    main()
