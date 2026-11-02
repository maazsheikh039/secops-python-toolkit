#!/usr/bin/env python3
"""
Enterprise Password Strength Validation Utility
Author: Cloud Platform Engineer / DevSecOps
"""

import re
import sys
import os

def load_common_passwords(filename='common_passwords.txt'):
    """
    Load common passwords from file.
    
    Args:
        filename (str): Path to password dictionary file
    
    Returns:
        set: Set of common passwords (lowercase)
    """
    common_set = set()
    try:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                for line in f:
                    pwd = line.strip().lower()
                    if pwd:
                        common_set.add(pwd)
    except FileNotFoundError:
        pass
    return common_set

# Load dictionary on startup
COMMON_PASSWORDS = load_common_passwords()

def check_length(password):
    """
    Check if password meets minimum length requirement (8-128 characters).
    """
    min_length = 8
    max_length = 128
    
    if min_length <= len(password) <= max_length:
        return (True, "Length is adequate")
    else:
        return (False, f"Password must be {min_length}-{max_length} characters")

def check_complexity(password):
    """
    Check if password contains required character types.
    """
    score = 0
    missing = []
    
    if re.search(r'[a-z]', password):
        score += 1
    else:
        missing.append("Missing lowercase letter")
        
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        missing.append("Missing uppercase letter")
        
    if re.search(r'\d', password):
        score += 1
    else:
        missing.append("Missing digit")
        
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        missing.append("Missing special character")
        
    return (score, missing)

def check_common_patterns(password):
    """
    Check for common weak patterns, sequential numbers/letters, and repetitions.
    """
    issues = []
    pwd_lower = password.lower()
    
    # Dictionary check
    if pwd_lower in COMMON_PASSWORDS:
        issues.append("Password matches a known common weak password.")
        
    # Sequential patterns (e.g., 123, abc)
    if re.search(r'(012|123|234|345|456|567|678|789|890|abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)', pwd_lower):
        issues.append("Password contains sequential characters or numbers.")
        
    # Repeated characters (3+ times, e.g., aaa, 111)
    if re.search(r'(.)\1{2,}', password):
        issues.append("Password contains repeated characters (3 or more times).")
        
    return (len(issues) > 0, issues)

def calculate_strength(password):
    """
    Calculate overall password strength score and feedback.
    """
    total_score = 0
    feedback = []
    
    # Length check
    length_valid, length_msg = check_length(password)
    if not length_valid:
        feedback.append(length_msg)
        return {
            'score': 0,
            'strength': 'Invalid',
            'feedback': feedback
        }
    else:
        total_score += 20
        
    # Complexity check (score 0-4 -> multiplied by 15 = max 60 points)
    comp_score, missing_reqs = check_complexity(password)
    total_score += comp_score * 15
    if missing_reqs:
        feedback.extend(missing_reqs)
        
    # Common pattern check (-30 points if found)
    has_weak, pattern_issues = check_common_patterns(password)
    if has_weak:
        total_score -= 30
        feedback.extend(pattern_issues)
        
    # Length bonus points
    if len(password) > 12:
        total_score += 10
    if len(password) > 16:
        total_score += 10
        
    # Clamp score between 0 and 100
    total_score = max(0, min(100, total_score))
    
    # Determine strength level
    if total_score <= 30:
        strength = 'Weak'
    elif total_score <= 60:
        strength = 'Fair'
    elif total_score <= 80:
        strength = 'Good'
    else:
        strength = 'Strong'
        
    return {
        'score': total_score,
        'strength': strength,
        'feedback': feedback
    }

def batch_test(filename):
    """
    Test multiple passwords from a file.
    """
    print(f"\n--- Batch Testing from {filename} ---")
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return
        
    total, strong_count, weak_count = 0, 0, 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            pwd = line.strip()
            if not pwd:
                continue
            total += 1
            res = calculate_strength(pwd)
            print(f"Password: {pwd:20} | Strength: {res['strength']:8} | Score: {res['score']}")
            if res['strength'] in ['Good', 'Strong']:
                strong_count += 1
            else:
                weak_count += 1
                
    print(f"\nSummary: Total Tested: {total} | Strong/Good: {strong_count} | Weak/Fair/Invalid: {weak_count}")
    print("-" * 45)

def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--batch':
        batch_file = sys.argv[2] if len(sys.argv) > 2 else 'test_passwords.txt'
        batch_test(batch_file)
        return
        
    print("=" * 50)
    print("Password Strength Validator")
    print("=" * 50)
    
    password = input("Enter password to validate: ")
    result = calculate_strength(password)
    
    print("\n--- Validation Results ---")
    print(f"Strength Level : {result['strength']}")
    print(f"Score          : {result['score']}/100")
    if result['feedback']:
        print("Feedback / Issues:")
        for msg in result['feedback']:
            print(f" - {msg}")
    else:
        print("Feedback       : No vulnerabilities or missing requirements detected.")
    print("--------------------------\n")

if __name__ == "__main__":
    main()
