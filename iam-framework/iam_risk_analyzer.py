#!/usr/bin/env python3
"""
IAM Risk Analysis Framework
Correlates user identities, permissions, behavior, and calculates risk scores
"""

import json
import pandas as pd
from datetime import datetime
from collections import defaultdict

class IAMRiskAnalyzer:
    """Main class for analyzing IAM risks"""
    
    def __init__(self, users_file, permissions_file, behavior_file):
        """
        Initialize the analyzer with data files
        """
        self.users = self.load_json(users_file)['users']
        self.permissions = self.load_json(permissions_file)['permissions']
        self.activities = self.load_json(behavior_file)['activities']
        self.risk_scores = {}
    
    def load_json(self, filepath):
        """Load JSON data from file"""
        with open(filepath, 'r') as f:
            return json.load(f)
    
    def correlate_user_data(self, user_id):
        """
        Correlate all data for a specific user
        """
        user_info = None
        for user in self.users:
            if user['id'] == user_id:
                user_info = user
                break
        
        user_permissions = []
        for perm in self.permissions:
            if perm['user_id'] == user_id:
                user_permissions.append(perm)
        
        user_activities = []
        for activity in self.activities:
            if activity['user_id'] == user_id:
                user_activities.append(activity)
        
        return {
            'identity': user_info,
            'permissions': user_permissions,
            'activities': user_activities
        }
    
    def analyze_permission_risk(self, permissions):
        """
        Calculate risk score based on permissions
        """
        risk_score = 0
        for perm in permissions:
            if perm['access_level'] == 'admin':
                risk_score += 30
            elif perm['access_level'] == 'write':
                risk_score += 15
            else:
                risk_score += 5
        
        return min(risk_score, 100)
    
    def analyze_behavior_risk(self, activities):
        """
        Calculate risk score based on user behavior
        """
        risk_score = 0
        
        failed_logins = 0
        for activity in activities:
            if activity['action'] == 'login' and not activity.get('success', True):
                failed_logins += 1
        
        risk_score += failed_logins * 20
        
        for activity in activities:
            timestamp = activity.get('timestamp', '')
            if timestamp:
                hour = int(timestamp.split()[1].split(':')[0])
                if hour >= 22 or hour <= 6:
                    risk_score += 15
        
        high_risk_actions = ['delete_records', 'modify_config', 'privilege_escalation']
        for activity in activities:
            if activity['action'] in high_risk_actions:
                risk_score += 25
        
        return min(risk_score, 100)
    
    def calculate_composite_risk(self, user_id):
        """
        Calculate overall risk score for a user
        """
        user_data = self.correlate_user_data(user_id)
        
        permission_risk = self.analyze_permission_risk(user_data['permissions'])
        behavior_risk = self.analyze_behavior_risk(user_data['activities'])
        
        # Weighted composite risk: 40% permission, 60% behavior
        composite_risk = (permission_risk * 0.4) + (behavior_risk * 0.6)
        
        if composite_risk >= 70:
            risk_level = "HIGH"
        elif composite_risk >= 40:
            risk_level = "MEDIUM"
        else:
            risk_level = "LOW"
        
        return {
            'user_id': user_id,
            'user_name': user_data['identity']['name'] if user_data['identity'] else 'Unknown',
            'department': user_data['identity']['department'] if user_data['identity'] else 'Unknown',
            'permission_risk': round(permission_risk, 2),
            'behavior_risk': round(behavior_risk, 2),
            'composite_risk': round(composite_risk, 2),
            'risk_level': risk_level,
            'permission_count': len(user_data['permissions']),
            'activity_count': len(user_data['activities'])
        }
    
    def analyze_all_users(self):
        """Analyze risk for all users and generate report"""
        results = []
        user_ids = set([user['id'] for user in self.users])
        
        for user_id in user_ids:
            risk_analysis = self.calculate_composite_risk(user_id)
            results.append(risk_analysis)
        
        results.sort(key=lambda x: x['composite_risk'], reverse=True)
        return results
    
    def generate_report(self, output_file):
        """
        Generate a comprehensive risk report
        """
        results = self.analyze_all_users()
        
        report = []
        report.append("=" * 80)
        report.append("IAM RISK ANALYSIS REPORT")
        report.append("=" * 80)
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Total Users Analyzed: {len(results)}")
        report.append("=" * 80)
        report.append("")
        
        high_risk = sum(1 for r in results if r['risk_level'] == 'HIGH')
        medium_risk = sum(1 for r in results if r['risk_level'] == 'MEDIUM')
        low_risk = sum(1 for r in results if r['risk_level'] == 'LOW')
        
        report.append("RISK SUMMARY:")
        report.append(f"  High Risk Users: {high_risk}")
        report.append(f"  Medium Risk Users: {medium_risk}")
        report.append(f"  Low Risk Users: {low_risk}")
        report.append("")
        report.append("=" * 80)
        report.append("DETAILED USER RISK ANALYSIS:")
        report.append("=" * 80)
        
        for result in results:
            report.append("")
            report.append(f"User: {result['user_name']} ({result['user_id']})")
            report.append(f"Department: {result['department']}")
            report.append(f"Risk Level: {result['risk_level']}")
            report.append(f"Composite Risk Score: {result['composite_risk']}/100")
            report.append(f"  - Permission Risk: {result['permission_risk']}/100")
            report.append(f"  - Behavior Risk: {result['behavior_risk']}/100")
            report.append(f"Permissions: {result['permission_count']}")
            report.append(f"Activities Logged: {result['activity_count']}")
            report.append("-" * 80)
        
        import os
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, 'w') as f:
            f.write('\n'.join(report))
        
        print(f"Report generated: {output_file}")
        return results


def main():
    """Main execution function"""
    print("Starting IAM Risk Analysis...")
    
    analyzer = IAMRiskAnalyzer(
        'data/users.json',
        'data/permissions.json',
        'data/behavior_logs.json'
    )
    
    results = analyzer.generate_report('reports/iam_risk_report.txt')
    
    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)
    for result in results:
        print(f"{result['user_name']:20} | Risk: {result['risk_level']:6} | Score: {result['composite_risk']:5.1f}")
    print("=" * 60)


if __name__ == "__main__":
    main()
