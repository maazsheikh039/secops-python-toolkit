#!/usr/bin/env python3
"""
Configuration Security Analyzer
Checks configuration files against security best practices
"""

import json
import yaml
import sys

def analyze_ssh_config(config_file):
    findings = []
    with open(config_file, 'r') as f:
        content = f.read()
    
    if 'PermitRootLogin yes' in content:
        findings.append({
            'severity': 'HIGH',
            'issue': 'Root login is enabled',
            'recommendation': 'Set PermitRootLogin to no'
        })
    
    if 'PasswordAuthentication yes' in content:
        findings.append({
            'severity': 'MEDIUM',
            'issue': 'Password authentication enabled',
            'recommendation': 'Use key-based authentication only'
        })
    
    if 'MaxAuthTries 6' in content or 'MaxAuthTries' not in content:
        findings.append({
            'severity': 'MEDIUM',
            'issue': 'MaxAuthTries is too high or not set',
            'recommendation': 'Set MaxAuthTries to 3'
        })
    
    return findings

def analyze_firewall_rules(config_file):
    findings = []
    with open(config_file, 'r') as f:
        config = json.load(f)
    
    for rule in config.get('rules', []):
        if rule['source'] == '0.0.0.0/0':
            findings.append({
                'severity': 'HIGH',
                'issue': f"Rule {rule['id']} allows access from anywhere",
                'recommendation': f"Restrict source IP for port {rule['port']}"
            })
    
    return findings

def analyze_user_permissions(config_file):
    findings = []
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    
    for user in config.get('users', []):
        if user.get('password_age', 0) > 90:
            findings.append({
                'severity': 'MEDIUM',
                'issue': f"User {user['username']} has password age > 90 days",
                'recommendation': 'Enforce 90-day password rotation'
            })
        
        if user.get('sudo') and user['username'] not in ['admin']:
            findings.append({
                'severity': 'LOW',
                'issue': f"User {user['username']} has sudo privileges",
                'recommendation': 'Review if sudo access is necessary'
            })
    
    return findings

def main():
    print("=" * 60)
    print("CONFIGURATION SECURITY AUDIT")
    print("=" * 60)
    
    all_findings = []
    
    print("\n[*] Analyzing SSH Configuration...")
    ssh_findings = analyze_ssh_config('configs/sshd_config.sample')
    all_findings.extend(ssh_findings)
    
    print("[*] Analyzing Firewall Rules...")
    fw_findings = analyze_firewall_rules('configs/firewall_rules.json')
    all_findings.extend(fw_findings)
    
    print("[*] Analyzing User Permissions...")
    user_findings = analyze_user_permissions('configs/users.yaml')
    all_findings.extend(user_findings)
    
    print(f"\n[*] Total Findings: {len(all_findings)}")
    print("\nDETAILED FINDINGS:")
    print("-" * 60)
    
    for i, finding in enumerate(all_findings, 1):
        print(f"\n{i}. [{finding['severity']}] {finding['issue']}")
        print(f"   Recommendation: {finding['recommendation']}")
    
    import os
    os.makedirs('reports', exist_ok=True)
    with open('reports/config_audit.json', 'w') as f:
        json.dump(all_findings, f, indent=2)
    
    print(f"\n[*] Report saved to reports/config_audit.json")

if __name__ == '__main__':
    main()
