#!/usr/bin/env python3
"""
Security Scanner - A simple CLI tool to scan files for security issues
"""

import argparse
import os
import re
import sys

class SecurityScanner:
    """Main security scanner class"""
    
    def __init__(self):
        """Initialize the scanner with security patterns"""
        self.patterns = {
            'hardcoded_password': r'(password|passwd|pwd)\s*=\s*["\'][^"\']+["\']',
            'api_key': r'(api_key|apikey|api-key)\s*=\s*["\'][^"\']+["\']',
            'private_key': r'-----BEGIN\s+(RSA\s+)?PRIVATE\s+KEY-----',
            'ip_address': r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        }
        self.findings = []
    
    def scan_file(self, filepath):
        """
        Scan a single file for security issues
        
        Args:
            filepath: Path to the file to scan
        """
        if not os.path.isfile(filepath):
            print(f"Error: File '{filepath}' not found")
            return
        
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                lines = content.split('\n')
        except Exception as e:
            print(f"Error reading file: {e}")
            return
        
        for line_num, line in enumerate(lines, start=1):
            for issue_type, pattern in self.patterns.items():
                matches = re.finditer(pattern, line, re.IGNORECASE)
                for match in matches:
                    self.findings.append({
                        'file': filepath,
                        'line': line_num,
                        'type': issue_type,
                        'content': line.strip(),
                        'match': match.group()
                    })
    
    def scan_directory(self, dirpath):
        """
        Scan all files in a directory
        
        Args:
            dirpath: Path to directory to scan
        """
        if not os.path.isdir(dirpath):
            print(f"Error: Directory '{dirpath}' not found")
            return
        
        for root, dirs, files in os.walk(dirpath):
            for filename in files:
                # Skip binary and hidden files
                if filename.startswith('.'):
                    continue
                filepath = os.path.join(root, filename)
                self.scan_file(filepath)
    
    def generate_report(self):
        """Generate and print the security scan report"""
        print("\n" + "="*70)
        print("SECURITY SCAN REPORT")
        print("="*70)
        
        if not self.findings:
            print("\nNo security issues found!")
            return
        
        print(f"\nTotal Issues Found: {len(self.findings)}\n")
        
        # Group findings by type
        by_type = {}
        for finding in self.findings:
            issue_type = finding['type']
            if issue_type not in by_type:
                by_type[issue_type] = []
            by_type[issue_type].append(finding)
        
        # Print findings by type
        for issue_type, items in by_type.items():
            print(f"\n[{issue_type.upper().replace('_', ' ')}] - {len(items)} occurrence(s)")
            print("-" * 70)
            for item in items:
                print(f"  File: {item['file']}")
                print(f"  Line: {item['line']}")
                print(f"  Found: {item['match'][:50]}...")
                print()

def main():
    """Main function to handle CLI arguments and run scanner"""
    parser = argparse.ArgumentParser(
        description='Security Scanner - Scan files for common security issues',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 security_scanner.py -f config.txt
  python3 security_scanner.py -d /path/to/project
  python3 security_scanner.py --file secrets.env
        """
    )
    
    parser.add_argument('-f', '--file', 
                       help='Scan a single file',
                       type=str)
    parser.add_argument('-d', '--directory',
                       help='Scan all files in a directory',
                       type=str)
    
    args = parser.parse_args()
    
    if not args.file and not args.directory:
        parser.print_help()
        sys.exit(1)
    
    scanner = SecurityScanner()
    
    if args.file:
        print(f"Scanning file: {args.file}")
        scanner.scan_file(args.file)
    
    if args.directory:
        print(f"Scanning directory: {args.directory}")
        scanner.scan_directory(args.directory)
    
    scanner.generate_report()

if __name__ == '__main__':
    main()
