#!/usr/bin/env python3
"""
Log Security Analyzer
Detects suspicious activities in log files
"""

import re
import json
from collections import defaultdict

def analyze_auth_logs(log_file):
    findings = []
    failed_attempts = defaultdict(int)
    
    with open(log_file, 'r') as f:
        for line in f:
            if 'Failed login attempt' in line:
                ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
                if ip_match:
                    ip = ip_match.group(1)
                    failed_attempts[ip] += 1
            
            if 'Brute force attack' in line:
                findings.append({
                    'severity': 'CRITICAL',
                    'type': 'Brute Force Attack',
                    'details': line.strip()
                })
    
    for ip, count in failed_attempts.items():
        if count >= 2:
            findings.append({
                'severity': 'HIGH',
                'type': 'Multiple Failed Logins',
                'details': f"IP {ip} had {count} failed login attempts"
            })
    
    return findings

def analyze_access_logs(log_file):
    findings = []
    with open(log_file, 'r') as f:
        for line in f:
            if '403' in line:
                findings.append({
                    'severity': 'MEDIUM',
                    'type': 'Unauthorized Access Attempt',
                    'details': line.strip()
                })
            
            if '/admin/' in line or '/api/secrets' in line:
                findings.append({
                    'severity': 'MEDIUM',
                    'type': 'Sensitive Endpoint Access',
                    'details': line.strip()
                })
            
            if 'DELETE' in line:
                findings.append({
                    'severity': 'LOW',
                    'type': 'Delete Operation',
                    'details': line.strip()
                })
    
    return findings

def main():
    print("=" * 60)
    print("LOG SECURITY AUDIT")
    print("=" * 60)
    
    all_findings = []
    
    print("\n[*] Analyzing Authentication Logs...")
    auth_findings = analyze_auth_logs('logs/auth.log')
    all_findings.extend(auth_findings)
    
    print("[*] Analyzing Access Logs...")
    access_findings = analyze_access_logs('logs/access.log')
    all_findings.extend(access_findings)
    
    print(f"\n[*] Total Security Events: {len(all_findings)}")
    print("\nDETAILED FINDINGS:")
    print("-" * 60)
    
    critical = [f for f in all_findings if f['severity'] == 'CRITICAL']
    high = [f for f in all_findings if f['severity'] == 'HIGH']
    medium = [f for f in all_findings if f['severity'] == 'MEDIUM']
    low = [f for f in all_findings if f['severity'] == 'LOW']
    
    for severity, findings in [('CRITICAL', critical), ('HIGH', high), 
                                ('MEDIUM', medium), ('LOW', low)]:
        if findings:
            print(f"\n{severity} SEVERITY ({len(findings)}):")
            for finding in findings:
                print(f"  - {finding['type']}: {finding['details']}")
    
    import os
    os.makedirs('reports', exist_ok=True)
    with open('reports/log_audit.json', 'w') as f:
        json.dump(all_findings, f, indent=2)
    
    print(f"\n[*] Report saved to reports/log_audit.json")

if __name__ == '__main__':
    main()
