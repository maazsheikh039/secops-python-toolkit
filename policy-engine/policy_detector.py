#!/usr/bin/env python3
"""
Policy Misconfiguration Detection Engine
Analyzes security policies for weak or conflicting rules
"""

import json
import sys

class PolicyDetector:
    """
    Main class for detecting policy misconfigurations
    """
    
    def __init__(self):
        """Initialize the detector with empty findings list"""
        self.findings = []
    
    def load_policy(self, filename):
        """
        Load policy file and return parsed JSON
        
        Args:
            filename: Path to the policy JSON file
            
        Returns:
            Dictionary containing policy data
        """
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: File {filename} not found")
            return None
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in {filename}")
            return None
    
    def check_overly_permissive_source(self, rule):
        """
        Check if firewall rule allows traffic from anywhere (0.0.0.0/0)
        
        Args:
            rule: Dictionary containing firewall rule data
            
        Returns:
            String describing the issue, or None if no issue found
        """
        if rule.get('source') == '0.0.0.0/0' and rule.get('action') == 'ALLOW':
            port = rule.get('port')
            return f"CRITICAL: Rule {rule['rule_id']} allows traffic from anywhere to port {port}"
        return None
    
    def check_conflicting_rules(self, rules):
        """
        Check for conflicting firewall rules (same source/dest/port but different actions)
        
        Args:
            rules: List of firewall rule dictionaries
            
        Returns:
            List of conflict descriptions
        """
        conflicts = []
        for i, rule1 in enumerate(rules):
            for rule2 in rules[i+1:]:
                if (rule1['source'] == rule2['source'] and 
                    rule1['destination'] == rule2['destination'] and
                    rule1['port'] == rule2['port'] and
                    rule1['protocol'] == rule2['protocol']):
                    if rule1['action'] != rule2['action']:
                        conflicts.append(
                            f"CONFLICT: Rules {rule1['rule_id']} and {rule2['rule_id']} "
                            f"have conflicting actions for same traffic"
                        )
        return conflicts
    
    def check_wildcard_permissions(self, rule):
        """
        Check for dangerous wildcard permissions in access rules
        
        Args:
            rule: Dictionary containing access rule data
            
        Returns:
            String describing the issue, or None if no issue found
        """
        if rule.get('user') == '*':
            return f"HIGH: Rule {rule['rule_id']} grants {rule['permission']} to everyone"
        return None
    
    def check_sensitive_resource_access(self, rule):
        """
        Check if non-admin users have access to sensitive resources
        
        Args:
            rule: Dictionary containing access rule data
            
        Returns:
            String describing the issue, or None if no issue found
        """
        sensitive_resources = ['/etc/passwd', '/etc/shadow', '/root', '/var/log/secure']
        resource = rule.get('resource')
        user = rule.get('user')
        
        if resource in sensitive_resources and user not in ['admin', 'root']:
            return f"HIGH: Rule {rule['rule_id']} allows {user} access to sensitive resource {resource}"
        return None
    
    def analyze_firewall_policy(self, policy_data):
        """
        Analyze firewall policy for misconfigurations
        
        Args:
            policy_data: Dictionary containing firewall rules
        """
        if not policy_data:
            return
        
        rules = policy_data.get('firewall_rules', [])
        print(f"Analyzing {len(rules)} firewall rules...")
        
        for rule in rules:
            finding = self.check_overly_permissive_source(rule)
            if finding:
                self.findings.append(finding)
        
        conflicts = self.check_conflicting_rules(rules)
        self.findings.extend(conflicts)
    
    def analyze_access_policy(self, policy_data):
        """
        Analyze access control policy for misconfigurations
        
        Args:
            policy_data: Dictionary containing access rules
        """
        if not policy_data:
            return
        
        rules = policy_data.get('access_rules', [])
        print(f"Analyzing {len(rules)} access control rules...")
        
        for rule in rules:
            finding = self.check_wildcard_permissions(rule)
            if finding:
                self.findings.append(finding)
            
            finding = self.check_sensitive_resource_access(rule)
            if finding:
                self.findings.append(finding)
    
    def generate_report(self):
        """
        Generate and print a report of all findings
        """
        print("\n" + "=" * 60)
        print("SECURITY FINDINGS REPORT")
        print("=" * 60)
        
        if not self.findings:
            print("\nNo misconfigurations detected. All policies appear secure.")
            return
        
        print(f"\nTotal Issues Found: {len(self.findings)}\n")
        
        for i, finding in enumerate(self.findings, 1):
            print(f"{i}. {finding}")
        
        critical = sum(1 for f in self.findings if 'CRITICAL' in f)
        high = sum(1 for f in self.findings if 'HIGH' in f)
        
        print("\n" + "-" * 60)
        print(f"Summary: {critical} Critical, {high} High severity issues")
        print("=" * 60)


def main():
    """Main function to run the policy detector"""
    print("=" * 60)
    print("Policy Misconfiguration Detection Engine")
    print("=" * 60)
    
    detector = PolicyDetector()
    
    fw_policy = detector.load_policy('firewall_policy.json')
    detector.analyze_firewall_policy(fw_policy)
    
    ac_policy = detector.load_policy('access_policy.json')
    detector.analyze_access_policy(ac_policy)
    
    detector.generate_report()
    
    print("\nAnalysis complete!")


if __name__ == "__main__":
    main()
