#!/usr/bin/env python3
"""
IPv6 Address Validator
Uses Python's ipaddress module for validation
"""

import ipaddress

def validate_ipv6(ip_address):
    """
    Validate an IPv6 address using ipaddress module.
    
    Args:
        ip_address (str): The IPv6 address to validate
    
    Returns:
        bool: True if valid, False otherwise
    """
    try:
        ipaddress.IPv6Address(ip_address)
        return True
    except ValueError:
        return False


def test_ipv6_addresses():
    """Test the IPv6 validator with sample addresses"""
    test_cases = [
        ("2001:0db8:85a3:0000:0000:8a2e:0370:7334", True),
        ("2001:db8::1", True),
        ("::1", True),
        ("fe80::1", True),
        ("2001:0db8:85a3::8a2e::7334", False),
        ("gggg::", False),
        ("192.168.1.1", False)
    ]
    
    print("IPv6 Validation Tests:")
    print("-" * 70)
    
    for ip, expected in test_cases:
        result = validate_ipv6(ip)
        status = "PASS" if result == expected else "FAIL"
        print(f"{ip:45} | Expected: {expected:5} | Got: {result:5} | {status}")


if __name__ == "__main__":
    test_ipv6_addresses()
