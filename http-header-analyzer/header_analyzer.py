#!/usr/bin/env python3
"""
HTTP Header Security Analyzer
Extracts and analyzes HTTP headers for security issues
"""

import requests
import sys
from colorama import Fore, Style, init

# Initialize colorama for colored output
init(autoreset=True)

# Critical security headers that should be present
SECURITY_HEADERS = {
    'Strict-Transport-Security': 'Enforces HTTPS connections',
    'X-Frame-Options': 'Prevents clickjacking attacks',
    'X-Content-Type-Options': 'Prevents MIME-type sniffing',
    'Content-Security-Policy': 'Controls resource loading',
    'X-XSS-Protection': 'Enables XSS filtering',
    'Referrer-Policy': 'Controls referrer information',
    'Permissions-Policy': 'Controls browser features'
}

# Insecure header values to flag
INSECURE_VALUES = {
    'X-Frame-Options': ['ALLOW', 'ALLOWALL'],
    'X-XSS-Protection': ['0'],
}

def fetch_headers(url):
    """
    Fetch HTTP headers from a given URL
    
    Args:
        url (str): Target URL to analyze
    
    Returns:
        dict: Response headers or None if error
    """
    try:
        response = requests.get(url, timeout=10, allow_redirects=True, verify=True)
        return response.headers
    except requests.exceptions.SSLError:
        print(f"{Fore.YELLOW}[!] SSL Certificate verification failed. Retrying without verification...")
        try:
            response = requests.get(url, timeout=10, allow_redirects=True, verify=False)
            return response.headers
        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}Error fetching URL: {e}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error fetching URL: {e}")
        return None

def display_headers(headers):
    """
    Display all HTTP headers in a formatted way
    
    Args:
        headers (dict): HTTP response headers
    """
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.CYAN}HTTP HEADERS FOUND")
    print(f"{Fore.CYAN}{'='*60}\n")
    
    for key, value in headers.items():
        print(f"{Fore.GREEN}{key}: {Style.RESET_ALL}{value}")

def analyze_security_headers(headers):
    """
    Analyze headers for security issues
    
    Args:
        headers (dict): HTTP response headers
    
    Returns:
        tuple: (missing_headers, insecure_headers)
    """
    missing = []
    insecure = []
    
    # Normalize header keys for case-insensitive comparison
    normalized_headers = {k.lower(): v for k, v in headers.items()}
    
    # Check for missing security headers
    for header, desc in SECURITY_HEADERS.items():
        if header.lower() not in normalized_headers:
            missing.append((header, desc))
    
    # Check for insecure configurations
    for header, insecure_vals in INSECURE_VALUES.items():
        header_lower = header.lower()
        if header_lower in normalized_headers:
            val = normalized_headers[header_lower].upper()
            for bad_val in insecure_vals:
                if bad_val in val:
                    insecure.append((header, normalized_headers[header_lower], f"Insecure value detected (contains '{bad_val}')"))
    
    # Check HSTS max-age if present
    if 'strict-transport-security' in normalized_headers:
        hsts_val = normalized_headers['strict-transport-security']
        if 'max-age=' in hsts_val:
            try:
                # Extract max-age number
                parts = hsts_val.split(';')
                max_age = 0
                for part in parts:
                    if 'max-age' in part:
                        max_age = int(part.split('=')[1].strip())
                if max_age < 15768000: # Less than 6 months
                    insecure.append(('Strict-Transport-Security', hsts_val, 'max-age is too short (< 6 months)'))
            except Exception:
                pass

    return missing, insecure

def display_security_report(missing, insecure):
    """
    Display security analysis report
    
    Args:
        missing (list): List of missing security headers
        insecure (list): List of insecure header configurations
    """
    print(f"\n{Fore.YELLOW}{'='*60}")
    print(f"{Fore.YELLOW}SECURITY ANALYSIS REPORT")
    print(f"{Fore.YELLOW}{'='*60}\n")
    
    # Display missing headers
    if missing:
        print(f"{Fore.RED}Missing Security Headers ({len(missing)}):")
        for header, desc in missing:
            print(f"  - {Fore.RED}{header}{Style.RESET_ALL}: {desc}")
    else:
        print(f"{Fore.GREEN}All critical security headers present!")
    
    # Display insecure configurations
    if insecure:
        print(f"\n{Fore.RED}Insecure Configurations Found ({len(insecure)}):")
        for header, val, reason in insecure:
            print(f"  - {Fore.RED}{header}{Style.RESET_ALL} (Value: '{val}'): {reason}")
    else:
        print(f"\n{Fore.GREEN}No insecure configurations detected!")

def main():
    """
    Main function to run the header analyzer
    """
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}Usage: python3 header_analyzer.py <URL>")
        print(f"{Fore.YELLOW}Example: python3 header_analyzer.py https://example.com")
        sys.exit(1)
    
    url = sys.argv[1]
    
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    print(f"{Fore.CYAN}Analyzing: {url}\n")
    
    headers = fetch_headers(url)
    if not headers:
        sys.exit(1)
        
    display_headers(headers)
    
    missing, insecure = analyze_security_headers(headers)
    display_security_report(missing, insecure)

if __name__ == "__main__":
    main()
