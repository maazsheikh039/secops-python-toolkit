#!/usr/bin/env python3
"""
Compliance Report Generator
Combines all audit findings into a comprehensive report
"""

import json
from datetime import datetime
import os

def load_audit_results():
    results = {}
    try:
        with open('reports/config_audit.json', 'r') as f:
            results['config'] = json.load(f)
    except FileNotFoundError:
        results['config'] = []
    
    try:
        with open('reports/log_audit.json', 'r') as f:
            results['log'] = json.load(f)
    except FileNotFoundError:
        results['log'] = []
    
    return results

def calculate_compliance_score(findings):
    total_issues = 0
    severity_weights = {
        'CRITICAL': 10,
        'HIGH': 5,
        'MEDIUM': 2,
        'LOW': 1
    }
    
    penalty = 0
    for category in findings.values():
        for finding in category:
            severity = finding.get('severity', 'LOW')
            penalty += severity_weights.get(severity, 1)
            total_issues += 1
    
    score = max(0, 100 - penalty)
    return score, total_issues

def generate_html_report(results, score, total_issues):
    html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Security Compliance Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        .header {{ background: #2c3e50; color: white; padding: 20px; }}
        .score {{ font-size: 48px; font-weight: bold; }}
        .critical {{ color: #e74c3c; }}
        .high {{ color: #e67e22; }}
        .medium {{ color: #f39c12; }}
        .low {{ color: #3498db; }}
        .section {{ margin: 20px 0; padding: 15px; border: 1px solid #ddd; }}
        table {{ width: 100%; border-collapse: collapse; }}
        th, td {{ padding: 10px; text-align: left; border-bottom: 1px solid #ddd; }}
        th {{ background: #34495e; color: white; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Security Compliance Audit Report</h1>
        <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>
    
    <div class="section">
        <h2>Compliance Score</h2>
        <div class="score">{score}/100</div>
        <p>Total Issues Found: {total_issues}</p>
    </div>
    
    <div class="section">
        <h2>Configuration Audit Findings</h2>
        <table>
            <tr>
                <th>Severity</th>
                <th>Issue</th>
                <th>Recommendation</th>
            </tr>
"""
    
    for finding in results['config']:
        severity_class = finding['severity'].lower()
        html += f"""
            <tr>
                <td class="{severity_class}">{finding['severity']}</td>
                <td>{finding['issue']}</td>
                <td>{finding['recommendation']}</td>
            </tr>
"""
    
    html += """
        </table>
    </div>
    
    <div class="section">
        <h2>Log Analysis Findings</h2>
        <table>
            <tr>
                <th>Severity</th>
                <th>Type</th>
                <th>Details</th>
            </tr>
"""
    
    for finding in results['log']:
        severity_class = finding['severity'].lower()
        html += f"""
            <tr>
                <td class="{severity_class}">{finding['severity']}</td>
                <td>{finding['type']}</td>
                <td>{finding['details']}</td>
            </tr>
"""
    
    html += """
        </table>
    </div>
</body>
</html>
"""
    return html

def main():
    print("=" * 60)
    print("GENERATING COMPLIANCE REPORT")
    print("=" * 60)
    
    print("\n[*] Loading audit results...")
    results = load_audit_results()
    
    print("[*] Calculating compliance score...")
    score, total_issues = calculate_compliance_score(results)
    
    print("[*] Generating HTML report...")
    html_report = generate_html_report(results, score, total_issues)
    
    os.makedirs('reports', exist_ok=True)
    with open('reports/compliance_report.html', 'w') as f:
        f.write(html_report)
    
    print(f"\n[*] Compliance Score: {score}/100")
    print(f"[*] Total Issues: {total_issues}")
    print(f"[*] HTML report saved to reports/compliance_report.html")
    
    print("\nSUMMARY:")
    print(f"  Configuration Issues: {len(results['config'])}")
    print(f"  Log Security Events: {len(results['log'])}")

if __name__ == '__main__':
    main()
