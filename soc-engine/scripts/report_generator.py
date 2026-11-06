#!/usr/bin/env python3
"""
Security report generator
Creates summary reports from detected threats
"""
from datetime import datetime
from collections import Counter
import os

def parse_alerts(alert_file):
    """
    Parse alert file and extract threat information
    """
    threats = []
    if not os.path.exists(alert_file):
        return threats
        
    with open(alert_file, 'r') as f:
        for line in f:
            if "ALERT:" in line:
                try:
                    # Example format: [2026-11-06 13:11:00] ALERT: BRUTE_FORCE -> ...
                    parts = line.split("ALERT:")
                    timestamp = parts[0].strip("[] ")
                    threat_part = parts[1].split("->")[0].strip()
                    threats.append({
                        'timestamp': timestamp,
                        'threat_type': threat_part
                    })
                except Exception:
                    continue
    return threats

def generate_summary(threats):
    """
    Generate summary statistics from threats
    """
    total_threats = len(threats)
    threat_types = [t['threat_type'] for t in threats]
    counts = Counter(threat_types)
    
    breakdown = {}
    for t_type, count in counts.items():
        percentage = (count / total_threats * 100) if total_threats > 0 else 0
        breakdown[t_type] = {
            'count': count,
            'percentage': round(percentage, 2)
        }
        
    summary = {
        'total_threats': total_threats,
        'threat_breakdown': breakdown,
        'report_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return summary

def create_report(summary, output_file):
    """
    Create formatted report file
    """
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w') as f:
        f.write("="*60 + "\n")
        f.write("             SOC AUTOMATED SECURITY INCIDENT REPORT\n")
        f.write("="*60 + "\n")
        f.write(f"Report Generated: {summary['report_time']}\n")
        f.write(f"Total Threats Detected: {summary['total_threats']}\n\n")
        
        f.write("THREAT BREAKDOWN:\n")
        f.write("-" * 40 + "\n")
        for t_type, data in summary['threat_breakdown'].items():
            f.write(f"- {t_type}: {data['count']} occurrences ({data['percentage']}%)\n")
            
        f.write("\n" + "="*60 + "\n")
        f.write("RECOMMENDATIONS:\n")
        f.write("1. Investigate source IP addresses associated with brute_force attempts.\n")
        f.write("2. Review firewall rules to mitigate incoming port scans.\n")
        f.write("3. Inspect unauthorized outbound traffic on port 4444.\n")
        f.write("="*60 + "\n")

def main():
    alert_file = "alerts/threats.txt"
    report_file = "reports/security_report.txt"
    
    print("Generating security report...")
    threats = parse_alerts(alert_file)
    summary = generate_summary(threats)
    create_report(summary, report_file)
    print(f"Report saved to {report_file}")

if __name__ == "__main__":
    main()
