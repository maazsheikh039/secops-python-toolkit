#!/usr/bin/env python3
"""
Combined Network Identifier Validator
Detects and validates IPv4, IPv6, and hostnames
"""

import ipaddress
import re

def detect_and_validate(identifier):
    """
    Detect the type of network identifier and validate it.
    
    Args:
        identifier (str): The network identifier to validate
    
    Returns:
        tuple: (type, is_valid) where type is 'IPv4', 'IPv6', 'Hostname', or 'Unknown'
    """
    # Try IPv4
    if '.' in identifier and ':' not in identifier:
        try:
            ipaddress.IPv4Address(identifier)
            return ('IPv4', True)
        except ValueError:
            pass
    
    # Try IPv6
    if ':' in identifier:
        try:
            ipaddress.IPv6Address(identifier)
            return ('IPv6', True)
        except ValueError:
            return ('IPv6', False)
    
    # Try Hostname
    if len(identifier) <= 253:
        hostname = identifier[:-1] if identifier.endswith('.') else identifier
        labels = hostname.split('.')
        label_pattern = re.compile(r'^[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?$')
        
        if all(label_pattern.match(label) for label in labels):
            return ('Hostname', True)
    
    return ('Unknown', False)


def main():
    """Interactive validator"""
    print("Network Identifier Validator")
    print("=" * 60)
    print("Enter network identifiers to validate (type 'quit' to exit)")
    print()
    
    test_samples = [
        "192.168.1.1",
        "2001:db8::1",
        "example.com",
        "256.1.1.1",
        "-invalid.com"
    ]
    print("Running automated sanity check on samples...")
    for sample in test_samples:
        t, v = detect_and_validate(sample)
        print(f"Sample: {sample:20} -> Type: {t:10} | Status: {'VALID' if v else 'INVALID'}")
    print("-" * 60)

if __name__ == "__main__":
    main()
