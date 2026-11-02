#!/usr/bin/env python3
"""
IPv4 Address Validator
Validates IPv4 addresses using basic parsing logic
"""

def validate_ipv4(ip_address):
    """
    Validate an IPv4 address.
    
    Args:
        ip_address (str): The IP address to validate
    
    Returns:
        bool: True if valid, False otherwise
    """
    parts = ip_address.split('.')
    
    # Check if there are exactly 4 parts
    if len(parts) != 4:
        return False
    
    # Validate each part
    for part in parts:
        if not part.isdigit():
            return False
        
        num = int(part)
        if num < 0 or num > 255:
            return False
    
    return True


def test_ipv4_addresses():
    """Test the IPv4 validator with sample addresses"""
    test_cases = [
        ("192.168.1.1", True),
        ("10.0.0.1", True),
        ("256.1.1.1", False),
        ("192.168.1", False),
        ("192.168.1.1.1", False),
        ("192.168.-1.1", False),
        ("192.168.1.a", False)
    ]
    
    print("IPv4 Validation Tests:")
    print("-" * 50)
    
    for ip, expected in test_cases:
        result = validate_ipv4(ip)
        status = "PASS" if result == expected else "FAIL"
        print(f"{ip:20} | Expected: {expected:5} | Got: {result:5} | {status}")


if __name__ == "__main__":
    test_ipv4_addresses()
